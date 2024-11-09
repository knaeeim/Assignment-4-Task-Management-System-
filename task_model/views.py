from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.
def add_task(request):
    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('homepage')
    else:
        form = TaskModelForm()
    return render(request, 'add_task.html', {"form" : form})


def edit_task(request, id):
    form = TaskModel.objects.get(pk=id)
    if request.method == "POST":
        form = TaskModelForm(request.POST, instance=form)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:
        form = TaskModelForm(instance=form)
    return render(request, "edit_task.html", {"form" : form})

def delete_task(request, id):
    form = TaskModel.objects.get(pk=id)
    form.delete()
    return redirect("homepage")