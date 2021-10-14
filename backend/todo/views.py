from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todolist
from .serializers import TodolistSerializer
from backend.tasks import todo_list_task, todo_add_task, todo_delete_task, todo_update_task


@api_view(['GET'])
def todo_list(request):
    if request.method == 'GET':
        todo = todo_list_task.delay()
        temp = {}
        while not todo.ready():
            temp = todo.get(timeout=1)
        return Response(temp, status=status.HTTP_200_OK)


@api_view(['GET'])
def todo_one(request, pk: int):
    if request.method == 'GET':
        todo = Todolist.objects.get(pk=pk)
        serializer = TodolistSerializer(todo)
        return Response(serializer.data)


@api_view(['POST'])
def todo_add(request):
    if request.method == 'POST':
        todo = todo_add_task.delay(request.data)
        temp = {}
        while not todo.ready():
            temp = todo.get(timeout=1)
        if temp.get("true") is not None:
            return Response(temp['true'], status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def todo_delete(request, pk):
    if request.method == 'DELETE':
        todo = todo_delete_task.delay(pk=pk)
        while not todo.ready():
            todo.get(timeout=1)
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def todo_update(request, pk: int):
    if request.method == 'PUT':
        todo = todo_update_task.delay(data= request.data,pk=pk)
        temp = {}
        while not todo.ready():
            temp = todo.get(timeout=1)
        if temp.get("true") is not None:
            return Response(temp['true'], status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def todo_update_check(request, pk: int):
    if request.method == 'PUT':
        todo = todo_update_task.delay(data=request.data, pk=pk)
        temp = {}
        while not todo.ready():
            temp = todo.get(timeout=1)
        if temp.get("true") is not None:
            return Response(temp['true'], status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
