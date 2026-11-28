from enum import Enum


class InboxScope(str, Enum):
    USERS_CREATE = "settings.users.create"
