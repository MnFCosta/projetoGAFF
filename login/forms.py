from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email:', max_length=100)
    senha = forms.CharField(widget=forms.PasswordInput())
    
    