from datetime import datetime

from pydantic import BaseModel
from termdo_tasks_api.common.models.task_model import TaskModel


class TasksResponse(BaseModel):
    task_id: int
    title: str
    description: str
    is_completed: bool
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def from_model(model: TaskModel) -> "TasksResponse":
        return TasksResponse(
            task_id=model.task_id,
            title=model.title,
            description=model.description,
            is_completed=model.is_completed,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )

    @staticmethod
    def from_models(models: list[TaskModel]) -> list["TasksResponse"]:
        return [TasksResponse.from_model(model) for model in models]
