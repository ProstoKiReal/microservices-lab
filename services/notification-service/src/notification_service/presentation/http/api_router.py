from fastapi import APIRouter

from notification_service.presentation.http.v1.v1_router import v1_router


api_router = APIRouter(prefix="/api")

api_router.include_router(v1_router)
