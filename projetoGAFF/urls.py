"""projetoGAFF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django_select2 import urls as select2_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('select2/', include(select2_urls)),
    path('', include('home.urls')),
    path('', include('login.urls')),
    path('', include('familias.urls')),
    path('', include('visitas.urls')),
    path('', include('colaboradores.urls')),
    path('', include('doacoes.urls')),
    path('', include('entregas.urls')),
    path('', include('estoque.urls')),
]   