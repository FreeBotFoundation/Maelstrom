# FreeBotFoundation: Maelstrom

## Maelstrom is a Discord levelling bot, built to rival MEE6 levelling

## Database Object Reference

### Guilds:

| Name     | Type    | Description                                              |
|----------|---------|----------------------------------------------------------|
| id       | bigint  | The Discord ID of the guild.                             |
| owner_id | bigint  | The Discord ID of the guild owner.                       |
| banned   | boolean | Whether the guild is banned.                             |
| perms    | bigint  | A bitfield representing the guild's special permissions. |

---

### GuildConfigs:

| Name         | Type         | Description                                                                    |
|--------------|--------------|--------------------------------------------------------------------------------|
| id           | bigint       | The Discord ID of the guild whose config it is.                                |
| default_xp   | int          | The default XP gain on the guild.                                              |
| algo         | int          | The algorithm to use for calculating levels. See `Algorithm`'s type reference. |
| levelup_type | int          | The action to perform on level ups. See `LevelUp`'s type reference.            |
| levelup_msg  | string[1024] | The message to send in chat, or DM, depending on `levelup_type`.               |
| level_roles  | boolean      | Whether to enable level roles on the guild.                                    |

---

### GuildOverrides

| Name          | Type       | Description                                                               |
|---------------|------------|---------------------------------------------------------------------------|
| id            | serial:int | The automatically generated ID for the override.                          |
| guild_id      | bigint     | The ID of the guild the override belongs to.                              |
| override_type | int        | The type of the override. See `OverridesType`'s type reference.'          |
| override_data | string     | The dumped JSON data of the override's data.                              |
| target_type   | int        | The type of the override's target. See `OverrideTarget`'s type reference. |
| target_id     | bigint     | The Discord ID of the target of the override.                             |

---

### LevelRoles

| Name        | Type   | Description                                                |
|-------------|--------|------------------------------------------------------------|
| guild_id    | bigint | The ID of the guild the level role belongs to.             |
| guild_level | int    | The level the role belongs to.                             |
| guild_role  | bigint | The ID of the role in the guild the level role belongs to. |

---

### Users

| Name   | Type    | Description                 |
|--------|---------|-----------------------------|
| id     | bigint  | The Discord ID of the user. |
| banned | boolean | Whether the user is banned. |

---

### GuildUsers

| Name     | Type   | Description                          |
|----------|--------|--------------------------------------|
| id       | bigint | The Discord ID of the user.          |
| guild_id | bigint | The Discord ID of the guild.         |
| xp       | bigint | The amount of XP the guild user has. |

---

## Type Reference

### Algorithm

| Value | Detail               | Default |
|-------|----------------------|---------|
| 0     | Linear levelling.    | yes     |
| 1     | Quadratic levelling. | no      |

---

### LevelUp

| Value | Detail            | Default |
|-------|-------------------|---------|
| 0     | React to message. | yes     |
| 1     | Message in chat.  | no      |
| 2     | Message in DMs.   | no      |

---

### OverrideType

| Value | Detail                | Default |
|-------|-----------------------|---------|
| 0     | XP modifier override. | yes     |
| 1     | Permission override.  | no      |


---

### TargetType

| Value | Detail   | Default |
|-------|----------|---------|
| 0     | Member.  | yes     |
| 1     | Role.    | no      |
| 1     | Channel. | no      |