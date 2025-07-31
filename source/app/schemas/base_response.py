from pydantic import BaseModel

from source.app.configs.app_config import AppConfig


class BaseResponse(BaseModel):
    host: str = AppConfig.HOST
