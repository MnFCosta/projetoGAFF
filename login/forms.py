from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML, Row, Column, Div, Submit
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(forms.Form):
    email = forms.EmailField(label='',max_length=100, required=True, widget=forms.EmailInput(attrs={'class': 'email-input'}))
    senha = forms.CharField(label='',widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('email')
        )
        self.fields['email'].label_class = 'my-custom-class'


class RegisterForm(forms.Form):
    nome = forms.CharField(label='Nome Completo:', max_length=100, required=True)
    telefone = forms.CharField(label='Celular:', max_length=100, required=False)
    rua = forms.CharField(label='Rua:', max_length=100, required=False)
    bairro = forms.CharField(label='Bairro:', max_length=100, required=False)
    numero_casa = forms.CharField(label='Numero da Casa:', max_length=100, required=False)
    cidade = forms.CharField(label='Cidade:', max_length=100, required=False)
    unidade_federativa = forms.CharField(label='Unidade Federativa:', max_length=2, required=False)
    email = forms.EmailField(label='Email:', max_length=100)
    senha = forms.CharField(label='Sua senha:', widget=forms.PasswordInput())
    senha_confirmar = forms.CharField(label='Confirme sua senha:', widget=forms.PasswordInput())

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
                HTML('<h1>Dados Pessoais:</h1>'),
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
                HTML('<h1>Credencias Login: </h1>'),
            Row(
                Div(
                Field('email', autocomplete='off'),
                Field('senha', autocomplete='off'),
                Field('senha_confirmar', autocomplete='off'),
                css_class='form-row form-div-credenciais'
                ),
            ),
                HTML('<div class="form-buttons"><button class="form-button" type="submit">Criar Perfil</button></div>'),
        )   