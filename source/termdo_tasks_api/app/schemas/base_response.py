from pydantic import BaseModel
from termdo_tasks_api.app.configs.app_config import AppConfig


class BaseResponse(BaseModel):
    host: str = AppConfig.HOST
