from dotenv import load_dotenv
from fastapi import FastAPI

# Environment
load_dotenv()

# Application
app = FastAPI()


@app.get("/tasks")
async def get_tasks():
    return {"message": "List of tasks"}
