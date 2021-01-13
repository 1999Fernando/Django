"""Django_init URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Aplicaciones.principal.views import inicio
from Aplicaciones.principal.views import crearPersona,editarPersona,eliminarPersona,registerPage, loginPage, logoutUser
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',inicio,name = 'index'),
    path('crear_persona/',crearPersona, name = 'crear_persona'),
    path('editar_persona/<int:id>/',editarPersona, name = 'editar_persona'),
    path('eliminar_persona/<int:id>/',eliminarPersona, name = 'eliminar_persona'),
    path('register/',registerPage, name = 'register'),
    path('',loginPage, name = 'login'),
    path('logout', logoutUser, name = 'logout')
]
