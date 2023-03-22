from django.contrib import admin
from django.urls import include, path
from doacoes import views


app_name = 'doacoes'

urlpatterns = [
    path('doacoes', views.doacoes, name="doacoes")
    

]

