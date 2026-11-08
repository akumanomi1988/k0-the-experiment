-- K0 / Project CHAOS v2.3 — DISTRIBUTED MULTISTREAMER DESIGN ADDENDUM.
-- NOT A PRODUCTION MIGRATION. Not run against PostgreSQL.
-- Requires architecture/001_schema_v2.sql and design/002; review conflicts,
-- migrate CHECK votes.state for PAUSED, NationId DTO and resource_ledger gold kind.
-- No provider OAuth access tokens or overlay secrets in clear text in database.
BEGIN;

CREATE TABLE k0_accounts (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  issuer text NOT NULL,
  subject_hash char(64) NOT NULL,
  status text NOT NULL CHECK (status IN ('ACTIVE','DISABLED')),
  created_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE (issuer,subject_hash)
);

CREATE TABLE campaign_memberships (
  campaign_id uuid NOT NULL REFERENCES campaigns(id),
  account_id uuid NOT NULL REFERENCES k0_accounts(id),
  role text NOT NULL CHECK (role IN ('OWNER','OPERATOR','BROADCASTER','MODERATOR','AUDITOR')),
  state text NOT NULL CHECK (state IN ('INVITED','ACTIVE','REVOKED')),
  created_at timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (campaign_id,account_id,role)
);

CREATE TABLE streamer_seats (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  season_id uuid NOT NULL,
  nation_id uuid NOT NULL,
  account_id uuid NOT NULL REFERENCES k0_accounts(id),
  role text NOT NULL CHECK (role IN ('BROADCASTER','COHOST','MODERATOR')),
  seat_state text NOT NULL CHECK (seat_state IN ('INVITED','ACCEPTED','REVOKED','LEFT')),
  is_primary boolean NOT NULL DEFAULT false,
  accepted_at timestamptz,
  FOREIGN KEY (season_id,nation_id) REFERENCES nations(season_id,nation_id),
  UNIQUE (season_id,nation_id,account_id,role)
);
-- Exactly one accepted primary broadcaster per nation in multistreamer mode.
CREATE UNIQUE INDEX ux_primary_streamer_per_nation
  ON streamer_seats(season_id,nation_id)
  WHERE seat_state='ACCEPTED' AND is_primary=true;

CREATE TABLE streamer_invitations (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  campaign_id uuid NOT NULL REFERENCES campaigns(id),
  season_id uuid NOT NULL,
  nation_id uuid NOT NULL,
  created_by_account_id uuid NOT NULL REFERENCES k0_accounts(id),
  token_sha256 char(64) NOT NULL UNIQUE,
  role text NOT NULL CHECK (role IN ('BROADCASTER','COHOST','MODERATOR')),
  state text NOT NULL CHECK (state IN ('PENDING','ACCEPTED','REVOKED','EXPIRED')),
  expires_at timestamptz NOT NULL,
  accepted_by_account_id uuid REFERENCES k0_accounts(id),
  accepted_at timestamptz,
  created_at timestamptz NOT NULL DEFAULT now(),
  FOREIGN KEY (season_id,nation_id) REFERENCES nations(season_id,nation_id),
  CHECK (expires_at > created_at)
);
-- Accept within a single transaction with row lock, state=PENDING and now()<expires_at.

CREATE TABLE provider_connections (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  account_id uuid NOT NULL REFERENCES k0_accounts(id),
  provider text NOT NULL CHECK (provider IN ('twitch','youtube','tiktok','simulated')),
  provider_account_id text NOT NULL,
  status text NOT NULL CHECK (status IN ('PENDING','AUTHORIZED','REVOKED','EXPIRED','DISABLED')),
  credential_secret_ref text,
  token_version integer NOT NULL DEFAULT 1 CHECK (token_version >= 1),
  authorized_at timestamptz,
  revoked_at timestamptz,
  UNIQUE(account_id,provider,provider_account_id)
);
-- credential_secret_ref resolves only in server-side secrets manager; never in overlay.

CREATE TABLE provider_capability_evidence (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  connection_id uuid NOT NULL REFERENCES provider_connections(id),
  capability text NOT NULL CHECK(capability IN (
    'CHAT_READ','LIVE_PRESENCE','CHAT_WRITE','EVENTS_MONETARY',
    'EVENTS_REVERSAL','CURSOR_RESUME','ACCOUNT_IDENTITY',
    'OUTPUT_DISTRIBUTION_POLICY')),
  status text NOT NULL CHECK(status IN ('DISABLED','PENDING_VERIFICATION','VERIFIED','REVOKED','NOT_AVAILABLE')),
  source_url text,
  checked_at timestamptz NOT NULL,
  checked_by uuid NOT NULL REFERENCES k0_accounts(id),
  evidence_digest char(64),
  UNIQUE(connection_id,capability)
);

-- Old bindings may be unlinked; production migration will require relation for
-- active real channels, but cannot backfill invented authorizations.
ALTER TABLE channel_bindings ADD COLUMN provider_connection_id uuid REFERENCES provider_connections(id);
ALTER TABLE channel_bindings ADD COLUMN owner_account_id uuid REFERENCES k0_accounts(id);
ALTER TABLE channel_bindings ADD COLUMN binding_revision_changed_at timestamptz;

CREATE TABLE provider_live_sessions (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  binding_id uuid NOT NULL REFERENCES channel_bindings(id),
  provider_session_id text NOT NULL,
  health_state text NOT NULL CHECK (health_state IN ('LIVE_CONFIRMED','OFFLINE_CONFIRMED','UNCERTAIN')),
  started_at timestamptz,
  ended_at timestamptz,
  last_provider_evidence_at timestamptz,
  authority_revision integer NOT NULL CHECK(authority_revision >= 1),
  UNIQUE(binding_id,provider_session_id)
);
CREATE INDEX ix_live_session_health ON provider_live_sessions(binding_id,health_state);
CREATE UNIQUE INDEX ux_active_provider_live_session
  ON provider_live_sessions(binding_id)
  WHERE health_state='LIVE_CONFIRMED' AND ended_at IS NULL;

CREATE TABLE broadcast_outputs (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  season_id uuid NOT NULL,
  primary_nation_id uuid NOT NULL,
  owner_account_id uuid NOT NULL REFERENCES k0_accounts(id),
  view_mode text NOT NULL CHECK(view_mode IN ('NATION_FOCUS','SHARED_WORLD','EVENT_STAGE','SAFE_SCENE')),
  layout_mode text NOT NULL CHECK(layout_mode IN ('VERTICAL_360_640','HORIZONTAL_640_360')),
  locale text NOT NULL DEFAULT 'es' CHECK(locale IN ('es','en')),
  output_state text NOT NULL CHECK(output_state IN ('ACTIVE','REVOKED','DISABLED')),
  revision integer NOT NULL DEFAULT 1 CHECK(revision >= 1),
  overlay_policy_version text NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE (id,season_id),
  FOREIGN KEY (season_id,primary_nation_id) REFERENCES nations(season_id,nation_id)
);
CREATE TABLE broadcast_output_permissions (
  output_id uuid NOT NULL REFERENCES broadcast_outputs(id),
  season_id uuid NOT NULL,
  nation_id uuid NOT NULL,
  PRIMARY KEY(output_id,season_id,nation_id),
  FOREIGN KEY (season_id,nation_id) REFERENCES nations(season_id,nation_id),
  FOREIGN KEY (output_id,season_id) REFERENCES broadcast_outputs(id,season_id)
);

CREATE TABLE broadcast_output_secrets (
  output_id uuid NOT NULL REFERENCES broadcast_outputs(id),
  secret_sha256 char(64) NOT NULL,
  issued_at timestamptz NOT NULL,
  revoked_at timestamptz,
  expires_at timestamptz,
  PRIMARY KEY(output_id,secret_sha256)
);
-- Read-only output token exchanges are rate-limited and scoped to outputId.

CREATE TABLE competition_clock_states (
  season_id uuid NOT NULL REFERENCES seasons(id),
  competition_event_id uuid NOT NULL,
  state text NOT NULL CHECK(state IN ('SCHEDULED','WAITING_FOR_ALL_LIVE','RUNNING','PAUSED','RESOLVED','CANCELLED')),
  elapsed_live_ms bigint NOT NULL DEFAULT 0 CHECK(elapsed_live_ms>=0),
  last_integrated_at timestamptz,
  ruleset_hash char(64) NOT NULL,
  version bigint NOT NULL DEFAULT 0,
  PRIMARY KEY (season_id,competition_event_id)
);
-- Aggregate global CompetitionLiveClock increments only if 3 LIVE_CONFIRMED.

CREATE TABLE season_global_sequences (
  season_id uuid PRIMARY KEY REFERENCES seasons(id),
  last_sequence bigint NOT NULL DEFAULT 0 CHECK (last_sequence >= 0)
);
-- Commit winner, wonder and presentation source within same serializable transaction.

CREATE TABLE presentation_cues (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  season_id uuid NOT NULL REFERENCES seasons(id),
  source_event_id uuid NOT NULL,
  source_global_sequence bigint NOT NULL,
  audience_scope text NOT NULL CHECK(audience_scope IN ('GLOBAL','NATION','OUTPUT')),
  nation_id uuid,
  output_id uuid REFERENCES broadcast_outputs(id),
  scene text NOT NULL,
  subtitle text,
  presentation_at timestamptz NOT NULL,
  expires_at timestamptz NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now(),
  FOREIGN KEY (season_id,nation_id) REFERENCES nations(season_id,nation_id),
  CHECK(expires_at > presentation_at),
  UNIQUE NULLS NOT DISTINCT (season_id,source_event_id,audience_scope,nation_id,output_id,scene)
);
-- NULLS NOT DISTINCT requires PostgreSQL 15+; reference uses PostgreSQL 16+.

CREATE TABLE era_mission_instances (
  season_id uuid NOT NULL,
  nation_id uuid NOT NULL,
  era_index smallint NOT NULL CHECK(era_index BETWEEN 1 AND 12),
  mission_catalog_id text NOT NULL,
  progress_json jsonb NOT NULL DEFAULT '{}'::jsonb,
  completed_at timestamptz,
  PRIMARY KEY(season_id,nation_id,era_index),
  FOREIGN KEY (season_id,nation_id) REFERENCES nations(season_id,nation_id)
);
-- Only 1 era mission per nation/era; must be completable via NPC. Does not
-- repeat daily/weekly rewards. Mission content catalog still to be authored.

COMMIT;

-- REQUIRED BEFORE PRODUCTION: state migration votes.OPEN↔PAUSED,
-- event clocks and global dedup, contribution ledger COSMETIC_SPEND,
-- generate contract DTO NationId UUID / FactionId string,
-- run true clean install, schema diff, concurrency and rollback tests.
