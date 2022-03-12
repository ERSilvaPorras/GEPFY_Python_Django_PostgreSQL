from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
# def sumar (request,a , b):
#     result = a + b
#     return HttpResponse(str(result))

# def showFormLogin (request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password1']
#         user = authenticate(request, username=username, password=password)
#         if user is None:
#             login(request, user)
#             print(str(messages))
#             return redirect('index/')
            
#         else:
#             messages.success(request, 'El usuario y/o contraseña son incorrectos.')
#             messages.warning(request, 'Please correct the error below.')
#             return redirect('/accounts/login')
#     else:
#         return render(request, './registration/login.html')
