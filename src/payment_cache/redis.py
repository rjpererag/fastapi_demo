import redis.asyncio as redis
from .settings import Settings as RedisSettings


class RedisService:
    def __init__(self, settings: RedisSettings):
        self.connection = redis.from_url(url=settings.URL, decode_responses=True)

    async def check_rate_limit(
        self, identifier: str, limit: int, window: int = 60
    ) -> bool:
        key = f"rate_limit:{identifier}"
        async with self.connection.pipeline(transaction=True) as pipe:
            await pipe.incr(key)
            await pipe.expire(key, window)
            results = await pipe.execute()

        current_requests = results[0]
        return current_requests <= limit


redis_service = RedisService(settings=RedisSettings())
