from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML, Row, Column, Div, Submit
from django.contrib.auth.forms import AuthenticationForm

class ColaboradorEditForm(forms.Form):
    nome = forms.CharField(label='Nome Completo:', max_length=100, required=True)
    telefone = forms.CharField(label='Celular:', max_length=100, required=False)
    rua = forms.CharField(label='Rua:', max_length=100, required=False)
    bairro = forms.CharField(label='Bairro:', max_length=100, required=False)
    numero_casa = forms.CharField(label='Numero da Casa:', max_length=100, required=False)
    cidade = forms.CharField(label='Cidade:', max_length=100, required=False)
    unidade_federativa = forms.CharField(label='Unidade Federativa:', max_length=2, required=False)

    
    def __init__(self, *args, **kwargs,):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
                HTML('<h1>Dados pessoais:</h1>'),
            Row(
                Div(
                'nome',
                'telefone',
                css_class='form-row form-div-info'
                ),
            ),
                HTML('<h1>Endereço: </h1>'),
            Row(
                Div(
                'rua',
                'bairro',
                'numero_casa',
                'cidade',
                'unidade_federativa',
                css_class='form-row form-div-endereco'
                ),
            ),
                HTML('<div class="form-buttons"><button class="form-button" type="submit">Editar</button></div>'),
        )   