from fastapi import HTTPException
from starlette import status
from termdo_tasks_api.core.tasks.schemas.tasks_request import TasksRequest
from termdo_tasks_api.core.tasks.schemas.tasks_response import TasksResponse
from termdo_tasks_api.core.tasks.tasks_provider import TasksProvider


class TasksManager:
    _provider = TasksProvider()

    @classmethod
    async def get_tasks(cls, account_id: int) -> list[TasksResponse]:
        tasks = await cls._provider.get_tasks(account_id)
        return TasksResponse.from_models(tasks)

    @classmethod
    async def post_task(
        cls, account_id: int, task: TasksRequest
    ) -> TasksResponse:
        task_model = await cls._provider.insert_task(
            account_id, task.title, task.description
        )
        return TasksResponse.from_model(task_model)

    @classmethod
    async def get_task(cls, account_id: int, task_id: int) -> TasksResponse:
        task = await cls._provider.get_task(account_id, task_id)
        if task is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
            )
        return TasksResponse.from_model(task)

    @classmethod
    async def put_task(
        cls, account_id: int, task_id: int, req_task: TasksRequest
    ) -> TasksResponse:
        task = await cls._provider.get_task(account_id, task_id)
        if task is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
            )
        updated_task = await cls._provider.update_task(
            account_id,
            task_id,
            req_task.title,
            req_task.description,
            req_task.is_completed,
        )
        return TasksResponse.from_model(updated_task)

    @classmethod
    async def delete_task(cls, account_id: int, task_id: int) -> None:
        task = await cls._provider.get_task(account_id, task_id)
        if task is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
            )
        await cls._provider.delete_task(task.account_id, task.task_id)
