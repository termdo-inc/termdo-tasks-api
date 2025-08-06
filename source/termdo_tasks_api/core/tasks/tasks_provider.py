from asyncpg import DataError
from asyncpg.pool import PoolConnectionProxy
from termdo_tasks_api.app.constants.db_constants import DbConstants
from termdo_tasks_api.common.models.task_model import TaskModel
from termdo_tasks_api.common.queries.task_queries import TaskQueries
from termdo_tasks_api.modules.db.module import DbModule


class TasksProvider:
    @classmethod
    async def get_tasks(cls, account_id: int) -> list[TaskModel]:
        client: PoolConnectionProxy | None = None
        try:
            client = await DbModule.get().get_client()
            await client.execute(DbConstants.BEGIN)
            result = await client.fetch(
                TaskQueries.GET_TASKS_1AID.value, account_id
            )
            tasks = TaskModel.from_records(result)
            await client.execute(DbConstants.COMMIT)
            return tasks
        except Exception as e:
            if client:
                await client.execute(DbConstants.ROLLBACK)
            raise e
        finally:
            if client:
                await DbModule.get().release_client(client)

    @classmethod
    async def get_task(cls, account_id: int, task_id: int) -> TaskModel | None:
        client: PoolConnectionProxy | None = None
        try:
            client = await DbModule.get().get_client()
            await client.execute(DbConstants.BEGIN)
            result = await client.fetchrow(
                TaskQueries.GET_TASK_1AID_2TID.value, account_id, task_id
            )
            if result is None:
                return None
            task = TaskModel.from_record(result)
            await client.execute(DbConstants.COMMIT)
            return task
        except Exception as e:
            if client:
                await client.execute(DbConstants.ROLLBACK)
            raise e
        finally:
            if client:
                await DbModule.get().release_client(client)

    @classmethod
    async def insert_task(
        cls, account_id: int, title: str, description: str
    ) -> TaskModel:
        client: PoolConnectionProxy | None = None
        try:
            client = await DbModule.get().get_client()
            await client.execute(DbConstants.BEGIN)
            result = await client.fetchrow(
                TaskQueries.INSERT_TASK_RT_1AID_2TITLE_3DESC.value,
                account_id,
                title,
                description,
            )
            if result is None:
                raise DataError("Failed to insert task")
            task = TaskModel.from_record(result)
            await client.execute(DbConstants.COMMIT)
            return task
        except Exception as e:
            if client:
                await client.execute(DbConstants.ROLLBACK)
            raise e
        finally:
            if client:
                await DbModule.get().release_client(client)

    @classmethod
    async def update_task(
        cls,
        account_id: int,
        task_id: int,
        title: str,
        description: str,
        is_completed: bool,
    ) -> TaskModel:
        client: PoolConnectionProxy | None = None
        try:
            client = await DbModule.get().get_client()
            await client.execute(DbConstants.BEGIN)
            result = await client.fetchrow(
                TaskQueries.UPDATE_TASK_RT_1AID_2TID_3TITLE_4DESC_5ISCMP.value,
                account_id,
                task_id,
                title,
                description,
                is_completed,
            )
            if result is None:
                raise DataError("Failed to update task")
            updated_task = TaskModel.from_record(result)
            await client.execute(DbConstants.COMMIT)
            return updated_task
        except Exception as e:
            if client:
                await client.execute(DbConstants.ROLLBACK)
            raise e
        finally:
            if client:
                await DbModule.get().release_client(client)

    @classmethod
    async def delete_task(cls, account_id: int, task_id: int) -> None:
        client: PoolConnectionProxy | None = None
        try:
            client = await DbModule.get().get_client()
            await client.execute(DbConstants.BEGIN)
            await client.execute(
                TaskQueries.DELETE_TASK_1AID_2TID.value, account_id, task_id
            )
            await client.execute(DbConstants.COMMIT)
        except Exception as e:
            if client:
                await client.execute(DbConstants.ROLLBACK)
            raise e
        finally:
            if client:
                await DbModule.get().release_client(client)
