import asyncpg


class PostgresFacade(object):
    def __init__(self, config):
        self.config = config
        self.pool = None

    async def connect(self) -> None:
        if not self.pool:
            self.pool = await asyncpg.create_pool(dsn=self.config.DATABASE_DSN)

    async def disconnect(self) -> None:
        await self.pool.close()
