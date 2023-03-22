from django.contrib import admin
from django.urls import include, path
from login import views


app_name = 'login'

urlpatterns = [
    path('register', views.register_superuser, name="register"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    
]

