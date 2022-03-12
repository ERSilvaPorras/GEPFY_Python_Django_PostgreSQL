from pyexpat.errors import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import logout, get_user
from django.contrib.auth.decorators import login_required
from login.forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
@login_required
def welcome(request):
    return render(request, 'index.html')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to='index')
        data['form']=formulario
        messages.warning(request, "Ingrese correctamente los campos pedidos")
    return render(request, 'registration/registro.html', data)

def actualizar(request):

    if request.method == 'POST':
        user_profile = User.objects.get(id=request.user.id)
        formulario = CustomUserCreationForm(request.POST, instance=user_profile)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Cambios guardados correctamente.")
            return redirect(to='index')
        messages.warning(request, "Ingrese correctamente los campos pedidos")
    user_profile = User.objects.get(id=request.user.id)
    formulario = CustomUserCreationForm(instance=user_profile)
    formulario.password1 = user_profile.password
    print(str(user_profile))
    
    print(str(request.user.id))
    return render(request, 'myData.html', {'form': formulario})

def salir(request):
    logout(request)
    return redirect('main')

def main(request):
    return render(request, 'main.html')

@login_required
def myData(request):
    return render(request, 'myData.html')

@login_required
def services(request):
    return render(request, 'services.html')

@login_required
def movement(request):
    return render(request, 'movement.html')

@login_required
def reportsAndGraphs(request):
    return render(request, 'reportsAndGraphs.html')

@login_required
def contact(request):
    return render(request, 'contact.html')