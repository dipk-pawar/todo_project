from django.shortcuts import render
from .models import *


# Create your views here.
def Home(request):
    tasks = Task.objects.filter(is_completed=False)
    return render(request, "home.html", context={"tasks": tasks})
