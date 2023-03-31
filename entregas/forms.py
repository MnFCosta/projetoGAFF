from django import forms
from .models import *

class EntregaForm(forms.ModelForm):
    class Meta:
        model = Entrega
        fields = '__all__'

class ItensForm(forms.ModelForm):
    class Meta:
        model = ItemEntrega
        fields = '__all__'
        exclude = ['entrega']