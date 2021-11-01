from django.urls import path
from .consumer import WSConsumer

ws_urlpatterns = [
    path('ws/get/', WSConsumer.as_asgi()),

]
