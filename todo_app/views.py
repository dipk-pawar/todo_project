from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages


# Create your views here.
def Home(request):
    tasks = Task.objects.filter(is_completed=False)
    completed_tasks = Task.objects.filter(is_completed=True)
    return render(
        request, "home.html", context={"tasks": tasks, "cm_tasks": completed_tasks}
    )


def create_todo(request):
    title = request.POST.get("title")
    if not title.strip():
        messages.error(request, "Sorry, Task name is required")
        return redirect("home")
    Task.objects.create(title=title)
    messages.success(request, "Task added successfully")
    return redirect("home")


def complete_task(request, id):
    if task := Task.objects.filter(id=id):
        task.update(is_completed=True)
        messages.success(request, "Task marked as completed successfully")
    else:
        messages.error(request, "Sorry, Task not found")
    return redirect("home")


def un_complete_task(request, id):
    if task := Task.objects.filter(id=id):
        task.update(is_completed=False)
        messages.success(request, "Task marked as uncompleted")
    else:
        messages.error(request, "Sorry, Task not found")
    return redirect("home")


def edit_post(request, id):
    task = Task.objects.get(id=id)
    if not task:
        messages.error(request, "Sorry, Task not found")
        return redirect("home")
    if request.method == "POST":
        title = request.POST.get("title")
        task.title = title
        task.save()
        messages.success(request, "Task updated successfully")
        return redirect("home")
    return render(request, "edit_task.html", context={"get_task": task})


def delete_task(request, id):
    if task := Task.objects.filter(id=id):
        task.delete()
        messages.success(request, "Task deleted successfully")
    else:
        messages.error(request, "Sorry, Task not found")
    return redirect("home")
