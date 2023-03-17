from django import forms
from .models import *

class ComponenteForm(forms.ModelForm):
    class Meta:
        model = componenteFamilia
        fields = '__all__'

class FamiliaForm(forms.ModelForm):
    composicao = forms.ModelMultipleChoiceField(queryset=componenteFamilia.objects.all(),widget=forms.SelectMultiple)


    class Meta:
        model = Familia
        fields = ['nome','rua','numero','bairro','cidade',
                  'unidade_federativa','latitude','longitude','cep',
                  'celular','moradia','casa_de','condicoes_casa','aluguel',
                  'data_cadastro','realizado_por','observacao']

    #override no metodo padrão save para poder tratar um multiselectfield
    def save(self, commit=True):
        #chama o método save padrão para criar uma instancia do model
        #porém commit=False para que a instancia nao seja salva na db
        instance = super().save(commit=False)
        if commit:
            instance.save()  # salva a instancia na db com valores para que ela tenha um id 
            #(necessário para salvar multiselectfield)
        instance.componentes.set(self.cleaned_data['composicao']) #coloca os dados do formulário no atributo componentes do model
        if commit:
            instance.save() #salva a instancia com todos os dados na db
        return instance
    
class   RendaForm(forms.ModelForm):
    class Meta:
        model = RendaFamiliar
        fields = '__all__'