from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.todo_list, name='all'),
    path('todo/<int:pk>', views.todo_one, name='get'),
    path('update/<int:pk>', views.todo_update, name='update'),
    path('check/<int:pk>', views.todo_update_check, name='update'),
    path('add', views.todo_add, name='Post'),
    path('delete/<int:pk>', views.todo_delete, name='Delete'),
]
