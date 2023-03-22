from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email:', max_length=100)
    senha = forms.CharField(widget=forms.PasswordInput())
    
class RegisterForm(forms.Form):
    nome = forms.CharField(label='Nome Completo', max_length=100, required=True)
    telefone = forms.CharField(label='Celular', max_length=100, required=False)
    rua = forms.CharField(label='Rua', max_length=100, required=False)
    bairro = forms.CharField(label='Bairro', max_length=100, required=False)
    numero_casa = forms.CharField(label='Numero da Casa', max_length=100, required=False)
    cidade = forms.CharField(label='Cidade', max_length=100, required=False)
    unidade_federativa = forms.CharField(label='Unidade Federativa', max_length=100, required=False)
    email = forms.EmailField(label='Email:', max_length=100)
    senha = forms.CharField(label='Sua senha', widget=forms.PasswordInput())
    senha_confirmar = forms.CharField(label='Confirme sua senha', widget=forms.PasswordInput())