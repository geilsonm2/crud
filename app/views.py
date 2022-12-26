from django.shortcuts import render
from app.forms import CursosForm
# Create your views here.

def cadastro(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def form(request):
   data= {}
   data['form'] = CursosForm()
   return render(request, 'form.html', data)

def cursos(request):
    return render(request, 'cursos.html')

