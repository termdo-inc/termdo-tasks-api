from typing import Generic, TypeVar

from pydantic import BaseModel, ConfigDict, Field

T = TypeVar("T")


class AppResponse(BaseModel, Generic[T]):
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    data: T = Field(alias="data")
