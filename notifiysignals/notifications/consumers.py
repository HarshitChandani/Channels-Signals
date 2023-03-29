import json
import asyncio

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.exceptions import StopConsumer, AcceptConnection

from .utils import add_val_to_notification_model


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        try:
            # group
            self.group_name = "notification-room"
            await self.channel_layer.group_add(self.group_name, self.channel_name)
            await self.accept()
            raise AcceptConnection()
        except AcceptConnection as ac:
            print("Connection established")
        except Exception as error:
            raise AttributeError(error)

    async def disconnect(self, code):
        try:
            # Close codes ranges values is between 1001 - 1015 for the actual reasons of closing the connection.Here we are specifying the 1000 for the normal closure.
            await self.channel_layer.group_discard(self.group_name, self.channel_name)
            await self.close(code)
        except Exception as error:
            raise Exception(error.__cause__)
        finally:
            # we need to raise channels.exceptions.StopConsumer to halt the ASGI application cleanly and let the server clean it up. If you leave it running - by not raising this exception - the server will reach its application close timeout (which is 10 seconds by default in Daphne) and then kill your application and raise a warning.
            raise StopConsumer()

    async def receive(self, text_data=None):
        # receive: used to received the message from browser.
        # NOTE: we are not sending any data back to browser.
        try:
            data = json.loads(text_data)
            message = data["message"]
            print("New message received.{0}".format(message))
        except Exception as error:
            raise Exception(error.__cause__)

    async def notification_send(self, event):
        try:
            received_message = event["text"]["message"]

            # gather will run the task concurrently. Here we would not able to identify the concurrency because no two task has sleep method to use.

            await asyncio.gather(
                self.send(text_data=json.dumps({"message": received_message})),
                add_val_to_notification_model(
                    title=event["text"]["title"],
                    description=received_message,
                ),
            )
        except Exception as e:
            raise Exception(e)
