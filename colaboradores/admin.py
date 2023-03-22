from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

class MyModelAdmin(admin.ModelAdmin):
    fields = ('nome', 'email', 'password', 'celular', 'rua', 'bairro', 'numero', 'cidade',
               'unidade_federativa', 'is_active', 'is_superuser', 'is_staff', 'data_de_ingresso', 'last_login', 'groups', 'user_permissions')
    
admin.site.register(User, MyModelAdmin)