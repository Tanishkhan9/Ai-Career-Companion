from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    # API Settings
    PROJECT_NAME: str = "AI Career Companion"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    # Security
    # Provide a safe default for local/dev/tests; override via env in production
    SECRET_KEY: str = "dev-secret-key-change-me"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Database
    # Default to a local SQLite DB to allow tests to run out of the box
    DATABASE_URL: str = "sqlite:///./test.db"
    REDIS_URL: str = "redis://localhost:6379/0"

    # External Services (dummy defaults for tests/dev)
    OPENAI_API_KEY: str = "test-openai-key"
    LINKEDIN_CLIENT_ID: str = "test-linkedin-client-id"
    LINKEDIN_CLIENT_SECRET: str = "test-linkedin-client-secret"

    # Feature flags
    REQUIRE_EMAIL_VERIFICATION: bool = False

    model_config = SettingsConfigDict(env_file=".env")

@lru_cache()
def get_settings():
    return Settings()