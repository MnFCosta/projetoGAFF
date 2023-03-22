from django.urls import path
from home import views


app_name = 'home'

urlpatterns = [
    path('', views.view),
    path('home/', views.view, name="home"),
]