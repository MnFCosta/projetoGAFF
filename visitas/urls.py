from django.contrib import admin
from django.urls import include, path
from visitas import views


app_name = 'visitas'

urlpatterns = [
    path('visita', views.visitas, name="visita"),
    path('cadastro_visita', views.cadastroVisita, name="cadastro_visita"),
    
]

