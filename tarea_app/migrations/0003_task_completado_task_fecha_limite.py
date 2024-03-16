# Generated by Django 5.0.3 on 2024-03-15 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarea_app', '0002_rename_description_task_descripcion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='fecha_limite',
            field=models.DateField(blank=True, null=True),
        ),
    ]