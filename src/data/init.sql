CREATE TABLE IF NOT EXISTS Guilds (
    id              BIGINT NOT NULL PRIMARY KEY,
    owner_id        BIGINT NOT NULL,
    banned          BOOLEAN NOT NULL,
    perms           BIGINT NOT NULL DEFAULT 0,
    created_at      TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS GuildConfigs (
    id              BIGINT NOT NULL PRIMARY KEY REFERENCES Guilds (id) ON DELETE CASCADE,
    default_xp      INT NOT NULL DEFAULT 30,
    algo            INT NOT NULL DEFAULT 0,
    levelup_type    INT NOT NULL DEFAULT 0,
    levelup_msg     VARCHAR(1024) DEFAULT NULL,
    level_roles     BOOLEAN NOT NULL DEFAULT FALSE,
    created_at      TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS GuildOverrides (
    id              SERIAL PRIMARY KEY,
    guild_id        BIGINT NOT NULL REFERENCES Guilds (id) ON DELETE CASCADE,
    override_type   INT NOT NULL DEFAULT 0,
    override_data   TEXT NOT NULL,
    target_type     INT NOT NULL DEFAULT 0,
    target_id       BIGINT NOT NULL,
    created_at      TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS LevelRoles (
    guild_id        BIGINT NOT NULL REFERENCES Guilds (id) ON DELETE CASCADE,
    guild_level     INT NOT NULL,
    guild_role      BIGINT NOT NULL,
    created_at      TIMESTAMP NOT NULL DEFAULT NOW(),
    PRIMARY KEY (guild_id, guild_level)
);

CREATE TABLE IF NOT EXISTS Users (
    id              BIGINT NOT NULL PRIMARY KEY,
    banned          BOOLEAN NOT NULL,
    created_at      TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS GuildUsers (
    id              BIGINT NOT NULL REFERENCES Users (id) ON DELETE CASCADE,
    guild_id        BIGINT NOT NULL REFERENCES Guilds (id) ON DELETE CASCADE,
    xp              BIGINT NOT NULL DEFAULT 0,
    created_at      TIMESTAMP NOT NULL DEFAULT NOW()
);