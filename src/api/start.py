from fastapi import FastAPI
from src.payment_cache.rate_limit import RateLimitMiddleware


def start_app() -> FastAPI:
    app = FastAPI(title="Payment Getaway")
    app.add_middleware(RateLimitMiddleware)

    return app
