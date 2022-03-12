"""gepfy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from gepfy.views import register, welcome, salir, main, actualizar, services, movement, reportsAndGraphs, contact
# login y logout
urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', register, name='registro'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('index/', welcome, name='index'),
    path('salir/', salir, name='salir'),
    path('', main, name='main'),
    path('my_data/', actualizar, name='myData'),
    path('services/', services, name='services'),
    path('movement/', movement, name='movement'),
    path('reports-and-graphs', reportsAndGraphs, name='reports'),
    path('contact/', contact, name='contact'),
    path('services/', include('services.urls')),
]
