from django.shortcuts import render
from .models import Region,Ciudad,Comuna,TipoUsuario,Estado,Mascota,Registro
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
def index (request):
    return render(request, 'index.html')

def formulario(request):
    return render(request,'formulario.html')

def page(request):
    return render(request,'page.html')

def mascota(request):
    return render(request,'Mascota.html')

def listar(request):
    return render(request,'listar.html')

def page2(request):
    return render(request,'page2.html')

def modificar(request):
    return render(request,'modificar.html')

def eliminar(request):
    return render(request,'eliminar.html')