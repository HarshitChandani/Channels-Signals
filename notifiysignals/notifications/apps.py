from django.apps import AppConfig
from django.db.models.signals import post_save


from .signals import send_notification


class NotificationsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "notifications"

    def ready(self) -> None:
        from .models import Book

        try:
            post_save.connect(
                receiver=send_notification, sender=Book, dispatch_uid="notify_signal"
            )
        except Exception as error:
            return error.message
