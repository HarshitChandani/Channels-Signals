from django.urls import path
from .consumers import NotificationConsumer

ASGI_URL_PATTERNS = [path("ws/connect/", NotificationConsumer.as_asgi())]
