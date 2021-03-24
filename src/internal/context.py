from discord.ext.commands import Context as _BaseContext


class Context(_BaseContext):
    """A Custom Context for extra functionality."""

    async def fetch_guild(self):
        return await self.bot.db.fetch_guild(self.guild)
