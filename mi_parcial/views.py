import email
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from .forms import consultasForm
from django.shortcuts import get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Consultas
from .serializers import ConsultaSerializer
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.

def pagina_inicio(request):
    return render(request, 'mi_parcial/index.html')



def listadoconsultas(request) :
    consultas = Consultas.objects.all()
    return render(request, 'mi_parcial/listadoconsultas.html', {"consultas": consultas})

def nosotros(request):
    return render(request, 'mi_parcial/nosotros.html')


def contacto(request):
    if request.method == "POST":
        form = consultasForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            correo = form.cleaned_data["email"]
            mensaje = form.cleaned_data["mensaje"]
            nueva_consulta = Consultas(
                nombre=nombre,
                email=correo,
                mensaje=mensaje
            )
            nueva_consulta.save()
            asunto = "Nueva consulta desde el sitio web"
            mensaje_email = f"Nombre: {nombre}\nEmail: {correo}\nMensaje:\n{mensaje}"
            send_mail(
                asunto,
                mensaje_email,
                settings.DEFAULT_FROM_EMAIL,
                [correo],
                fail_silently=False
            )
            return render(request, 'mi_parcial/contacto.html', {
                'form': consultasForm(),
                'mensajeexito': "¡Tu consulta fue enviada con exito!"
            })
    else:
        form = consultasForm()
    return render(request, 'mi_parcial/contacto.html', {
        'form': form
    })

def servicios(request):
    return render(request, 'mi_parcial/servicios.html')

def categoria(mensaje):
    mensaje = mensaje.lower()
    if any(palabra in mensaje for palabra in ["precio", "costo", "tarifa", "compra"]):
        return "Consulta Comercial"
    elif any(palabra in mensaje for palabra in ["soporte", "error", "problema", "ayuda"]):
        return "Consulta Tecnica"
    elif any(palabra in mensaje for palabra in ["trabajo", "cv", "empleo", "linkedin"]):
        return "Consulta de RRHH"
    else:
        return "Consulta General"

def eliminar_consulta(request, consulta_id):
    consulta = get_object_or_404(Consultas, id=consulta_id)
    consulta.delete()
    return JsonResponse({ "success": True, "Message": "Consulta eliminada correctamente" })

def modificar_consulta(request, consulta_id):
    consulta = get_object_or_404(Consultas, id=consulta_id)

    if request.method == 'POST':
        form = consultasForm(request.POST)
        if form.is_valid():
            consulta.nombre = form.cleaned_data['nombre']
            consulta.email = form.cleaned_data['email']
            consulta.mensaje = form.cleaned_data['mensaje']
            consulta.save()

            return redirect('listadoconsultas')
    else:
        form = consultasForm(initial={
            'nombre': consulta.nombre,
            'email': consulta.email,
            'mensaje': consulta.mensaje,
        })

    return render(request, 'mi_parcial/listadoconsulta.html', {'form': form,'consulta': consulta})


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'mi_parcial/registro.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'mi_parcial/dashboard.html')


@api_view(['GET'])
def api_consultas(request):
    consultas = Consultas.objects.all()
    serializer = ConsultaSerializer(consultas, many=True)
    return Response(serializer.data)