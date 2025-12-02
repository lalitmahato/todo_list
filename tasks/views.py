from django.shortcuts import render, redirect
from tasks.models import Task
from tasks.forms import TaskForm

# Create your views here.

# List View
def task_list(request):
    tasks = Task.objects.all()
    form = TaskForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid:
            form.save()
            return redirect('task_list')
    context = {
        'tasks': tasks,
        'form': form
    }
    return render(request, "index.html", context)


def update_task(request, id):
    instance = Task.objects.get(id=id)
    tasks = Task.objects.all()
    form = TaskForm(request.POST or None, instance=instance)
    if request.method == "POST":
        if form.is_valid:
            form.save()
            return redirect('task_list')
    context = {
        'tasks': tasks,
        'form': form
    }
    return render(request, "index.html", context)


def delete_task(request, id):
    instance = Task.objects.get(id=id)
    instance.delete()
    return redirect('task_list')

