from django.contrib import admin
from .models import *

# Register your models here.
class DoadorAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'celular', 'bairro', 'rua', 'numero', 'cidade', 'unidade_federativa')
    list_display_links = ('id','nome', 'celular', 'bairro', 'rua', 'numero', 'cidade', 'unidade_federativa')
    search_fields = ('id','nome', 'celular', 'bairro', 'rua', 'numero', 'cidade', 'unidade_federativa')
    
admin.site.register(Doador, DoadorAdmin)