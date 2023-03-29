from channels.db import database_sync_to_async
from django.core.exceptions import ValidationError

from .models import Notification


@database_sync_to_async
def add_val_to_notification_model(title: None, description: None) -> None:
    try:
        new_row = Notification()
        new_row.set_title(title)
        new_row.set_description(description)
        new_row.save()
    except ValidationError as validation_error:
        raise Exception(validation_error.message)
    except Exception as error:
        pass


@database_sync_to_async
def count_notification_model_row():
    try:
        return Notification.objects.count()
    except Exception as error:
        pass
