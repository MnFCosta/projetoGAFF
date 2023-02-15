from django.contrib import admin
from django.urls import include, path
from login import views


app_name = 'login'

urlpatterns = [
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),

]

