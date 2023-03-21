from django import forms
from .models import *

class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = '__all__'

class ParticipantesForm(forms.ModelForm):
    participantes = forms.ModelMultipleChoiceField(queryset=User.objects.all(),widget=forms.SelectMultiple)
    class Meta:
        model = VisitaParticipantes
        exclude = ['visita']