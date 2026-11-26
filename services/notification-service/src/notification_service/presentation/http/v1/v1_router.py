from fastapi import APIRouter

from notification_service.presentation.http.v1.routers.settings_router import router as settings_router


v1_router = APIRouter(prefix="/v1")

v1_router.include_router(settings_router)
