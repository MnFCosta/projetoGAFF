from django.urls import path
from teste import views


app_name = 'teste'

urlpatterns = [
    path('', views.view),
    path('home/', views.view, name="home"),
]