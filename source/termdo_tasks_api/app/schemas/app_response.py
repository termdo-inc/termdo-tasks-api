from typing import Generic, TypeVar

from pydantic import BaseModel
from termdo_tasks_api.app.utils.string_utils import snake_to_camel_case

T = TypeVar("T")


class AppResponse(BaseModel, Generic[T]):
    data: T

    model_config = {
        "alias_generator": snake_to_camel_case,
    }
