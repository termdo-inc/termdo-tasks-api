from pydantic import BaseModel
from termdo_tasks_api.app.utils.string_utils import to_camel_case


class BaseResponse(BaseModel):
    model_config = {
        "alias_generator": to_camel_case,
    }
