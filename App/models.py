from django.db import models
from django.contrib.auth.models import User

def nuevoUsuario(nombre, email, contraseña):
    return User.objects.create_user(username=nombre, email=email, password=contraseña)

# Create your models here.
class Medico(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    numero = models.CharField(max_length=20)
    puesto = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user = User.objects.create_user(username=self.nombre, email=self.email, password=self.contraseña)
            self.contraseña = None
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Nombre Medico= {self.nombre} | Nombre User= {self.user.username}'

class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    numero = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user = nuevoUsuario(self.nombre, self.email)
        super().save(*args, **kwargs)


