from django.contrib import admin
from django.urls import include, path
from colaboradores import views


app_name = 'doacoes'

urlpatterns = [
    path('', views.colaboradores, name="colaboradores")
    

]

