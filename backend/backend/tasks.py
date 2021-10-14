from backend.celery import  app

from todo.models import Todolist
from todo.serializers import TodolistSerializer

from rest_framework.response import Response

@app.task
def todo_list_task():
    todo = Todolist.objects.all()
    serializer = TodolistSerializer(todo, many=True)
    return serializer.data


@app.task
def todo_add_task(data):
    serializer = TodolistSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return {"true": serializer.data}
    return {"false" : "serializer bad"}

@app.task
def todo_delete_task(pk):
    todo = Todolist.objects.filter(pk=pk)
    todo.delete()
    return True


@app.task
def todo_update_task(data,pk):
    todo = Todolist.objects.get(pk=pk)
    serializer = TodolistSerializer(todo, data=data)
    if serializer.is_valid():
        serializer.save()
        return {"true": serializer.data}
    return {"false": "serializer bad"}


@app.task
def todo_update_check_task(data,pk):
    todo = Todolist.objects.get(pk=pk)
    serializer = TodolistSerializer(todo, data=data)
    if serializer.is_valid():
        serializer.save()
        return {"true": serializer.data}
    return {"false": "serializer bad"}
