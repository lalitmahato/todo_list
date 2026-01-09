from django.urls import path
from classbasedview.views import *

app_name = "class_based_view"

urlpatterns = [
    path('', TaskListView.as_view(), name='class_task_list'),
    path('create-view/', TaskCreateView.as_view(), name='class_task_create'),
    path('<int:pk>/detail-view/', TaskDetailView.as_view(), name='class_task_detail'),
    path('<int:pk>/edit/', TaskUpdateView.as_view(), name='class_task_update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='class_task_delete'),
]