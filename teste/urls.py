from django.urls import path
from teste import views


app_name = 'teste'

urlpatterns = [
    path('home/', views.view, name="home"),
]