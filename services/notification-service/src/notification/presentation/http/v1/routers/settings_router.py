from fastapi import APIRouter, status


router = APIRouter(
    prefix="/settings",
    tags=["Settings"],
)


@router.get("/", status_code=status.HTTP_200_OK)
async def get_my_settings():
    return {"msg": "ok"}


@router.patch("/")
async def update_my_settings():
    return {"msg": "ok"}
