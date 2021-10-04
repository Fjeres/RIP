from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todolist
from .serializers import TodolistSerializer


@api_view(['GET'])
def todo_list(request):
    if request.method == 'GET':
        todo = Todolist.objects.all()
        serializer = TodolistSerializer(todo, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def todo_one(request, pk: int):
    if request.method == 'GET':
        todo = Todolist.objects.get(pk=pk)
        serializer = TodolistSerializer(todo)
        return Response(serializer.data)


@api_view(['POST'])
def todo_add(request):
    if request.method == 'POST':
        serializer = TodolistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def todo_delete(request, pk):
    if request.method == 'DELETE':
        todo = Todolist.objects.filter(pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def todo_update(request, pk: int):
    if request.method == 'PUT':
        todo = Todolist.objects.get(pk=pk)
        serializer = TodolistSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def todo_update_check(request, pk: int):
    if request.method == 'PUT':
        todo = Todolist.objects.get(pk=pk)
        serializer = TodolistSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
