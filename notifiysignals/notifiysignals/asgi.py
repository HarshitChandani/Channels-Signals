import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter

from notifications.routing import ASGI_URL_PATTERNS

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notifiysignals.settings")
from notifications import consumers

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": URLRouter(ASGI_URL_PATTERNS),
        "channel": ChannelNameRouter(
            {"notification": consumers.NotificationConsumer.as_asgi()}
        ),
    }
)
