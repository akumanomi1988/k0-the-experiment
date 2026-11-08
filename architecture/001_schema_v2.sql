-- Design alignment v2.3: votes.PAUSED and cosmetic-only gold spending (NOT EXECUTED).
-- Project CHAOS v2.0: schema DDL reference; PostgreSQL >= 16.
-- This script defines persistence topology and integrity constraints; not tested against a live PostgreSQL instance.
-- Economy writes MUST use transactional application code/stored procedures respecting ledger and holds.
BEGIN;
CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE campaigns (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(), slug text NOT NULL UNIQUE,
  display_name text NOT NULL, created_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE seasons (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(), campaign_id uuid NOT NULL REFERENCES campaigns(id),
  season_number integer NOT NULL CHECK(season_number>0),
  state text NOT NULL CHECK(state IN ('DRAFT','PREPARED','RUNNING','PAUSED','COMPLETED','ARCHIVED','RECOVERY_REQUIRED','ABORTED')),
  ruleset_hash char(64) NOT NULL, content_hash char(64) NOT NULL, seed char(64) NOT NULL,
  started_at timestamptz, ended_at timestamptz, winner_nation_id uuid,
  engine_version text NOT NULL, season_clock_offset bigint NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(campaign_id,season_number)
);
CREATE TABLE nations (
  season_id uuid NOT NULL REFERENCES seasons(id), nation_id uuid NOT NULL,
  faction_id text NOT NULL CHECK(faction_id IN ('micelios','runicos','ferrinos')),
  era_index smallint NOT NULL DEFAULT 1 CHECK(era_index BETWEEN 1 AND 13),
  historical_points smallint NOT NULL DEFAULT 0 CHECK(historical_points BETWEEN 0 AND 100),
  era_ready_pending boolean NOT NULL DEFAULT false,
  live_state text NOT NULL DEFAULT 'OFFLINE_CONFIRMED' CHECK(live_state IN ('LIVE_CONFIRMED','OFFLINE_CONFIRMED','UNCERTAIN')),
  nation_live_seconds bigint NOT NULL DEFAULT 0 CHECK(nation_live_seconds>=0),
  nation_economy_ms bigint NOT NULL DEFAULT 0 CHECK(nation_economy_ms>=0),
  active_penalty_seconds bigint NOT NULL DEFAULT 0 CHECK(active_penalty_seconds>=0),
  last_simulated_at timestamptz, writer_epoch bigint NOT NULL DEFAULT 0,
  version bigint NOT NULL DEFAULT 0, state text NOT NULL DEFAULT 'ACTIVE',
  PRIMARY KEY(season_id,nation_id), UNIQUE(season_id,faction_id)
);
ALTER TABLE seasons ADD CONSTRAINT fk_winner_in_season
  FOREIGN KEY (id,winner_nation_id) REFERENCES nations(season_id,nation_id)
  DEFERRABLE INITIALLY DEFERRED;
CREATE TABLE channel_bindings (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  season_id uuid NOT NULL, nation_id uuid NOT NULL,
  provider text NOT NULL CHECK(provider IN ('twitch','youtube','tiktok','simulated')),
  provider_channel_id text NOT NULL, display_alias text NOT NULL,
  roles text[] NOT NULL DEFAULT ARRAY['commands','live_health']::text[],
  active boolean NOT NULL DEFAULT false, revision integer NOT NULL DEFAULT 1,
  monetization_enabled boolean NOT NULL DEFAULT false, is_clock_authority boolean NOT NULL DEFAULT false,
  evidence_id text, auth_ref text, created_at timestamptz NOT NULL DEFAULT now(),
  FOREIGN KEY(season_id,nation_id) REFERENCES nations(season_id,nation_id),
  UNIQUE(season_id,provider,provider_channel_id),
  UNIQUE(season_id,nation_id,id), CHECK(cardinality(roles) BETWEEN 1 AND 4)
);
CREATE UNIQUE INDEX ux_one_clock_binding_per_nation ON channel_bindings(season_id,nation_id) WHERE is_clock_authority = true AND active = true;
CREATE TABLE provider_identities (
  provider text NOT NULL, provider_user_id text NOT NULL,
  pseudonym_hash char(64) NOT NULL, last_seen_at timestamptz NOT NULL,
  PRIMARY KEY(provider,provider_user_id)
);
CREATE TABLE citizens (
  season_id uuid NOT NULL, nation_id uuid NOT NULL, id uuid NOT NULL DEFAULT gen_random_uuid(),
  provider text NOT NULL, provider_user_id text NOT NULL,
  profession_id text CHECK(profession_id IN ('food','wood','mine','build','research')),
  joined_at timestamptz NOT NULL, active_until timestamptz,
  xp_milli bigint NOT NULL DEFAULT 0 CHECK(xp_milli>=0),
  level smallint NOT NULL DEFAULT 1 CHECK(level BETWEEN 1 AND 20),
  last_activation_at timestamptz, public_display_name text,
  PRIMARY KEY(season_id,nation_id,id),
  FOREIGN KEY(season_id,nation_id) REFERENCES nations(season_id,nation_id),
  FOREIGN KEY(provider,provider_user_id) REFERENCES provider_identities(provider,provider_user_id),
  UNIQUE(season_id,nation_id,provider,provider_user_id)
);
-- Multiple nations may legitimately have distinct citizens for the same provider identity.
-- The unique key above is (season,nation,provider,provider_user_id), preventing duplication only within nation.
CREATE TABLE selected_skills (
  season_id uuid NOT NULL, nation_id uuid NOT NULL, citizen_id uuid NOT NULL,
  tier smallint NOT NULL CHECK(tier IN (1,2,3)), skill_id text NOT NULL,
  chosen_at timestamptz NOT NULL,
  PRIMARY KEY(season_id,nation_id,citizen_id,tier),
  FOREIGN KEY(season_id,nation_id,citizen_id) REFERENCES citizens(season_id,nation_id,id)
);
CREATE TABLE nation_resource_balances (
  season_id uuid NOT NULL, nation_id uuid NOT NULL,
  resource_id text NOT NULL CHECK(resource_id IN ('food','wood','stone','ore','knowledge','gold')),
  stock bigint NOT NULL DEFAULT 0 CHECK(stock>=0),
  reserved bigint NOT NULL DEFAULT 0 CHECK(reserved>=0 AND reserved<=stock),
  capacity bigint CHECK(capacity IS NULL OR capacity>=0), version bigint NOT NULL DEFAULT 0,
  PRIMARY KEY(season_id,nation_id,resource_id),
  FOREIGN KEY(season_id,nation_id) REFERENCES nations(season_id,nation_id)
);
CREATE TABLE resource_ledger (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(), season_id uuid NOT NULL, nation_id uuid NOT NULL,
  resource_id text NOT NULL, delta bigint NOT NULL CHECK(delta <> 0),
  entry_kind text NOT NULL CHECK(entry_kind IN ('PRODUCE','UPKEEP','BUILD_COST','MISSION_REWARD','TOURNAMENT_PENALTY','CONTRIBUTION_CREDIT','CONTRIBUTION_REVERSAL','COSMETIC_SPEND','ADJUSTMENT_AUDITED','SEASON_CLOSE')),
  cause_id uuid NOT NULL, correlation_id uuid NOT NULL, created_at timestamptz NOT NULL,
  FOREIGN KEY(season_id,nation_id,resource_id) REFERENCES nation_resource_balances(season_id,nation_id,resource_id),
  UNIQUE(season_id,nation_id,resource_id,entry_kind,cause_id),
  CHECK(resource_id<>'gold' OR (entry_kind='CONTRIBUTION_CREDIT' AND delta>0) OR (entry_kind IN ('CONTRIBUTION_REVERSAL','COSMETIC_SPEND','SEASON_CLOSE') AND delta<0))
);
CREATE TABLE gold_debt (
  season_id uuid NOT NULL, nation_id uuid NOT NULL, debt_units bigint NOT NULL DEFAULT 0 CHECK(debt_units>=0),
  PRIMARY KEY(season_id,nation_id), FOREIGN KEY(season_id,nation_id) REFERENCES nations(season_id,nation_id)
);
CREATE TABLE input_events (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(), source_key char(64) NOT NULL UNIQUE,
  binding_id uuid NOT NULL REFERENCES channel_bindings(id), season_id uuid NOT NULL, nation_id uuid NOT NULL,
  provider_timestamp timestamptz, received_at timestamptz NOT NULL, payload_digest char(64) NOT NULL,
  event_type text NOT NULL, command_text text, validated boolean NOT NULL DEFAULT false,
  processing_state text NOT NULL CHECK(processing_state IN ('RECEIVED','VALIDATED','APPLIED','REJECTED','QUARANTINED')),
  ingest_seq bigint GENERATED ALWAYS AS IDENTITY UNIQUE,
  FOREIGN KEY(season_id,nation_id,binding_id) REFERENCES channel_bindings(season_id,nation_id,id)
);
CREATE TABLE contributions (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(), season_id uuid NOT NULL, nation_id uuid NOT NULL,
  binding_id uuid NOT NULL, input_event_id uuid NOT NULL UNIQUE REFERENCES input_events(id),
  provider text NOT NULL, contribution_external_id text NOT NULL, event_type text NOT NULL,
  denomination text NOT NULL, amount_minor_units bigint NOT NULL CHECK(amount_minor_units>0),
  conversion_rule_id text NOT NULL, rule_version text NOT NULL,
  gold_credited bigint NOT NULL DEFAULT 0 CHECK(gold_credited>=0),
  state text NOT NULL CHECK(state IN ('RECEIVED','AUTHENTICATED','VERIFIED','CREDITED','REJECTED','REVERSED')),
  verified_at timestamptz, credited_at timestamptz, created_at timestamptz NOT NULL,
  FOREIGN KEY(season_id,nation_id,binding_id) REFERENCES channel_bindings(season_id,nation_id,id),
  UNIQUE(binding_id,provider,contribution_external_id,event_type)
);
CREATE TABLE buildings (
  season_id uuid NOT NULL, nation_id uuid NOT NULL, id uuid NOT NULL DEFAULT gen_random_uuid(),
  building_catalog_id text NOT NULL, era_index smallint NOT NULL CHECK(era_index BETWEEN 1 AND 13),
  tile_x smallint, tile_y smallint, orientation smallint NOT NULL DEFAULT 0,
  kind text NOT NULL CHECK(kind IN ('BASIC_AUTO','STRATEGIC_OPTIONAL','WONDER')),
  state text NOT NULL CHECK(state IN ('WAITING_RESOURCES','WAITING_PLOT','QUEUED','BUILDING','COMPLETED','CANCELLED')),
  work_total bigint NOT NULL CHECK(work_total>0), work_done bigint NOT NULL DEFAULT 0,
  materials_committed boolean NOT NULL DEFAULT false,
  started_at timestamptz, completed_at timestamptz,
  PRIMARY KEY(season_id,nation_id,id),
  FOREIGN KEY(season_id,nation_id) REFERENCES nations(season_id,nation_id),
  CHECK(work_done>=0 AND work_done<=work_total)
);
CREATE TABLE history_milestones (
  season_id uuid NOT NULL, nation_id uuid NOT NULL, era_index smallint NOT NULL CHECK(era_index BETWEEN 1 AND 13),
  milestone_id text NOT NULL, criteria_json jsonb NOT NULL, progress_json jsonb NOT NULL DEFAULT '{}'::jsonb,
  points smallint NOT NULL CHECK(points BETWEEN 0 AND 100),
  completed_at timestamptz,
  PRIMARY KEY(season_id,nation_id,era_index,milestone_id),
  FOREIGN KEY(season_id,nation_id) REFERENCES nations(season_id,nation_id),
  CHECK(jsonb_typeof(criteria_json) = 'object' AND jsonb_typeof(progress_json) = 'object')
);
CREATE TABLE technologies_completed (
  season_id uuid NOT NULL, nation_id uuid NOT NULL, technology_id text NOT NULL,
  completed_at timestamptz NOT NULL,
  PRIMARY KEY(season_id,nation_id,technology_id),
  FOREIGN KEY(season_id,nation_id) REFERENCES nations(season_id,nation_id)
);
CREATE TABLE votes (
  season_id uuid NOT NULL, nation_id uuid NOT NULL, id uuid NOT NULL DEFAULT gen_random_uuid(),
  vote_kind text NOT NULL CHECK(vote_kind IN ('GOVERNMENT','GOVERNMENT_RUNOFF','PRIORITY','STRATEGIC','RPS')),
  scope_id text NOT NULL, state text NOT NULL CHECK(state IN ('QUEUED','OPEN','PAUSED','RESOLVED','CANCELLED','PAYMENT_BLOCKED')),
  opened_utc timestamptz, closed_utc timestamptz, live_clock_start bigint NOT NULL DEFAULT 0,
  duration_seconds bigint NOT NULL CHECK(duration_seconds>0),
  option_ids text[] NOT NULL, winner_option text, result_digest char(64),
  PRIMARY KEY(season_id,nation_id,id),
  FOREIGN KEY(season_id,nation_id) REFERENCES nations(season_id,nation_id)
);
CREATE UNIQUE INDEX ux_only_one_open_strategic_vote_per_nation
 ON votes(season_id,nation_id) WHERE vote_kind='STRATEGIC' AND state='OPEN';
CREATE TABLE ballots (
  season_id uuid NOT NULL, nation_id uuid NOT NULL, vote_id uuid NOT NULL,
  citizen_id uuid NOT NULL, option_id text NOT NULL, command_event_id uuid NOT NULL UNIQUE REFERENCES input_events(id),
  voted_at timestamptz NOT NULL,
  PRIMARY KEY(season_id,nation_id,vote_id,citizen_id),
  FOREIGN KEY(season_id,nation_id,vote_id) REFERENCES votes(season_id,nation_id,id),
  FOREIGN KEY(season_id,nation_id,citizen_id) REFERENCES citizens(season_id,nation_id,id)
);
CREATE TABLE vote_holds (
  season_id uuid NOT NULL, nation_id uuid NOT NULL, vote_id uuid NOT NULL,
  resource_id text NOT NULL, amount bigint NOT NULL CHECK(amount>=0),
  PRIMARY KEY(season_id,nation_id,vote_id,resource_id),
  FOREIGN KEY(season_id,nation_id,vote_id) REFERENCES votes(season_id,nation_id,id),
  FOREIGN KEY(season_id,nation_id,resource_id) REFERENCES nation_resource_balances(season_id,nation_id,resource_id)
);
CREATE TABLE missions_claimed (
  season_id uuid NOT NULL, nation_id uuid NOT NULL, mission_id text NOT NULL,
  period_start_utc timestamptz NOT NULL, claim_at timestamptz NOT NULL,
  PRIMARY KEY(season_id,nation_id,mission_id,period_start_utc),
  FOREIGN KEY(season_id,nation_id) REFERENCES nations(season_id,nation_id)
);
CREATE TABLE wonders_global (
  season_id uuid NOT NULL REFERENCES seasons(id), wonder_id text NOT NULL,
  winner_nation_id uuid NOT NULL, building_id uuid NOT NULL, claimed_at timestamptz NOT NULL,
  PRIMARY KEY(season_id,wonder_id),
  FOREIGN KEY(season_id,winner_nation_id,building_id) REFERENCES buildings(season_id,nation_id,id)
);
CREATE TABLE season_winner_claims (
  season_id uuid PRIMARY KEY REFERENCES seasons(id), nation_id uuid NOT NULL,
  event_sequence bigint NOT NULL, claimed_at timestamptz NOT NULL,
  FOREIGN KEY(season_id,nation_id) REFERENCES nations(season_id,nation_id)
);
CREATE TABLE nation_snapshots (
  season_id uuid NOT NULL, nation_id uuid NOT NULL, snapshot_sequence bigint NOT NULL,
  content_hash char(64) NOT NULL, ruleset_hash char(64) NOT NULL, state_hash char(64) NOT NULL,
  state_json jsonb NOT NULL, stored_at timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY(season_id,nation_id,snapshot_sequence),
  FOREIGN KEY(season_id,nation_id) REFERENCES nations(season_id,nation_id)
);
CREATE TABLE event_outbox (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(), season_id uuid NOT NULL REFERENCES seasons(id),
  nation_id uuid, event_type text NOT NULL, event_version integer NOT NULL DEFAULT 2,
  payload jsonb NOT NULL, occurred_at timestamptz NOT NULL,
  published_at timestamptz, retry_count integer NOT NULL DEFAULT 0,
  UNIQUE(id,season_id), FOREIGN KEY(season_id,nation_id) REFERENCES nations(season_id,nation_id)
);
CREATE INDEX ix_outbox_pending ON event_outbox(occurred_at,id) WHERE published_at IS NULL;
CREATE TABLE audit_log (
  id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  season_id uuid REFERENCES seasons(id), actor_type text NOT NULL, actor_id text NOT NULL,
  action text NOT NULL, reason text NOT NULL, correlation_id uuid NOT NULL,
  details jsonb NOT NULL DEFAULT '{}'::jsonb, created_at timestamptz NOT NULL DEFAULT now()
);
COMMIT;
