from django import forms
from .models import *

class TaskModelForm(forms.ModelForm):
    task_assign_date = forms.DateField(widget=forms.DateInput(attrs={"type" : "date"}))
    class Meta:
        model = TaskModel
        fields = "__all__"
