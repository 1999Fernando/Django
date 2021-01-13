from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import Persona
from .forms import PersonaForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import  login_required


from .models import *
from .forms import PersonaForm,CreateUserForm
from django.contrib import messages


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Cuenta creada por ' + user)
            return redirect('login')
    contexto = {'form':form }
    return render(request,'register.html', contexto)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request,'Credenciales incorrectas')
    contexto = { }
    return render(request,'login.html', contexto)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('/')


@login_required(login_url='login')
def crearPersona(request):
    if request.method == 'GET':
        form = PersonaForm()
        contexto = {
            'form':form 
        }
    else:
        form = PersonaForm(request.POST)
        contexto = {
            'form':form 
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'crear_persona.html',contexto) 
 
@login_required(login_url='login')
def inicio(request):
    personas = Persona.objects.all()
    contexto = {
        'personas':personas
    }
    print(personas)
    return render(request,'index.html',contexto)

@login_required(login_url='login')
def editarPersona(request,id):
    persona= Persona.objects.get(id= id)
    if request.method == 'GET':
        form = PersonaForm(instance=persona)
        contexto = {
            'form':form 
        }
    else:
        form = PersonaForm(request.POST, instance = persona)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'crear_persona.html',contexto)
    
@login_required(login_url='login')
def eliminarPersona(request,id):
    persona= Persona.objects.get(id= id)
    persona.delete()
    return redirect('index')
