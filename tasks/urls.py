"""
tasks urls
"""
from django.contrib import admin
from django.urls import path
from tasks.views import task_list, update_task, delete_task

urlpatterns = [
    path('', task_list, name='task_list'),
    path('edit/<int:id>/', update_task, name='update_task'),
    path('delete/<int:id>/', delete_task, name='delete_task'),
]
