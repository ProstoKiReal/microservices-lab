from faststream.rabbit.broker import RabbitRouter
from dishka_faststream import FromDishka

from notification_service.presentation.broker.queues import Topics
from notification_service.presentation.broker.schemas.settings import SettingsCreateRequest,SettingsDeleteRequest
from notification_service.application.dtos.settings import SettingsCreateRequestDTO, SettingsDeleteRequestDTO
from notification_service.application.handlers.settings import SettingsCreateHandler, SettingsDeleteHandler


router = RabbitRouter()
# TODO add broker root router


@router.subscriber(queue=Topics.USERS_CREATE)
async def create_settings(
    create_settings_request: SettingsCreateRequest,
    handler: FromDishka[SettingsCreateHandler],
):
    settings_dto = SettingsCreateRequestDTO(**create_settings_request.model_dump())
    await handler(settings_dto)


@router.subscriber(queue=Topics.USERS_DELETE)
async def delete_user_settings(
    delete_settings_request: SettingsDeleteRequest,
    handler: FromDishka[SettingsDeleteHandler],
):
    settings_dto = SettingsDeleteRequestDTO(**delete_settings_request.model_dump())
    await handler(settings_dto)
