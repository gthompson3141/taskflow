from fastapi import FastAPI

from app.core.config import settings
from app.db.base import create_db_and_tables
from app.models.user import User
from app.api.v1 import auth, tasks
from app.models.task import Task

app = FastAPI(title=settings.app_name)
app.include_router(auth.router, prefix="/api/v1")
app.include_router(tasks.router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message", "Taskflow is running"}


@app.get("/health")
def health_check():
    return {"status", "healthy"}


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
