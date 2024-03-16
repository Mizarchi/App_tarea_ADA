from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_tareas, name='listar_tareas'),
    path('crear/', views.crear_tarea, name='crear_tarea'),
    path('editar/<int:pk>/', views.editar_tarea, name='editar_tarea'),
    path('eliminar/<int:pk>/', views.eliminar_tarea, name='eliminar_tarea'),
    path('registro/', views.registrar_usuario, name='registro'),
    path('inicio-sesion/', views.iniciar_sesion, name='inicio_sesion'),
]
