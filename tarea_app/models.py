from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Task(models.Model):
    STATUS_CHOICES = (
        ('Pendiente', 'Pendiente'),
        ('Completado', 'Completado'),
    )

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='Pendiente')
    completado = models.BooleanField(default=False)
    fecha_limite = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.titulo


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('El email es obligatorio')
        if not username:
            raise ValueError('El nombre de usuario es obligatorio')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email=email, username=username, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
