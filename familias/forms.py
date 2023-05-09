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
                Field('papel'),
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
        widgets = {
            'aluguel': forms.TextInput(attrs={'placeholder': 'R$ 0,00'})
        }
        labels = {
            'aluguel': 'Valor do aluguel (opcional)',
            'numero': 'Numero da casa',
            'casa_de': 'Material da moradia:',
            'condicoes_casa': 'Condições da moradia:',
            'observacao': ''
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['aluguel'].required = False
        self.fields['data_cadastro'].widget = forms.HiddenInput()
        self.helper = FormHelper()
        self.helper.layout = Layout(
                HTML('<h1>Informações da familia:</h1>'),
            Row(
                Div(
                'nome',
                'celular',
                'data_cadastro',
                
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
                HTML('<div class="form-buttons"><button class="form-button" type="submit">Criar nova familia</button></div>'),
        )
    
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

class FamiliaEditForm(forms.ModelForm):
    class Meta:
        model = Familia
        fields = '__all__'
        exclude = ['componentes', 'realizado_por',]
        widgets = {
            'aluguel': forms.TextInput(attrs={'placeholder': 'R$ 0,00'})
        }
        labels = {
            'aluguel': 'Valor do aluguel (opcional)',
            'numero': 'Numero da casa',
            'casa_de': 'Material da moradia:',
            'condicoes_casa': 'Condições da moradia:',
            'observacao': ''
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = False
        self.fields['data_cadastro'].widget = forms.HiddenInput()
        self.helper = FormHelper()
        self.helper.layout = Layout(
                HTML('<h1>Informações da familia:</h1>'),
            Row(
                Div(
                'celular',
                'data_cadastro',
                
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
                HTML('<div class="form-buttons"><button class="form-button" type="submit">Atualizar familia</button></div>'),
        )
class ComponenteEditForm(forms.ModelForm):
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
                Field('papel'),
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
                HTML('<div class="form-buttons"><button class="form-button" type="submit">Atualizar componente familiar</button></div>'),
        )
class RendaEditForm(forms.ModelForm):
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
                HTML('<div class="form-buttons"><button class="form-button" type="submit">Atualizar renda familiar</button></div>'),
        )