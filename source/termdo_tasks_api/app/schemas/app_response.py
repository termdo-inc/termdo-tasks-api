from typing import Generic, TypeVar

from pydantic import BaseModel
from termdo_tasks_api.app.utils.string_utils import to_camel_case

T = TypeVar("T")


class AppResponse(BaseModel, Generic[T]):
    data: T

    model_config = {
        "alias_generator": to_camel_case,
    }
