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
    """ def save(self, commit=True):
        #chama o método save padrão para criar uma instancia do model
        #porém commit=False para que a instancia nao seja salva na db
        instance = super().save(commit=False)
        if commit:
            instance.save()  # salva a instancia na db com valores para que ela tenha um id 
            #(necessário para salvar multiselectfield)
        instance.familia.set(id)
        instance.participantes.set(self.cleaned_data['participantes']) #coloca os dados do formulário no atributo componentes do model
        if commit:
            instance.save() #salva a instancia com todos os dados na db
        return instance """