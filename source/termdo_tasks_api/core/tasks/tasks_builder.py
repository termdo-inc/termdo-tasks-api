from typing import Annotated

from fastapi import APIRouter, Body, Path
from starlette import status
from termdo_tasks_api.app.schemas.app_response import AppResponse
from termdo_tasks_api.core.tasks.schemas.tasks_request import TasksRequest
from termdo_tasks_api.core.tasks.schemas.tasks_response import TasksResponse
from termdo_tasks_api.core.tasks.tasks_manager import TasksManager

tasks_router = APIRouter()
_manager = TasksManager()


@tasks_router.get("/{account_id}/", status_code=status.HTTP_200_OK)
async def get_tasks(
    account_id: Annotated[int, Path(gt=0)],
) -> AppResponse[list[TasksResponse]]:
    return AppResponse[list[TasksResponse]](
        data=await _manager.get_tasks(account_id)
    )


@tasks_router.post("/{account_id}/", status_code=status.HTTP_201_CREATED)
async def post_task(
    account_id: Annotated[int, Path(gt=0)],
    task: TasksRequest = Body(),
) -> AppResponse[TasksResponse]:
    return AppResponse[TasksResponse](
        data=await _manager.post_task(account_id, task)
    )


@tasks_router.get("/{account_id}/{task_id}/", status_code=status.HTTP_200_OK)
async def get_task(
    account_id: Annotated[int, Path(gt=0)],
    task_id: Annotated[int, Path(gt=0)],
) -> AppResponse[TasksResponse]:
    return AppResponse[TasksResponse](
        data=await _manager.get_task(account_id, task_id)
    )


@tasks_router.put("/{account_id}/{task_id}/", status_code=status.HTTP_200_OK)
async def put_task(
    account_id: Annotated[int, Path(gt=0)],
    task_id: Annotated[int, Path(gt=0)],
    task: TasksRequest = Body(),
) -> AppResponse[TasksResponse]:
    return AppResponse[TasksResponse](
        data=await _manager.put_task(account_id, task_id, task)
    )


@tasks_router.delete("/{account_id}/{task_id}/", status_code=status.HTTP_200_OK)
async def delete_task(
    account_id: Annotated[int, Path(gt=0)],
    task_id: Annotated[int, Path(gt=0)],
) -> AppResponse[None]:
    await _manager.delete_task(account_id, task_id)
    return AppResponse[None](data=None)
