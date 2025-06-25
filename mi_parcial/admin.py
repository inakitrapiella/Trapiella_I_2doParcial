from django.contrib import admin
from .models import Consultas, UsuariosPermitidos

# Register your models here.

admin.site.register([Consultas, UsuariosPermitidos])
