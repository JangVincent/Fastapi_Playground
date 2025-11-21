from fastapi import APIRouter

from src.domains.user.router import router as user_router

domain_router = APIRouter()

domain_router.include_router(user_router)
