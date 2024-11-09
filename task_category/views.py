from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def add_category(request):
    if request.method == "POST":
        form = TaskCatgoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = TaskCatgoryForm()
    return render(request, 'add_category.html', {"form" : form})