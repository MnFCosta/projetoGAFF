from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML, Row, Column, Div, Submit
from .models import *

class ComponenteForm(forms.ModelForm):
    class Meta:
        model = componenteFamilia
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
                HTML('<h1>Informações da pessoa:</h1>'),
            Row(
                Div(
                'nome',
                'cpf',
                'rg',
                'papel',
                'nascimento',
                
                css_class='form-row form-div-info'
                ),
            ),
                HTML('<h1>Informação Vestimentas:</h1>'),
            Row(
                Div(
                'NR_roupa',    
                'NR_calcado',
                css_class='form-row form-div-info'
                ),
            ),
                HTML('<div class="form-buttons"><button class="form-button" type="submit">Cadastrar componente familiar</button></div>'),
        )

class FamiliaForm(forms.ModelForm):
    class Meta:
        model = Familia
        fields = '__all__'
        exclude = ['componentes', 'realizado_por',]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
                HTML('<h1>Informações da familia:</h1>'),
            Row(
                Div(
                'nome',
                'celular',
                
                css_class='form-row form-div-info'
                ),
            ),
                HTML('<h1>Situação da Moradia:</h1>'),
            Row(
                Div(
                'moradia',    
                'casa_de',
                'condicoes_casa',
                'aluguel',
                css_class='form-row form-div-info'
                ),
            ),
                HTML('<h1>Endereço: </h1>'),
            Row(
                Div(
                'rua',
                'bairro',
                'numero',
                'cidade',
                'unidade_federativa',
                css_class='form-row form-div-endereco'
                ),
            ),
               HTML('<h1>Localização: </h1>'),
            Row(
                Div(
                Field('latitude'),
                Field('longitude'),
                Field('cep'),
                css_class='form-row form-div-credenciais'
                ),
            ),
                HTML('<h1>Observações sobre a familia: </h1>'),
            Row(
                Div(
                Field('observacao'),
                css_class='form-row form-div-observacao'
                ),
            ),
                HTML('<div class="form-buttons"><button class="form-button" type="submit">Criar Perfil</button></div>'),
        )
        
    """ #override no metodo padrão save para poder tratar um multiselectfield
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
        return instance """
    
class RendaForm(forms.ModelForm):
    class Meta:
        model = RendaFamiliar
        fields = '__all__'
        exclude = ['familia',]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
                HTML('<h1>Renda:</h1>'),
            Row(
                Div(
                'origem_renda',
                'valor', 
                css_class='form-row form-div-info'
                ),
            ),
                HTML('<div class="form-buttons"><button class="form-button" type="submit">Cadastrar renda familiar</button></div>'),
        )