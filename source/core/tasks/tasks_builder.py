from core.tasks.schemas.tasks_request import TasksRequest
from core.tasks.schemas.tasks_response import TasksResponse
from core.tasks.tasks_manager import TasksManager
from fastapi import APIRouter, Body, Path
from starlette import status

tasks_router = APIRouter()
_manager = TasksManager()


@tasks_router.get("/accounts/{account_id}/tasks", status_code=status.HTTP_200_OK)
async def get_tasks(
    account_id: int = Path(gt=0),
) -> list[TasksResponse]:
    return await _manager.get_tasks(account_id)


@tasks_router.post("/accounts/{account_id}/tasks", status_code=status.HTTP_201_CREATED)
async def post_task(
    account_id: int = Path(gt=0),
    task: TasksRequest = Body(),
) -> TasksResponse:
    return await _manager.post_task(account_id, task)


@tasks_router.get("/accounts/{account_id}/tasks/{task_id}", status_code=status.HTTP_200_OK)
async def get_task(
    account_id: int = Path(gt=0),
    task_id: int = Path(gt=0),
) -> TasksResponse:
    return await _manager.get_task(account_id, task_id)


@tasks_router.put("/accounts/{account_id}/tasks/{task_id}", status_code=status.HTTP_200_OK)
async def put_task(
    account_id: int = Path(gt=0),
    task_id: int = Path(gt=0),
    task: TasksRequest = Body(),
) -> TasksResponse:
    return await _manager.put_task(account_id, task_id, task)


@tasks_router.delete("/accounts/{account_id}/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    account_id: int = Path(gt=0),
    task_id: int = Path(gt=0),
) -> None:
    await _manager.delete_task(account_id, task_id)
    return None
