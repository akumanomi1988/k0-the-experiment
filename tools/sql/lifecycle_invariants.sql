-- Design-only, transactional negative tests on an EMPTY PostgreSQL 16 database.
-- Proves DDL constraints, not the absent .NET command handler or real OAuth.
BEGIN;
DO $$
DECLARE
  campaign uuid;
  season uuid;
  nation_a uuid := gen_random_uuid();
  nation_b uuid := gen_random_uuid();
  primary_acc uuid;
  owner_acc uuid;
  second_acc uuid;
  incident uuid;
  baseline timestamptz := '2026-11-09 10:00:00+00'::timestamptz;
BEGIN
  INSERT INTO campaigns(slug, display_name)
    VALUES ('test-lifecycle', 'DB lifecycle verification') RETURNING id INTO campaign;
  INSERT INTO seasons(campaign_id, season_number, state, ruleset_hash,
                      content_hash, seed, engine_version)
    VALUES (campaign, 1, 'PAUSED', repeat('a',64), repeat('b',64),
            repeat('c',64), 'design-test') RETURNING id INTO season;
  INSERT INTO nations(season_id,nation_id,faction_id)
    VALUES (season,nation_a,'micelios'), (season,nation_b,'runicos');
  INSERT INTO k0_accounts(issuer,subject_hash,status)
    VALUES ('test',repeat('1',64),'ACTIVE') RETURNING id INTO primary_acc;
  INSERT INTO k0_accounts(issuer,subject_hash,status)
    VALUES ('test',repeat('2',64),'ACTIVE') RETURNING id INTO owner_acc;
  INSERT INTO k0_accounts(issuer,subject_hash,status)
    VALUES ('test',repeat('3',64),'ACTIVE') RETURNING id INTO second_acc;
  INSERT INTO campaign_memberships(campaign_id,account_id,role,state)
    VALUES(campaign,owner_acc,'OWNER','ACTIVE');
  INSERT INTO season_primary_departures
    (season_id,primary_account_id,nation_id,confirmed_at,cancel_after,state,confirmed_by_account_id)
    VALUES(season,primary_acc,nation_a,baseline,baseline + interval '7 days',
           'PAUSED',owner_acc) RETURNING id INTO incident;

  -- One active incident per season; second attempt must fail.
  BEGIN
    INSERT INTO season_primary_departures
      (season_id,primary_account_id,nation_id,confirmed_at,cancel_after,state,confirmed_by_account_id)
      VALUES(season,primary_acc,nation_a,baseline,baseline + interval '7 days',
             'PAUSED',owner_acc);
    RAISE EXCEPTION 'Multiple active departure incidents incorrectly accepted';
  EXCEPTION WHEN unique_violation THEN
    NULL;
  END;

  -- Wrong broadcaster and at-deadline return must be rejected by CHECK.
  BEGIN
    UPDATE season_primary_departures SET state='RESUMED',
      returned_primary_account_id=second_acc,
      reverified_at=baseline + interval '1 day',
      resolved_at=baseline + interval '1 day',
      resumed_by_owner_account_id=owner_acc WHERE id=incident;
    RAISE EXCEPTION 'Return by wrong primary incorrectly accepted';
  EXCEPTION WHEN check_violation THEN
    NULL;
  END;
  BEGIN
    UPDATE season_primary_departures SET state='RESUMED',
      returned_primary_account_id=primary_acc,
      reverified_at=baseline + interval '7 days',
      resolved_at=baseline + interval '7 days',
      resumed_by_owner_account_id=owner_acc WHERE id=incident;
    RAISE EXCEPTION 'Return at cancellation deadline incorrectly accepted';
  EXCEPTION WHEN check_violation THEN
    NULL;
  END;

  -- Strict-before deadline success: now a second departure can be recorded.
  UPDATE season_primary_departures SET state='RESUMED',
    returned_primary_account_id=primary_acc,
    reverified_at=baseline + interval '7 days' - interval '2 milliseconds',
    resolved_at=baseline + interval '7 days' - interval '1 millisecond',
    resumed_by_owner_account_id=owner_acc WHERE id=incident;
  INSERT INTO season_primary_departures
    (season_id,primary_account_id,nation_id,confirmed_at,cancel_after,state,confirmed_by_account_id)
    VALUES(season,primary_acc,nation_a,baseline + interval '8 days',
           baseline + interval '15 days','PAUSED',owner_acc)
    RETURNING id INTO incident;
  UPDATE season_primary_departures SET state='ABORTED',
    resolved_at=baseline + interval '15 days' WHERE id=incident;

  -- Aborted seasons have NO winner, regardless of event ordering.
  BEGIN
    UPDATE seasons SET state='ABORTED', winner_nation_id=nation_a WHERE id=season;
    RAISE EXCEPTION 'ABORTED season winner incorrectly accepted';
  EXCEPTION WHEN check_violation THEN
    NULL;
  END;
  UPDATE seasons SET state='ABORTED', winner_nation_id=NULL WHERE id=season;

  -- Council vote cannot ever be PAYMENT_BLOCKED by optional gold.
  BEGIN
    INSERT INTO votes(season_id,nation_id,vote_kind,scope_id,state,duration_seconds,option_ids)
      VALUES(season,nation_a,'STRATEGIC','test-council','PAYMENT_BLOCKED',600,
             ARRAY['one','two','three']);
    RAISE EXCEPTION 'Obsolete PAYMENT_BLOCKED Council state incorrectly accepted';
  EXCEPTION WHEN check_violation THEN
    NULL;
  END;

  -- Viewer account is unique per season, even when provider identity differs.
  INSERT INTO provider_identities(provider,provider_user_id,pseudonym_hash,last_seen_at)
    VALUES('simulated','one',repeat('d',64),baseline),
          ('simulated','two',repeat('e',64),baseline);
  INSERT INTO citizens(season_id,nation_id,provider,provider_user_id,joined_at,account_id)
    VALUES(season,nation_a,'simulated','one',baseline,primary_acc);
  BEGIN
    INSERT INTO citizens(season_id,nation_id,provider,provider_user_id,joined_at,account_id)
      VALUES(season,nation_b,'simulated','two',baseline,primary_acc);
    RAISE EXCEPTION 'Same K0 account joined two nations';
  EXCEPTION WHEN unique_violation THEN
    NULL;
  END;
  RAISE NOTICE 'PASS: strict deadline, same primary, repeat departure, unique K0 account, abort/no winner, no Council gold block';
END;
$$;
ROLLBACK;
