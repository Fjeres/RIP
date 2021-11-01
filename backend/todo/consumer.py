import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import TodoNotes
from .serializers import TodoNotesSerializer


class WSConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        todo = TodoNotes.objects.all()
        serializer = TodoNotesSerializer(todo, many=True)
        self.send(json.dumps(serializer.data))

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if text_data_json['header'] == 'PUT':

            todo = TodoNotes.objects.get(pk=text_data_json['id'])

            data = {
                "text": text_data_json['text']
            }

            serializer = TodoNotesSerializer(todo, data=data)
            if serializer.is_valid():
                serializer.save()

        if text_data_json['header'] == 'DELETE':
            todo = TodoNotes.objects.filter(pk=text_data_json['id'])
            todo.delete()

        if text_data_json['header'] == 'POST':
            data = {
                "text": text_data_json['text']
            }
            serializer = TodoNotesSerializer(data=data)
            if serializer.is_valid():
                serializer.save()


        todo_temp = TodoNotes.objects.all()
        serializer_temp = TodoNotesSerializer(todo_temp, many=True)
        self.send(text_data=json.dumps(serializer_temp.data))
