from django.urls import path
from login.views import sumar, showFormLogin
urlpatterns = [
    path('sumar/<int:a>/<int:b>', sumar),
    #path('/login', showFormLogin),
]