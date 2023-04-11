from django.http import HttpResponse
from django.shortcuts import redirect, render
""" from django.contrib.auth.models import User """
from colaboradores.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from utils.utils import login_excluded
from .forms import *

# Create your views here.
@login_excluded('home:home')
def signin(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('senha')
            user = authenticate(email=email, password=password)

            if user is not None:
                login(request, user)
                if ' ' in user.nome:
                    fname, lname = user.nome.split(' ', 1)
                else:
                    fname = user.nome 
                    lname = ""
                return render(request, 'home/pages/home.html', context={
                    'fname': fname,
                    'lname': lname,
                })
            else:
                messages.error(request, "Usuário ou senha incorretos!")
                return redirect("login:signin")  
    else:
        form = LoginForm()
        
    return render(request, "login/pages/signin.html", {'form': form})

# @login_excluded('home:home')
def register_superuser(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():   
            nome = form.cleaned_data.get("nome")
            celular = form.cleaned_data.get("telefone")
            rua = form.cleaned_data.get("rua")
            bairro = form.cleaned_data.get("bairro")
            numero_casa = form.cleaned_data.get("numero_casa")
            cidade = form.cleaned_data.get("cidade")
            unidade_federativa = form.cleaned_data.get("unidade_federativa")
            email = form.cleaned_data.get("email")
            senha = form.cleaned_data.get("senha")
            cpassword = form.cleaned_data.get("senha_confirmar")
            
            if cpassword == senha:
                user = User.objects.create_superuser(email, senha)
                user.nome = nome
                user.celular = celular
                user.rua = rua
                user.bairro = bairro
                user.numero = numero_casa
                user.cidade = cidade
                user.unidade_federativa = unidade_federativa
                user.save()
                messages.success(request, "Novo técnico cadastrado!")
                return redirect("home:home")
            else:
                messages.error(request, "Senhas não são iguais!")
                return redirect("login:register")
    else:
        form = RegisterForm()

    return render(request, "login/pages/register.html", {'form': form})

def signout(request):
    logout(request)
    return redirect('login:signin')
