from rest_framework import serializers
from todo.models import Todolist


# Todolist Serializer
class TodolistSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=False)
    checked = serializers.BooleanField(default=False)

    class Meta:
        model = Todolist
        fields = ['id', 'name', 'checked']
