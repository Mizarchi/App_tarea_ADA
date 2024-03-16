from django.contrib import admin
from .models import Task

# Registro del modelo Task en el panel de administración
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'fecha_creacion', 'estado')
    search_fields = ('titulo', 'descripcion', 'estado')
