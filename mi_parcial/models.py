from django.db import models

# Tablas Consultas.

class Consultas( models.Model ):
    nombre = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mensaje = models.TextField()
    categoria = models.CharField(max_length=50, default='Consulta General')


class UsuariosPermitidos(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    codigo_validacion = models.CharField(max_length=10)
    def __str__(self):
        return self.email