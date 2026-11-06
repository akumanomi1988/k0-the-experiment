-- K0: The Experiment v2.2. DESIGN SCHEMA ADDENDUM ONLY.
-- NOT AN EXECUTED MIGRATION. Requires PostgreSQL integration tests and migration review.
-- Run only after 001_schema_v2.sql in isolated development database.
BEGIN;

-- Per-building cohort state prevents one database row per rendered soldier.
CREATE TABLE garrison_cohorts (
  season_id uuid NOT NULL,
  nation_id uuid NOT NULL,
  defense_building_id uuid NOT NULL,
  unit_catalog_id text NOT NULL,
  units_count integer NOT NULL DEFAULT 0 CHECK (units_count BETWEEN 0 AND 6),
  last_spawn_live_second bigint NOT NULL DEFAULT 0 CHECK (last_spawn_live_second >= 0),
  version bigint NOT NULL DEFAULT 0,
  PRIMARY KEY (season_id,nation_id,defense_building_id,unit_catalog_id),
  FOREIGN KEY (season_id,nation_id,defense_building_id)
      REFERENCES buildings(season_id,nation_id,id),
  FOREIGN KEY (season_id,nation_id) REFERENCES nations(season_id,nation_id)
);
-- Application: only completed defense buildings may own cohorts; across all cohorts
-- enforce <=6 units per building and <=120 per nation under writer transaction.

CREATE TABLE automated_battles (
  season_id uuid NOT NULL REFERENCES seasons(id),
  id uuid NOT NULL DEFAULT gen_random_uuid(),
  state text NOT NULL CHECK (state IN ('SCHEDULED','WAITING_LIVE','RUNNING','RESOLVED','CANCELLED')),
  scheduled_by text NOT NULL,
  scheduled_at timestamptz NOT NULL,
  started_at timestamptz,
  resolved_at timestamptz,
  ruleset_hash char(64) NOT NULL,
  content_hash char(64) NOT NULL,
  result_digest char(64),
  PRIMARY KEY (season_id,id)
);
CREATE TABLE automated_battle_participants (
  season_id uuid NOT NULL,
  battle_id uuid NOT NULL,
  nation_id uuid NOT NULL,
  effective_strength bigint NOT NULL DEFAULT 0 CHECK (effective_strength >= 0),
  scored_points integer NOT NULL DEFAULT 0 CHECK (scored_points BETWEEN 0 AND 4),
  resource_penalty_milli bigint NOT NULL DEFAULT 0 CHECK(resource_penalty_milli >= 0),
  territory_penalty_seconds bigint NOT NULL DEFAULT 0 CHECK(territory_penalty_seconds >= 0),
  PRIMARY KEY (season_id,battle_id,nation_id),
  FOREIGN KEY (season_id,battle_id) REFERENCES automated_battles(season_id,id),
  FOREIGN KEY (season_id,nation_id) REFERENCES nations(season_id,nation_id)
);
-- Pairwise scores 2/1/0, max 4 per nation over 2 pairings. Three rows required by
-- domain gate before RESOLVED; no gold or world destruction. Prevent duplicate
-- penalties with unique cause IDs in resource_ledger.

CREATE TABLE cosmetic_sponsorships (
  season_id uuid NOT NULL,
  nation_id uuid NOT NULL,
  id uuid NOT NULL DEFAULT gen_random_uuid(),
  citizen_id uuid NOT NULL,
  catalog_item_id text NOT NULL,
  state text NOT NULL CHECK(state IN ('REQUESTED','APPROVED','DELIVERED','REVOKED','REJECTED')),
  gold_spend_ledger_id uuid UNIQUE REFERENCES resource_ledger(id),
  moderated_display_name text,
  display_consent boolean NOT NULL DEFAULT false,
  public_text text,
  created_at timestamptz NOT NULL DEFAULT now(),
  moderated_at timestamptz,
  revoked_at timestamptz,
  PRIMARY KEY(season_id,nation_id,id),
  FOREIGN KEY(season_id,nation_id,citizen_id) REFERENCES citizens(season_id,nation_id,id),
  UNIQUE(season_id,nation_id,citizen_id,catalog_item_id),
  CHECK ((state NOT IN ('APPROVED','DELIVERED')) OR display_consent = true)
);
-- A future versioned migration must extend `resource_ledger.entry_kind` gold CHECK
-- to include a negative COSMETIC_SPEND event. It is NOT safe to misuse BUILD_COST.
-- Do not attempt the migration without checking live DB constraint names/versions.

COMMIT;
