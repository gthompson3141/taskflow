from fastapi import FastAPI

from app.core.config import settings
from app.db.base import create_db_and_tables

app = FastAPI(title=settings.app_name)


@app.get("/")
def root():
    return {"message", "Taskflow is running"}


@app.get("/health")
def health_check():
    return {"status", "healthy"}


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
