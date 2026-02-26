from fastapi import APIRouter
from src.api.endpoints.v1.whoami import router as whoami_router

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(whoami_router, tags=["Utility"])
