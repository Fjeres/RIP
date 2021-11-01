from django.contrib import admin

from todo.models import Todolist, TodoNotes


class TodolistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'checked')

class TodoNotesAdmin(admin.ModelAdmin):
    list_display = ('id', 'text',)

admin.site.register(Todolist, TodolistAdmin)
admin.site.register(TodoNotes, TodoNotesAdmin)