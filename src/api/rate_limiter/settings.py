from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    URL: str = "redis://localhost:6379/0"
    RATE_LIMIT_PER_MINUTE: int = 60

    model_config = SettingsConfigDict(
        env_file=".env", extra="ignore", env_prefix="REDIS_"
    )
