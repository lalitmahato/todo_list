from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from tasks.models import Task
from tasks.forms import TaskForm

# Create your views here.
class TaskListView(ListView):
    template_name = 'class_index.html'
    model = Task
    context_object_name = "tasks"


class TaskCreateView(CreateView):
    template_name = 'class_index.html'
    form_class = TaskForm
    success_url = reverse_lazy('class_task_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'class_index.html'
    form_class = TaskForm
    success_url = reverse_lazy('class_task_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context





