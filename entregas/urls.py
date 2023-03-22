from django.contrib import admin
from django.urls import include, path
from entregas import views


app_name = 'entregas'

urlpatterns = [
    path('entregas', views.entregas, name="entregas")
    

]