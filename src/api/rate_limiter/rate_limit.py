from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware


from .redis import redis_service


class RateLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host

        is_allowed = await redis_service.check_rate_limit(
            identifier=client_ip, limit=redis_service.settings.RATE_LIMIT_PER_MINUTE
        )

        if not is_allowed:
            raise HTTPException(status_code=429, detail="Too many requests")

        response = await call_next(request)
        return response
