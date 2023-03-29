# Built-in module imports
import json

# Django Imports
from django.test import TestCase, Client
from channels.testing import WebsocketCommunicator
from django.db.models import signals

# Project imports
from notifications.consumers import NotificationConsumer
from notifications.utils import (
    add_val_to_notification_model,
    count_notification_model_row,
)
from notifications.models import Book
from notifications.signals import send_notification


class ConsumerTestCase(TestCase):
    async def test_ws(self):
        communicator_instance = WebsocketCommunicator(
            NotificationConsumer.as_asgi(), "ws/connect/"
        )
        is_ws_connected, subprotocal = await communicator_instance.connect()

        # Test sending of data frame .
        await communicator_instance.send_to(
            text_data=json.dumps({"message": "Hello Harshit"})
        )

        # Test that no frame is received as received method of consumer class will not send any data.
        is_nothing_received = await communicator_instance.receive_nothing()

        self.assertTrue(is_ws_connected)
        self.assertIsNone(subprotocal)
        self.assertTrue(is_nothing_received)
        # context manager
        with self.assertRaises(AttributeError):
            await communicator_instance.disconnect(code=1000)


class TemplateTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.root = "http://localhost:8000/"

    def test_index_template_render(self):
        response = self.client.get(self.root)
        self.assertTemplateUsed(response, "base.html")


class UtilsMethodTestCase(TestCase):
    async def test_add_val_to_notification_model_method(self):

        await add_val_to_notification_model(
            title="Harry potter", description="The prisionar of azkaban."
        )

        count_rows = await count_notification_model_row()
        self.assertEqual(
            count_rows, 1, msg="New row inserted in the notification model"
        )

# pending
class SignalTestCase(TestCase):
    def test_post_save_signal(self):

        signals.post_save.connect(
            receiver=send_notification,
            sender=Book,
            dispatch_uid="test_book_post_save_signal",
        )
