from django.shortcuts import render, redirect
from app.forms import CursosForm
from app.models import Cursos
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
    data = {}
    data['db'] = Cursos.objects.all()
    return render(request, 'cursos.html', data)

def create(request):
    form = CursosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cursos')

def edit(request, pk):
    data = {}
    data['db'] = Cursos.objects.get(pk=pk)
    data['form'] = CursosForm(instance=data['db'])
    return render(request, 'form.html', data)    

def update(request, pk):
    data = {}
    data['db'] = Cursos.objects.get(pk=pk) #Pegamos os dados que estão vindo
    form = CursosForm(request.POST or None, instance=data['db']) #Chamamos o request.POST, com uma instancia realizando o update em um id especifico
    if form.is_valid():#Validamos o formulário
        form.save()
        return redirect('cursos') #Salvamos o formulário e reencaminhamos para página de cursos

def delete (request, pk):
    db = Cursos.objects.get(pk=pk)
    db.delete()
    return redirect('cursos')
