from django.shortcuts import render, redirect
from .forms import CreateTaskForm
from .models import Task


# Create your views here.



def home(request):
    user = request.user
    user_tasks = Task.objects.filter(user=user).all()
    context = {
        "user" : user,
        "user_tasks" : user_tasks
    }
    return render(request, 'home/home.html', context)


def task_details(request, task_id):
    task = Task.objects.get(pk=task_id)
    context = {
        "task" : task
    }
    return render(request, 'home/task_detail.html', context)

def create_task(request):

    if request.method == 'POST':
        print(request.POST)
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('task:home')
        else:
            print(form.errors)
    else:
        form = CreateTaskForm()
    return render(request, 'forms/create_task.html', {'form': form})