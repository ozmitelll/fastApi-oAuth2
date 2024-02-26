from fastapi import APIRouter

from api import (
    user,
)
api_router = APIRouter()
api_router.include_router(user.auth, prefix="/auth", tags=["Authentication"])
api_router.include_router(user.router, prefix="/user", tags=["User"])

