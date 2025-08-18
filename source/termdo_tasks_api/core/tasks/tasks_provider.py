from asyncpg import DataError
from termdo_tasks_api.common.models.task_model import TaskModel
from termdo_tasks_api.common.queries import task_queries
from termdo_tasks_api.modules.db.module import DbModule


class TasksProvider:
    @classmethod
    async def get_tasks(cls, account_id: int) -> list[TaskModel]:
        async with DbModule.get().get_connection() as conn:
            async with conn.transaction():
                result = await conn.fetch(
                    task_queries.GET_TASKS_1AID, account_id
                )
                return TaskModel.from_records(result)

    @classmethod
    async def get_task(cls, account_id: int, task_id: int) -> TaskModel | None:
        async with DbModule.get().get_connection() as conn:
            async with conn.transaction():
                result = await conn.fetchrow(
                    task_queries.GET_TASK_1AID_2TID, account_id, task_id
                )
                if result is None:
                    return None
                return TaskModel.from_record(result)

    @classmethod
    async def insert_task(
        cls, account_id: int, title: str, description: str
    ) -> TaskModel:
        async with DbModule.get().get_connection() as conn:
            async with conn.transaction():
                result = await conn.fetchrow(
                    task_queries.INSERT_TASK_RT_1AID_2TITLE_3DESC,
                    account_id,
                    title,
                    description,
                )
                if result is None:
                    raise DataError("Failed to insert task")
                return TaskModel.from_record(result)

    @classmethod
    async def update_task(
        cls,
        account_id: int,
        task_id: int,
        title: str,
        description: str,
        is_completed: bool,
    ) -> TaskModel:
        async with DbModule.get().get_connection() as conn:
            async with conn.transaction():
                result = await conn.fetchrow(
                    task_queries.UPDATE_TASK_RT_1AID_2TID_3TITLE_4DESC_5ISCMP,
                    account_id,
                    task_id,
                    title,
                    description,
                    is_completed,
                )
                if result is None:
                    raise DataError("Failed to update task")
                return TaskModel.from_record(result)

    @classmethod
    async def delete_task(cls, account_id: int, task_id: int) -> None:
        async with DbModule.get().get_connection() as conn:
            async with conn.transaction():
                await conn.execute(
                    task_queries.DELETE_TASK_1AID_2TID, account_id, task_id
                )
