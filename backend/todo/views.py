from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todolist
from .serializers import TodolistSerializer
import pika
import json



@api_view(['GET'])
def todo_list(request):
    if request.method == 'GET':
        todo = Todolist.objects.all()
        serializer = TodolistSerializer(todo, many=True)
        send_log(request.META)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def todo_one(request, pk: int):
    if request.method == 'GET':
        todo = Todolist.objects.get(pk=pk)
        serializer = TodolistSerializer(todo)
        return Response(serializer.data)


@api_view(['POST'])
def todo_add(request):
    if request.method == 'POST':
        send_log(request.META)
        serializer = TodolistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def todo_delete(request, pk):
    if request.method == 'DELETE':
        send_log(request.META)
        todo = Todolist.objects.filter(pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def todo_update(request, pk: int):
    if request.method == 'PUT':
        send_log(request.META)
        todo = Todolist.objects.get(pk=pk)
        serializer = TodolistSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def todo_update_check(request, pk: int):
    if request.method == 'PUT':
        send_log(request.META)
        todo = Todolist.objects.get(pk=pk)
        serializer = TodolistSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


def send_log(meta):
    rmq_url_connection_str = 'amqp://demo_app_rabbitmq:5672/'  # 15672
    connection = pika.BlockingConnection(pika.URLParameters(
        rmq_url_connection_str))
    channel = connection.channel()
    channel.basic_publish(exchange='',
                          routing_key='task_queue',
                          body=json.dumps(meta),
                          properties=pika.BasicProperties(
                              delivery_mode=2,
                          ))