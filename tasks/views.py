from django.shortcuts import render, redirect
from tasks.models import Task
from tasks.forms import TaskForm
from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users


# Create your views here.
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'user'])
def task_list(request):
    tasks = Task.objects.all()
    form = TaskForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid:
            task_form = form.save(commit=False)
            task_form.creator = request.user
            task_form.save()
            return redirect('task_list')
    context = {
        'tasks': tasks,
        'form': form
    }
    return render(request, "index.html", context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_task(request, id):
    instance = Task.objects.get(id=id)
    tasks = Task.objects.all()
    form = TaskForm(request.POST or None, instance=instance)
    if request.method == "POST":
        if form.is_valid:
            task_form = form.save(commit=False)
            task_form.modifier = request.user
            task_form.save()
            return redirect('task_list')
    context = {
        'tasks': tasks,
        'form': form
    }
    return render(request, "index.html", context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_task(request, id):
    instance = Task.objects.get(id=id)
    instance.delete()
    return redirect('task_list')

