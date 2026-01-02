from django.urls import path
from classbasedview.views import *

urlpatterns = [
    path('', TaskListView.as_view(), name='class_task_list'),
    path('create-view/', TaskCreateView.as_view(), name='class_task_create'),
    # path('<int:pk>/edit/', TaskUpdateView.as_view(), name='class_task_update'),
]