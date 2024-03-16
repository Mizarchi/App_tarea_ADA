from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm, TaskUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


@login_required
def listar_tareas(request):
    tareas = Task.objects.all()
    return render(request, 'listar_tareas.html', {'tareas': tareas})


@login_required
def crear_tarea(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tareas')
    else:
        form = TaskForm()
    return render(request, 'crear_tarea.html', {'form': form})


@login_required
def editar_tarea(request, pk):
    tarea = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskUpdateForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('listar_tareas')  # Redirige a la lista de tareas
    else:
        form = TaskUpdateForm(instance=tarea)
    return render(request, 'editar_tarea.html', {'form': form, 'tarea': tarea})


@login_required
def eliminar_tarea(request, pk):
    tarea = get_object_or_404(Task, pk=pk)
    tarea.delete()
    return redirect('listar_tareas')


# vistas para la autenticacion
def registrar_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'registro.html', {'error_username': True})

        if User.objects.filter(email=email).exists():
            return render(request, 'registro.html', {'error_email': True})

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )

        if user is not None:
            return redirect('inicio_sesion')

        return render(request, 'registro.html', {'error': True})
    else:
        # Mostrar formulario de registro
        return render(request, 'registro.html')


def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(next)
        else:
            # Mostrar mensaje de error de inicio de sesión
            return render(request, 'inicio_de_sesion.html', {'error': True})
    else:
        # Mostrar formulario de inicio de sesión
        return render(request, 'inicio_de_sesion.html')


def cerrar_sesion(request):
    logout(request)
    return redirect('login')
