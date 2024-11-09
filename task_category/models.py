from django.db import models

# Create your models here.
class CategoryForm(models.Model):
    category_name = models.CharField(max_length=100)
    # task_category = models.ManyToManyField(TaskModel)

    def __str__(self) -> str:
        return self.category_name