from pydantic import BaseModel, Field


class TasksRequest(BaseModel):
    title: str = Field(min_length=1, max_length=64)
    description: str = Field(min_length=0, max_length=1024)
    is_completed: bool = Field(default=False, description="Not required when creating")

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Study Python",
                "description": "Complete the FastAPI course",
                "is_completed": False,
            }
        }
    }
