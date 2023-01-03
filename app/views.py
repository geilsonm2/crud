from django.shortcuts import render, redirect
from app.forms import CursosForm
from app.models import Cursos
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

#CADASTRO E LOGIN
def home(request): #Home / Index / Chamando MAIN
    return render(request, 'painel.html') 


def create(request): #Formulário de Cadastro
    return render(request, 'create.html')

def store(request): #Inserção de dados dos Usuários ao Banco
    # campos = {
    #     'name' : 'Preencha o campo nome',
    #     'user' : 'Preencha o campo de usuário',
    #     'password': 'Preencha o campo de senha',
    #     'password-conf': 'Confirme a senha',
    #     'email' : 'email'
    # }

    # for campo, msg in campos.items():
    #     if campo not in request.POST or request.POST[campo] == '':
    #         data = {
    #             'msg' : msg,
    #             'class' : 'alert-danger'
    #         }

    #         return render(request, 'create.html', data)
    data = {} #user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    if (request.POST['password'] != request.POST['password-conf']):
        data ['msg'] = 'Senhas divergentes!'
        data ['class'] = 'alert-danger'
    else: 
        user = User.objects.create_user(request.POST['name'],request.POST['email'],request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        data ['msg'] = 'Usuário cadastrado com sucesso!'
        data ['class'] = 'alert-success' 
    return render(request, 'create.html', data)



def painel(request): #Formulário painel do login
    return render(request, 'painel.html')



def dologin(request): #Formulário painel do login
    data = {}
    user = authenticate(username= request.POST['user'], password= request.POST['password'])
    if user is not None:
       login(request, user)
       return redirect('/cursos/')
    else:
        data ['msg'] = 'Usuário ou senha Inválidos!'
        data ['class'] = 'alert-primary'
        return render(request, 'painel.html', data)


def dashboard(request):
    return render(request, 'dashboard/home.html')

def logouts(request):
    logout(request)
    return redirect('/painel/')

#Alterar Senha
def password(request):
    # user = User.objects.get(email=request.user.email)
    # user.set_password('new password')
    # user.save()
    # logout(request)
    return render(request, 'changePassword.html')

def changePassword (request):
     user = User.objects.get (email=request.POST['email'])
     user.set_password(request.POST['password'])
     user.save()
     logout(request)
     return redirect('/painel/')
    

#CADASTRO DE CURSOS
def form(request):
   data= {}
   data['form'] = CursosForm()
   return render(request, 'form.html', data)

def cursos(request):
    data = {}
    data['db'] = Cursos.objects.all()
    return render(request, 'cursos.html', data)

def createCursos(request):
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




