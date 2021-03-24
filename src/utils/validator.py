from collections import namedtuple

from src.data.values import ALGOS, LEVELUP_TYPES


Result = namedtuple('Result', ["value", "valid", "reason"])


class ConfigValidator:
    @staticmethod
    def validate_default_xp(xp: int) -> Result:
        if 10 <= xp <= 1000:
            return Result(xp, True, None)
        return Result(None, False, "Value for default XP gain must be between 10 and 1,000.")

    @staticmethod
    def validate_algorithm(algo: str) -> Result:
        if algo in ALGOS:
            return Result(ALGOS[algo], True, None)
        return Result(None, False, f"Value for algorithm must be one of: {', '.join(list(ALGOS.keys()))}")

    @staticmethod
    def validate_levelup_type(type: str) -> Result:
        if type in LEVELUP_TYPES:
            return Result(LEVELUP_TYPES[type], True, None)
        return Result(None, False, f"Value for levelup type must be one of {', '.join(list(LEVELUP_TYPES.keys()))}")

    @staticmethod
    def validate_levelup_message(msg: str) -> Result:
        if 0 < len(msg) <= 1024:
            return Result(msg, True, None)
        return Result(None, False, "Value for level up message must be between 1 and 1024 characters.")

    @staticmethod
    def validate_level_role(value: str) -> Result:
        if value in ["on", "off"]:
            return Result(True if value == "on" else False, True, None)
        return Result(None, False, "Value for level role setting must be on or off.")