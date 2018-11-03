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