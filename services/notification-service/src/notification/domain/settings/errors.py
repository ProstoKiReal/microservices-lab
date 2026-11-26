from notification.domain.common.errors import BaseDomainError


class SettingsDomainError(BaseDomainError): ...


class TelegramIdDomainError(SettingsDomainError):
    def __init__(self, telegram_id: int) -> None:
        super().__init__(f"Telegram id {str(telegram_id)} invalid")


class EmailDomainError(SettingsDomainError):
    def __init__(self, email: str) -> None:
        super().__init__(f"Email {str(email)} invalid")


class NotExistedNotificationChannelDomainError(SettingsDomainError):
    def __init__(self) -> None:
        super().__init__("Not provide notification channel")
