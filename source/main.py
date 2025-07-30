from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI
from modules.db.module import DbModule

# Application
app = FastAPI()


@asynccontextmanager
async def lifespan(_: FastAPI):
    load_dotenv()
    await DbModule.instance().handler.create_pool()
    yield
    await DbModule.instance().handler.close_pool()
