from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import (ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView,
                                     ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from api.paginations import CustomPagination
from api.serializers import TaskSerializer
from tasks.models import Task


# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
    pagination_class = CustomPagination


class TaskListAPIView(ListAPIView):
    """
    API endpoint that allows tasks to be listed.
    """
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
    pagination_class = CustomPagination


class TaskCreateAPIView(CreateAPIView):
    """
    API endpoint that allows tasks to be created.
    """
    serializer_class = TaskSerializer

    def post(self, request, *args, **kwargs):
        api_status = False
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            api_status = True
        return Response(
            {
                "status": api_status,
                "errors": serializer.errors,
                "results": serializer.data
            }, status=status.HTTP_201_CREATED if api_status else status.HTTP_400_BAD_REQUEST
        )




class TaskRetrieveAPIView(RetrieveAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskUpdateAPIView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDestroyAPIView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskListCreateView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
