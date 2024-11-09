# Generated by Django 5.1.2 on 2024-11-09 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('task_model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('task_category', models.ManyToManyField(to='task_model.taskmodel')),
            ],
        ),
    ]
