from django import forms
from .models import *

class ComponenteForm(forms.ModelForm):
    class Meta:
        model = componenteFamilia
        fields = '__all__'
