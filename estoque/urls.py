from django.contrib import admin
from django.urls import include, path
from estoque import views


app_name = 'estoque'

urlpatterns = [
    path('estoque', views.estoque, name="estoque")
    

]