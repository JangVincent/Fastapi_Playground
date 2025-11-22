from fastapi import APIRouter

from src.domains.user.router import router as user_router

aggregated_router = APIRouter()

aggregated_router.include_router(user_router)
