from django.db import models
from task_category.models import CategoryForm

# Create your models here.
class TaskModel(models.Model):
    task_title = models.CharField(max_length=100)
    task_category = models.ManyToManyField(CategoryForm)
    task_description = models.TextField()
    is_completed = models.BooleanField(default=False)
    task_assign_date = models.DateField()

    def __str__(self):
        return self.task_title