from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api.views import (TaskViewSet, TaskListAPIView, TaskCreateAPIView, TaskRetrieveAPIView, TaskUpdateAPIView,
                       TaskDestroyAPIView, TaskListCreateView, TaskRetrieveUpdateDestroyView)

schema_view = get_schema_view(
    openapi.Info(
        title="Todo List API",
        default_version='v2',
        description="The TaskMaster API provides a robust and flexible interface for managing todo lists and tasks programmatically. Designed with simplicity in mind, this RESTful API allows developers to integrate task management features—such as creating, updating, organizing, and prioritizing tasks—directly into their applications.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="info@lalitmahato.com.np"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Create a router and register our viewset with it.
router = routers.SimpleRouter()

urlpatterns = [
    path('swagger.<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('task/generic/', TaskListAPIView.as_view(), name='task-list'),
    path('task/generic/create/', TaskCreateAPIView.as_view(), name='task_create'),
    path('task/generic/<int:pk>/', TaskRetrieveAPIView.as_view(), name='task_retrieve'),
    path('task/generic/edit/<int:pk>/', TaskUpdateAPIView.as_view(), name='task_update'),
    path('task/generic/delete/<int:pk>/', TaskDestroyAPIView.as_view(), name='task_delete'),
    path('task/generic/list-create/', TaskListCreateView.as_view(), name='task_list_create'),
    path('task/generic/retrive-update-destroy/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task_list_retrieve_update_destroy'),
    path('login/', obtain_auth_token, name='api_token_auth'),
]

router.register(r"task", TaskViewSet, basename="task_viewset")

urlpatterns += router.urls
