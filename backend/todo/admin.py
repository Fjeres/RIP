from django.contrib import admin

from todo.models import Todolist


class TodolistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'checked')


admin.site.register(Todolist, TodolistAdmin)