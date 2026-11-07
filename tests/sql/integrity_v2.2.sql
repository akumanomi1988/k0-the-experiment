-- Requires 001 + 002 + 003 on a fresh isolated PostgreSQL 16 database.
-- Any failed assertion raises an exception and fails CI.
BEGIN;
DO $$
DECLARE
  campaign uuid; season uuid; nation uuid; defense uuid; vote_id uuid;
  resource_ledger_id uuid; i integer; test_building uuid;
BEGIN
  INSERT INTO campaigns(slug,display_name)
    VALUES ('ci-v22-integrity', 'CI Test Campaign') RETURNING id INTO campaign;
  INSERT INTO seasons(campaign_id, season_number, state, ruleset_hash,
                      content_hash, seed, engine_version)
    VALUES(campaign, 1, 'DRAFT', repeat('a',64), repeat('b',64),
           repeat('c',64), 'ci-v2.2') RETURNING id INTO season;
  nation := gen_random_uuid();
  INSERT INTO nations(season_id,nation_id,faction_id)
    VALUES(season,nation,'micelios');
  INSERT INTO nation_resource_balances(season_id,nation_id,resource_id,stock,reserved)
    VALUES (season,nation,'food',5000000,0), (season,nation,'gold',1000,0);

  -- Gold credit and cosmetic spend are legal, competitive gold spend is not.
  INSERT INTO resource_ledger(season_id,nation_id,resource_id,delta,entry_kind,
                              cause_id,correlation_id,created_at)
    VALUES (season,nation,'gold',100,'CONTRIBUTION_CREDIT',
            gen_random_uuid(),gen_random_uuid(),now());
  INSERT INTO resource_ledger(season_id,nation_id,resource_id,delta,entry_kind,
                              cause_id,correlation_id,created_at)
    VALUES (season,nation,'gold',-25,'COSMETIC_SPEND',
            gen_random_uuid(),gen_random_uuid(),now());
  BEGIN
    INSERT INTO resource_ledger(season_id,nation_id,resource_id,delta,entry_kind,
                                cause_id,correlation_id,created_at)
      VALUES (season,nation,'gold',-100,'BUILD_COST',
              gen_random_uuid(),gen_random_uuid(),now());
    RAISE EXCEPTION 'FAIL: competitive gold BUILD_COST accepted';
  EXCEPTION WHEN check_violation THEN NULL;
  END;
  BEGIN
    INSERT INTO resource_ledger(season_id,nation_id,resource_id,delta,entry_kind,
                                cause_id,correlation_id,created_at)
      VALUES (season,nation,'food',-1,'COSMETIC_SPEND',
              gen_random_uuid(),gen_random_uuid(),now());
    RAISE EXCEPTION 'FAIL: cosmetic ordinary resource spend accepted';
  EXCEPTION WHEN check_violation THEN NULL;
  END;

  INSERT INTO votes(season_id,nation_id,vote_kind,scope_id,state,duration_seconds,option_ids)
    VALUES (season,nation,'STRATEGIC','council-test','OPEN',600,
            ARRAY['a','b','c']) RETURNING id INTO vote_id;
  BEGIN
    INSERT INTO vote_holds(season_id,nation_id,vote_id,resource_id,amount)
      VALUES(season,nation,vote_id,'gold',10);
    RAISE EXCEPTION 'FAIL: council gold hold accepted';
  EXCEPTION WHEN check_violation THEN NULL;
  END;
  INSERT INTO vote_holds(season_id,nation_id,vote_id,resource_id,amount)
    VALUES(season,nation,vote_id,'food',100);
  BEGIN
    UPDATE votes SET state='PAYMENT_BLOCKED'
      WHERE season_id=season AND nation_id=nation AND id=vote_id;
    RAISE EXCEPTION 'FAIL: council PAYMENT_BLOCKED accepted';
  EXCEPTION WHEN check_violation THEN NULL;
  END;

  INSERT INTO buildings(season_id,nation_id,building_catalog_id,era_index,
                        kind,state,work_total,work_done,materials_committed)
    VALUES(season,nation,'paleolithic_defense',1,'BASIC_AUTO','COMPLETED',100,100,true)
    RETURNING id INTO defense;
  INSERT INTO garrison_cohorts(season_id,nation_id,defense_building_id,
                               unit_catalog_id,units_count)
    VALUES(season,nation,defense,'paleolithic_guard',4),
          (season,nation,defense,'paleolithic_scout',2);
  BEGIN
    INSERT INTO garrison_cohorts(season_id,nation_id,defense_building_id,
                                 unit_catalog_id,units_count)
      VALUES(season,nation,defense,'paleolithic_heavy',1);
    RAISE EXCEPTION 'FAIL: garrison 7/6 accepted';
  EXCEPTION WHEN check_violation THEN NULL;
  END;
  BEGIN
    UPDATE garrison_cohorts SET units_count=5
      WHERE season_id=season AND nation_id=nation
        AND defense_building_id=defense AND unit_catalog_id='paleolithic_guard';
    RAISE EXCEPTION 'FAIL: garrison update 7/6 accepted';
  EXCEPTION WHEN check_violation THEN NULL;
  END;
  BEGIN
    INSERT INTO buildings(season_id,nation_id,building_catalog_id,era_index,
                          kind,state,work_total,work_done,materials_committed)
      VALUES(season,nation,'paleolithic_civic',1,'BASIC_AUTO','COMPLETED',100,100,true)
      RETURNING id INTO test_building;
    INSERT INTO garrison_cohorts(season_id,nation_id,defense_building_id,
                                 unit_catalog_id,units_count)
      VALUES(season,nation,test_building,'paleolithic_guard',1);
    RAISE EXCEPTION 'FAIL: garrison non-defense accepted';
  EXCEPTION WHEN check_violation THEN NULL;
  END;

  -- Synthetic stress fixtures: 20 completed defense sites × 6 units.
  -- This only tests the nation cap, not the gameplay per-era building allowance.
  FOR i IN 1..19 LOOP
    INSERT INTO buildings(season_id,nation_id,building_catalog_id,era_index,
                          kind,state,work_total,work_done,materials_committed)
      VALUES(season,nation,'paleolithic_defense',1,'BASIC_AUTO','COMPLETED',100,100,true)
      RETURNING id INTO test_building;
    INSERT INTO garrison_cohorts(season_id,nation_id,defense_building_id,
                                 unit_catalog_id,units_count)
      VALUES(season,nation,test_building,'paleolithic_guard',6);
  END LOOP;
  BEGIN
    INSERT INTO buildings(season_id,nation_id,building_catalog_id,era_index,
                          kind,state,work_total,work_done,materials_committed)
      VALUES(season,nation,'paleolithic_defense',1,'BASIC_AUTO','COMPLETED',100,100,true)
      RETURNING id INTO test_building;
    INSERT INTO garrison_cohorts(season_id,nation_id,defense_building_id,
                                 unit_catalog_id,units_count)
      VALUES(season,nation,test_building,'paleolithic_guard',1);
    RAISE EXCEPTION 'FAIL: nation 121/120 accepted';
  EXCEPTION WHEN check_violation THEN NULL;
  END;

  RAISE NOTICE 'PASS: gold-only cosmetic, council FREE, garrison 6/120, defense ownership';
END $$;
ROLLBACK;
