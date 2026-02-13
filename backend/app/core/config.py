from fastapi import FastAPI
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Taskflow API"
    debug: bool = False

    database_url: str = "postgresql://taskflow:taskflow@localhost:5432/taskflow"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
