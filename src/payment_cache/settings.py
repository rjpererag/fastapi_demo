from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    URL: str = "redis://localhost:6379/0"
    RATE_LIMIT_PER_MINUTE: int = 60

    model_config = {"env_file": ".env", "extra": "ignore"}
