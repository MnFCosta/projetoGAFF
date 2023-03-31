from django.contrib import admin
from .models import *


# Register your models here.
class MovimentoAdmin(admin.ModelAdmin):
    list_display = ('id','item', 'quantidade', 'data_movimento', 'tipo', 'por')
    list_display_links = ('id','item', 'quantidade', 'data_movimento', 'tipo', 'por')
    search_fields = ('id','item', 'quantidade', 'data_movimento', 'tipo', 'por')

admin.site.register(Movimentacao, MovimentoAdmin)