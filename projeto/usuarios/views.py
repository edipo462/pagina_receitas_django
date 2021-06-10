from typing import Text
from django.db import reset_queries
from django.shortcuts import render

from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# Create your views here.

#funcao criada para criação do usuário na base com algumas validações
#para buscarmos as informações do formulario de login e senha, pegamos o metodo 'POST'
def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['name']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if not nome.strip():
            print('O campo nome não pode ficar em branco')
            return redirect('cadastro')
        if not email.strip():
            print('O campo email não pode ficar em branco')
            return redirect('cadastro')
        if senha != senha2:
            print('As senhas não são iguais')
            return redirect('cadastro')
        

        if User.objects.filter(email=email).exists():
            print("usuário ja existe na base")
            return redirect('cadastro')
    #para criar o usuário na base de dados utilizar a classe "User ()django.contrib.auth.models"
        usuario = User.objects.create_user(username=nome, email=email, password=senha)
        usuario.save
        print("usuario cadastrado")
        return redirect('login')    

    else:

        return render(request,'login/cadastro.html')

  
        

def login(request):

    if request.method == 'POST':
        
        email = request.POST ['email']
        senha = request.POST ['senha']
        
        
        if  User.objects.filter(email=email).exists():
            nome_recuperado = User.objects.filter(email=email).values_list('username', flat=True).get() #Trazendo da base de dados o usuário atrelado ao e-mail para ser utilizado na autenticação
            usuario = auth.authenticate(request, username=nome_recuperado, password=senha)
            if usuario is not None:
                auth.login(request, usuario)
                print('Login realizado com sucesso')
                
                print ("acesso liberado")
                return redirect('dashboard')
            

    return render(request, 'login/login.html')

def dashboard(request):

    if request.user.is_authenticated:

        return render (request, 'login/dashboard.html')
    else:
        return redirect ('index')

def logout(request):

    auth.logout(request)
    return redirect('index')