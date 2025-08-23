from pydantic import BaseModel, ConfigDict, Field


class TasksRequest(BaseModel):
    model_config = ConfigDict(
        validate_by_name=True,
        validate_by_alias=True,
        json_schema_extra={
            "example": {
                "title": "Study Python",
                "description": "Complete the FastAPI course",
                "isCompleted": False,
            }
        },
    )

    title: str = Field(alias="title", min_length=1, max_length=64)
    description: str = Field(alias="description", min_length=0, max_length=1024)
    is_completed: bool = Field(alias="isCompleted")
