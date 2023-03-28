from django.contrib import admin
from django.urls import include, path
from colaboradores import views


app_name = 'colaboradores'

urlpatterns = [
    path('colaboradores', views.colaboradores, name="colaboradores"),
    path('colaboradores/<int:id>', views.colaboradorDetail, name="colaborador_detail")
    

]

