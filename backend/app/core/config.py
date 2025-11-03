from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # API Settings
    PROJECT_NAME: str = "AI Career Companion"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Security
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Database
    DATABASE_URL: str
    REDIS_URL: str
    
    # External Services
    OPENAI_API_KEY: str
    LINKEDIN_CLIENT_ID: str
    LINKEDIN_CLIENT_SECRET: str
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()