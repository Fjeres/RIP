import json
from channels.generic.websocket import WebsocketConsumer


class WSConsumer(WebsocketConsumer):
    async def connect(self):

        self.room_name = self.scope['url_route']['kwargs']

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await  self.accept()
        await  self.send(json.dumps({"message": "message"}))

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
