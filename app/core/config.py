import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    # API
    PROJECT_NAME: str = "reporting-system"
    PROJECT_VERSION: str = "1.0.0"
    API_PREFIX: str = "/api"

    # Server
    HOST: str = "127.0.0.1"
    PORT: int = 8001
    DEBUG: bool = False

    # Database
    DATABASE_URL: str = "postgresql+psycopg2://postgres:192837465@localhost:5432/reporting-system"

    # JWT Authentication
    JWT_SECRET_KEY: str = "super-secret-key-change-in-production"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()