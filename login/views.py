from django.http import HttpResponse
from django.shortcuts import redirect, render
""" from django.contrib.auth.models import User """
from colaboradores.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from utils.utils import login_excluded

# Create your views here.
def log(request):
    return render(request, "login/pages/login.html")

@login_excluded('teste:home')
def signin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(email=email, password=password)

        if user is not None:
            print(f"Seu nome é {user.nome}")
            login(request, user)
            if ' ' in user.nome:
                fname, lname = user.nome.split(' ', 1)
            else:
                fname = user.nome 
                lname = ""
            print(fname)
            print(lname)
            return render(request, 'teste/pages/home.html', context={
                'fname': fname,
                'lname': lname,
            })
        else:
            messages.error(request, "Usuário ou senha incorretos!")
            return redirect("login:signin")

    
    return render(request, "login/pages/signin.html")

# @login_excluded('teste:home')
def register_superuser(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        celular = request.POST.get("celular")
        rua = request.POST.get("rua")
        bairro = request.POST.get("bairro")
        numero_casa = request.POST.get("numero_casa")
        cidade = request.POST.get("cidade")
        unidade_federativa = request.POST.get("unidade_federativa")
        email = request.POST.get("email")
        senha = request.POST.get("password")
        cpassword = request.POST.get("cpassword")
        
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
            return redirect("teste:home")
        else:
            messages.error(request, "Senhas não são iguais!")
            return redirect("login:registerr")

    return render(request, "login/pages/register.html")

def teste(request):
    return render(request, "login/pages/login.html")

def signout(request):
    logout(request)
    return redirect('login:signin')
