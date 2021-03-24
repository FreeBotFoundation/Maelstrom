from discord import Embed
from discord.ext import commands

from loguru import logger
from datetime import datetime

from src.internal.bot import Bot
from src.internal.context import Context
from src.utils.validator import ConfigValidator
from src.data.values import ALGOS_REVERSE, LEVELUP_TYPES_REVERSE, LEVELUP_TYPES, MESSAGE_CHAT, MESSAGE_DM


class Config(commands.Cog):
    """Config commands for Maelstrom."""

    def __init__(self, bot: Bot):
        self.bot = bot

    async def confirm(self, ctx: Context, title: str, content: str):
        await ctx.send(
            embed=Embed(
                title=title,
                description=content,
                colour=0x87CEEB,
                timestamp=ctx.message.created_at,
            )
        )

    @commands.group(name="config", aliases=["cfg"], invoke_without_command=True)
    @commands.check_any(commands.is_owner(), commands.has_guild_permissions(manage_guild=True))
    @commands.guild_only()
    async def config(self, ctx: Context):
        """Config commands for Maelstrom."""

        await ctx.send_help("config")

    @config.group(name="set", invoke_without_command=True)
    async def config_set(self, ctx: Context):
        """Set config values."""

        await ctx.send_help("config set")

    @config.group(name="get", invoke_without_command=True)
    async def config_get(self, ctx: Context):
        """Get config values."""

        await ctx.send_help("config get")

    ## Default XP

    @config_set.command(name="default", aliases=["defaultxp"])
    async def set_default(self, ctx: Context, value: int = 30):
        """Set the default XP gain per message. Defaults to 30."""

        result = ConfigValidator.validate_default_xp(value)

        if result.valid:
            await self.bot.db.update_default_xp(ctx.guild, result.value)
            return await self.confirm(ctx, "Success!", f"The default XP gain for this server has been set to: {result.value}")

        await self.confirm(ctx, "Something went wrong!", result.reason)

    @config_get.command(name="default", aliases=["defaultxp"])
    async def get_default(self, ctx: Context):
        """Get the default XP gain per message."""

        cfg = await ctx.fetch_guild_config()

        return await self.confirm(ctx, "Config: default xp gain", f"The default XP gain in this server is: {cfg['default_xp']}")

    ## Algorithm

    @config_set.command(name="algo", aliases=["algorithm"])
    async def set_algo(self, ctx: Context, value: str = "linear"):
        """Set the levelling algorithm. Defaults to linear."""

        result = ConfigValidator.validate_algorithm(value)

        if result.valid:
            await self.bot.db.update_algo(ctx.guild, result.value)
            return await self.confirm(ctx, "Success!", f"The levelling algorithm for this server has been set to: {value.lower()}")

        await self.confirm(ctx, "Something went wrong!", result.reason)

    @config_get.command(name="algo", aliases=["algorithm"])
    async def get_algo(self, ctx: Context):
        """Get the levelling algorithm."""

        cfg = await ctx.fetch_guild_config()

        return await self.confirm(ctx, "Config: levelling algorithm", f"The levelling algorithm in this server is: {ALGOS_REVERSE[cfg['algo']]}")

    ## Levelup Type

    @config_set.command(name="levelup", aliases=["lu"])
    async def set_levelup(self, ctx: Context, value: str = "react"):
        """Set the action to perform on level ups."""

        result = ConfigValidator.validate_levelup_type(value)

        if result.valid:
            await self.bot.db.update_levelup_type(ctx.guild, result.value)
            return await self.confirm(ctx, "Success!", f"The level up action for this server has been set to: {value.lower()}")

        await self.confirm(ctx, "Something went wrong!", result.reason)

    @config_get.command(name="levelup", aliases=["lu"])
    async def get_levelup(self, ctx: Context):
        """Get the action performed on level ups."""

        cfg = await ctx.fetch_guild_config()

        return await self.confirm(ctx, "Config: level up action", f"The level up action in this server is: {LEVELUP_TYPES_REVERSE[cfg['levelup_type']]}")

    ## Levelup Message

    @config_set.command(name="message", aliases=["msg"])
    async def set_msg(self, ctx: Context, *, msg: str = None):
        """Set the message sent on level ups."""

        cfg = await ctx.fetch_guild_config()

        if cfg["levelup_type"] not in [LEVELUP_TYPES["chat"], LEVELUP_TYPES["dm"]]:
            return await self.confirm(ctx, "Something went wrong!", "To set a level up message your level up action must either be dm or chat.")

        if not msg:
            if cfg["levelup_type"] == LEVELUP_TYPES["chat"]:
                msg = MESSAGE_CHAT
            else:
                msg = MESSAGE_DM

        result = ConfigValidator.validate_levelup_message(msg)

        if result.valid:
            await self.bot.db.update_levelup_msg(ctx.guild, result.value)
            return await self.confirm(ctx, "Success!", f"The level up message for this server has been changed.")

        await self.confirm(ctx, "Something went wrong!", result.reason)

    @config_get.command(name="message", aliases=["msg"])
    async def get_msg(self, ctx: Context):
        """Get the message sent on level ups."""

        cfg = await ctx.fetch_guild_config()

        if cfg["levelup_type"] not in [LEVELUP_TYPES["chat"], LEVELUP_TYPES["dm"]]:
            return await self.confirm(ctx, "Config: level up message", "To have a level up message your level up action must either be dm or chat.")

        msg = cfg["levelup_msg"]

        if not msg:
            if cfg["levelup_type"] == LEVELUP_TYPES["chat"]:
                msg = MESSAGE_CHAT
            else:
                msg = MESSAGE_DM

        await self.confirm(ctx, "Config: level up message", msg)

    ## Level Roles

    @config_set.command(name="level_roles", aliases=["roles"])
    async def set_level_roles(self, ctx: Context, value: str):
        """Enebale or disable level roles."""

        result = ConfigValidator.validate_level_role(value)

        if result.valid:
            await self.bot.db.update_level_roles(ctx.guild, result.value)
            return await self.confirm(ctx, "Success!", f"Level roles on this server have been turned {value.lower()}.")

        await self.confirm(ctx, "Something went wrong!", result.reason)

    @config_get.command(name="level_roles", aliases=["roles"])
    async def get_levelup(self, ctx: Context):
        """See the level roles status."""

        cfg = await ctx.fetch_guild_config()

        status = "on" if cfg["level_roles"] else "off"

        return await self.confirm(ctx, "Config: level roles", f"Level roles on this server are {status}.")


def setup(bot: Bot):
    bot.add_cog(Config(bot))
