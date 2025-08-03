import sys
from contextlib import asynccontextmanager

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from termdo_tasks_api.app.configs.app_config import AppConfig
from termdo_tasks_api.app.configs.db_config import DbConfig
from termdo_tasks_api.core.tasks.tasks_builder import tasks_router
from termdo_tasks_api.modules.db.module import DbModule


@asynccontextmanager
async def lifespan(_: FastAPI):
    # Initialize
    await DbModule.get().create_pool()

    # App runs
    yield

    # Cleanup
    await DbModule.get().close_pool()


# Application
app = FastAPI(lifespan=lifespan)


# Routers
app.include_router(tasks_router)


def main():
    if "--dev" in sys.argv:
        load_dotenv()

    AppConfig.load()
    DbConfig.load()

    uvicorn.run("termdo_tasks_api.main:app", port=AppConfig.PORT)


if __name__ == "__main__":
    main()
