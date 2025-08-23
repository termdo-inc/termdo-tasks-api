from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field
from termdo_tasks_api.common.models.task_model import TaskModel


class TasksResponse(BaseModel):
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    task_id: int = Field(alias="taskId")
    title: str = Field(alias="title")
    description: str = Field(alias="description")
    is_completed: bool = Field(alias="isCompleted")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")

    @staticmethod
    def from_model(model: TaskModel) -> "TasksResponse":
        return TasksResponse(
            taskId=model.task_id,
            title=model.title,
            description=model.description,
            isCompleted=model.is_completed,
            createdAt=model.created_at,
            updatedAt=model.updated_at,
        )

    @staticmethod
    def from_models(models: list[TaskModel]) -> list["TasksResponse"]:
        return [TasksResponse.from_model(model) for model in models]
