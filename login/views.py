from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from utils.utils import login_excluded

# Create your views here.
def log(request):
    return render(request, "login/pages/login.html")

@login_excluded('teste:home')
def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            lname = user.last_name
            return render(request, 'teste/pages/home.html', context={
                'fname': fname.upper(),
                'lname': lname.upper(),
            })
        else:
            messages.error(request, "Usuário ou senha incorretos!")
            return redirect("login:signin")

    
    return render(request, "login/pages/signin.html")

@login_excluded('teste:home')
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")
        
        user = User.objects.create_user(username, email, password)
        user.first_name = fname
        user.last_name = lname

        user.save()

        messages.success(request, "Conta criada com sucesso!")

        return redirect("login:signin")

    return render(request, "login/pages/register.html")

def signout(request):
    logout(request)
    return redirect('login:signin')
