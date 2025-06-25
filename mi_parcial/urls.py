from django.urls import path
from . import views
from .views import listadoconsultas, modificar_consulta, eliminar_consulta
from django.contrib.auth import views as auth_views
from . import create_superuser


urlpatterns = [
    path('', views.pagina_inicio, name='index'),
    path('listadoconsultas/', listadoconsultas, name='listadoconsultas'),
    path('servicios/', views.servicios, name='servicios'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contacto/', views.contacto, name='contacto'),
    path('eliminarconsultas/<int:consulta_id>/', eliminar_consulta, name='eliminar_consulta'),
    path('modificarconsultas/<int:consulta_id>/', modificar_consulta, name='modificar_consulta'),
    path('api/consultas/', views.api_consultas, name='api_consultas'),
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='mi_parcial/login.html'), name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]