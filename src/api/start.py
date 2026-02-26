import uvicorn
from fastapi import FastAPI
from src.api.rate_limiter.rate_limit import RateLimitMiddleware
from src.api.endpoints.v1 import v1_router


def start_app() -> FastAPI:
    app = FastAPI(title="Payment Getaway")
    app.add_middleware(RateLimitMiddleware)
    app.include_router(router=v1_router)

    return app


if __name__ == "__main__":
    app = start_app()
    uvicorn.run(app, host="0.0.0.0", port=8000)
