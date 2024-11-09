from django import forms
from .models import * 


class TaskCatgoryForm(forms.ModelForm):
    class Meta:
        model = CategoryForm
        fields = "__all__"