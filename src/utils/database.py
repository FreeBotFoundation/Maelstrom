from asyncpg import create_pool
from os import getenv

from loguru import logger

from discord import Guild


class Database:
    """A database interface for the bot to connect to Postgres."""

    def __init__(self):
        self.guilds = {}

    async def setup(self):
        logger.info("Setting up database...")
        self.pool = await create_pool(
            host=getenv("DB_HOST", "127.0.0.1"),
            port=getenv("DB_PORT", 5432),
            database=getenv("DB_DATABASE"),
            user=getenv("DB_USER", "root"),
            password=getenv("DB_PASS", "password"),
        )
        logger.info("Database setup complete.")

    async def execute(self, query: str, *args):
        async with self.pool.acquire() as conn:
            await conn.execute(query, *args)

    async def fetchrow(self, query: str, *args):
        async with self.pool.acquire() as conn:
            return await conn.fetchrow(query, *args)

    async def fetch(self, query: str, *args):
        async with self.pool.acquire() as conn:
            return await conn.fetch(query, *args)

    async def create_guild(self, id: int, owner_id: int, banned: bool = False) -> bool:
        return await self.fetchrow("INSERT INTO Guilds (id, owner_id, banned) VALUES ($1, $2, $3) RETURNING *;", id, owner_id, banned)

    async def fetch_guild(self, guild: Guild):
        data = await self.fetchrow("SELECT * FROM Guilds WHERE id = $1;", guild.id)

        if not data:
            return await self.create_guild(guild.id, guild.owner.id)
        return data
