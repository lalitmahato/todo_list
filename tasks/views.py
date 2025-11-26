from django.shortcuts import render
from tasks.models import Task

# Create your views here.

# List View
def task_list(request):
    tasks = Task.objects.all()
    print(tasks)
    context = {
        'tasks': tasks
    }
    return render(request, "index.html", context)

