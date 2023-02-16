from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def login(request):
    return render(request, "login/pages/login.html")

def signin(request):
    return render(request, "login/pages/signin.html")

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
    pass
