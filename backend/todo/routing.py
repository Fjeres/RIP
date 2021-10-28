from django.urls import path
from .consumer import WSConsumer

ws_urlpatterns = [
    path('ws/get/', WSConsumer.as_asgi()),
    path('ws/post/', WSConsumer.as_asgi()),
    path('ws/delete/', WSConsumer.as_asgi()),
    path('ws/put_update/', WSConsumer.as_asgi()),
    path('ws/put_check/', WSConsumer.as_asgi()),
]
