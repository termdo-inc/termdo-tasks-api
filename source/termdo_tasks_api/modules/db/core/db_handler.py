from asyncpg.pool import Pool, PoolConnectionProxy, create_pool
from termdo_tasks_api.app.configs.db_config import DbConfig


class DbHandler:
    def __init__(self):
        self._db_pool: Pool | None = None

    async def create_pool(self) -> None:
        if self._db_pool is None:
            self._db_pool = await create_pool(
                host=DbConfig.HOST,
                port=DbConfig.PORT,
                user=DbConfig.USER,
                password=DbConfig.PASSWORD,
                database=DbConfig.NAME,
            )

    async def get_client(self) -> PoolConnectionProxy:
        if self._db_pool is None:
            raise RuntimeError(
                "Database pool is not created. Call create_pool() first!"
            )
        return await self._db_pool.acquire()

    async def release_client(self, client: PoolConnectionProxy) -> None:
        if self._db_pool is None:
            raise RuntimeError(
                "Database pool is not created. Call create_pool() first!"
            )
        await self._db_pool.release(client)

    async def close_pool(self) -> None:
        if self._db_pool:
            await self._db_pool.close()
            self._db_pool = None
        else:
            raise RuntimeError("Pool can't be closed!")
