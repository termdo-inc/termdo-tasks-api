from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn
from modules.db.module import DbModule
from app.configs.app_config import AppConfig
from core.tasks.tasks_builder import tasks_router


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


if __name__ == "__main__":
    uvicorn.run("main:app", port=AppConfig.PORT, env_file=".env")
