from django import forms
from .models import Task
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['titulo', 'descripcion', 'estado']

class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['titulo', 'descripcion', 'estado']

class TaskSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False, label='Buscar tarea')


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class InicioSesionForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']