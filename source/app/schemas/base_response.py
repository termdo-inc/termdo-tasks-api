from pydantic import BaseModel

from app.configs.app_config import AppConfig


class BaseResponse(BaseModel):
    host: str = AppConfig.HOST
