-- K0 v2.2: migration for integrity of FREE councils and garrisons.
-- Execute once after 001_schema_v2.sql and 002_extensiones_diseno_v2.2.sql.
-- Only tested on an isolated PostgreSQL instance; production migration requires backups.
BEGIN;

ALTER TABLE vote_holds
  ADD CONSTRAINT ck_vote_holds_ordinary_only CHECK (resource_id <> 'gold');

ALTER TABLE votes
  ADD CONSTRAINT ck_strategic_never_payment_blocked
  CHECK (vote_kind <> 'STRATEGIC' OR state <> 'PAYMENT_BLOCKED');

ALTER TABLE resource_ledger DROP CONSTRAINT resource_ledger_entry_kind_check;
ALTER TABLE resource_ledger
  ADD CONSTRAINT ck_resource_ledger_entry_kind_v22
  CHECK (entry_kind IN (
    'PRODUCE','UPKEEP','BUILD_COST','MISSION_REWARD','TOURNAMENT_PENALTY',
    'CONTRIBUTION_CREDIT','CONTRIBUTION_REVERSAL','ADJUSTMENT_AUDITED',
    'SEASON_CLOSE','COSMETIC_SPEND'
  ));

-- Original unlabelled gold CHECK on the base table is named resource_ledger_check
-- by PostgreSQL. Verify its definition before dropping in a live migration.
DO $$
DECLARE old_def text;
BEGIN
  SELECT pg_get_constraintdef(oid) INTO old_def
  FROM pg_constraint WHERE conrelid = 'resource_ledger'::regclass
    AND conname = 'resource_ledger_check' AND contype = 'c';
  IF old_def IS NULL OR old_def NOT LIKE '%resource_id%' OR old_def NOT LIKE '%gold%' THEN
    RAISE EXCEPTION 'Unknown resource_ledger gold constraint; manual review required';
  END IF;
END $$;
ALTER TABLE resource_ledger DROP CONSTRAINT resource_ledger_check;
ALTER TABLE resource_ledger
  ADD CONSTRAINT ck_resource_ledger_gold_only_cosmetics_v22
  CHECK (
    (resource_id = 'gold' AND (
      (entry_kind = 'CONTRIBUTION_CREDIT' AND delta > 0)
      OR (entry_kind IN ('CONTRIBUTION_REVERSAL','COSMETIC_SPEND','SEASON_CLOSE') AND delta < 0)
    ))
    OR
    (resource_id <> 'gold' AND entry_kind NOT IN (
      'CONTRIBUTION_CREDIT','CONTRIBUTION_REVERSAL','COSMETIC_SPEND'
    ))
  );

-- Writers must already serialize on nations before invoking this trigger.
-- The DB lock protects against accidental bypasses by concurrent writers.
CREATE OR REPLACE FUNCTION assert_garrison_capacity_v22()
RETURNS trigger LANGUAGE plpgsql AS $$
DECLARE total_building int; total_nation int;
BEGIN
  PERFORM 1 FROM nations n
    WHERE n.season_id = NEW.season_id AND n.nation_id = NEW.nation_id
    FOR UPDATE;
  IF NOT FOUND THEN
    RAISE EXCEPTION 'Garrison nation not found' USING ERRCODE='23503';
  END IF;

  PERFORM 1 FROM buildings b
    WHERE b.season_id = NEW.season_id AND b.nation_id = NEW.nation_id
      AND b.id = NEW.defense_building_id
      AND b.kind = 'BASIC_AUTO' AND b.state = 'COMPLETED'
      AND b.building_catalog_id LIKE '%_defense';
  IF NOT FOUND THEN
    RAISE EXCEPTION 'Garrison requires completed defense building' USING ERRCODE='23514';
  END IF;

  SELECT COALESCE(SUM(c.units_count), 0) INTO total_building
  FROM garrison_cohorts c
  WHERE c.season_id = NEW.season_id AND c.nation_id = NEW.nation_id
    AND c.defense_building_id = NEW.defense_building_id
    AND (TG_OP = 'INSERT' OR (
      c.unit_catalog_id <> OLD.unit_catalog_id
      OR c.defense_building_id <> OLD.defense_building_id
      OR c.nation_id <> OLD.nation_id OR c.season_id <> OLD.season_id
    ));
  IF total_building + NEW.units_count > 6 THEN
    RAISE EXCEPTION 'Building garrison cap 6 exceeded' USING ERRCODE='23514';
  END IF;

  SELECT COALESCE(SUM(c.units_count), 0) INTO total_nation
  FROM garrison_cohorts c
  WHERE c.season_id = NEW.season_id AND c.nation_id = NEW.nation_id
    AND (TG_OP = 'INSERT' OR (
      c.unit_catalog_id <> OLD.unit_catalog_id
      OR c.defense_building_id <> OLD.defense_building_id
      OR c.nation_id <> OLD.nation_id OR c.season_id <> OLD.season_id
    ));
  IF total_nation + NEW.units_count > 120 THEN
    RAISE EXCEPTION 'Nation garrison cap 120 exceeded' USING ERRCODE='23514';
  END IF;

  RETURN NEW;
END $$;

CREATE TRIGGER trg_assert_garrison_capacity_v22
BEFORE INSERT OR UPDATE OF units_count, unit_catalog_id, defense_building_id,
  season_id, nation_id ON garrison_cohorts
FOR EACH ROW EXECUTE FUNCTION assert_garrison_capacity_v22();

COMMIT;
