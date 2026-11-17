from faststream.kafka.broker import KafkaBroker

from notification.presentation.broker.schemas.users import UserCreateRequest,UserDeleteRequest


router = KafkaBroker()


@router.subscriber("Users.Create")
async def create_user_settings(create_user_request: UserCreateRequest):
    return {"msg": "ok"}


@router.subscriber("Users.Delete")
async def delete_user_settings(delete_user_request: UserDeleteRequest):
    return {"msg": "ok"}
