from fastapi import Request, Response
from starlette.middleware.base import (
    BaseHTTPMiddleware,
    RequestResponseEndpoint,
)
from termdo_tasks_api.app.configs.app_config import AppConfig
from termdo_tasks_api.app.constants.header_constants import HeaderConstants


class HeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ):
        response: Response = await call_next(request)

        # Add custom header with host name
        response.headers[HeaderConstants.HOST_NAME_KEY] = AppConfig.HOST_NAME
        return response
