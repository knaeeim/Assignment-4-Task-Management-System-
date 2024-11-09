from django.shortcuts import render
from task_model.models import *
# Create your views here.

def home(request):
    tasks = TaskModel.objects.all()
    return render(request, 'home.html', {"tasks" : tasks})