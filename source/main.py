from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from source.app.configs.app_config import AppConfig
from source.core.tasks.tasks_builder import tasks_router
from source.modules.db.module import DbModule


@asynccontextmanager
async def lifespan(_: FastAPI):
    # Initialize
    await DbModule.instance().create_pool()

    # App runs
    yield

    # Cleanup
    await DbModule.instance().close_pool()


# Application
app = FastAPI(lifespan=lifespan)


# Routers
app.include_router(tasks_router)


def main():
    uvicorn.run("source.main:app", port=AppConfig.PORT)
