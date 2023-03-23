from django import forms
from .models import *

class DoacaoForm(forms.ModelForm):
    class Meta:
        model = Doacao
        fields = '__all__'

class ItensForm(forms.ModelForm):
    class Meta:
        model = ItemDoacao
        fields = '__all__'
        exclude = ['doacao']