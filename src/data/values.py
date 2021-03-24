def rd(d: dict): return {v: k for k, v in d.items()}

ALGOS = {
    "linear": 0,
    "quadratic": 1,
}

ALGOS_REVERSE = rd(ALGOS)

LEVELUP_TYPES = {
    "react": 0,
    "chat": 1,
    "dm": 2,
}

LEVELUP_TYPES_REVERSE = rd(LEVELUP_TYPES)

MESSAGE_DM = "You levelled up on {guild} to level {level}!"
MESSAGE_CHAT = "You levelled up to level {level}!"
