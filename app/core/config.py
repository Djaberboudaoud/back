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
    # DATABASE_URL: str = "postgresql://postgres.gcybsjcakekkyvuilcgl:192837465ReportingSystem@aws-1-eu-north-1.pooler.supabase.com:5432/postgres"
    DATABASE_URL : str="postgresql+psycopg2://postgres.gcybsjcakekkyvuilcgl:192837465ReportingSystem@aws-1-eu-north-1.pooler.supabase.com:6543/postgres"
    # JWT Authentication
    JWT_SECRET_KEY: str = "super-secret-key-change-in-production"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()