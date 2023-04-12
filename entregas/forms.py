from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML, Row, Column, Div, Submit
from django.urls import reverse
from .models import *

class EntregaForm(forms.ModelForm):
    class Meta:
        model = Entrega
        fields = '__all__'

class ItensForm(forms.ModelForm):
    item = forms.ModelChoiceField(
        queryset=Item.objects.all(),
        widget=forms.Select(attrs={'id': 'item-select'})
    )
    
    class Meta:
        model = ItemEntrega
        fields = '__all__'
        exclude = ['entrega']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML('<h1>Item: </h1>'),
            Row(
                Div(
                    'item',
                    css_class='form-row form-div-info'
                ),
            ),
            Row(
                Div(
                    HTML('<span id="unidades"></span>'),
                    css_class='form-row form-div-info'
                ),
            ),
            HTML('<h1>Quantidade: </h1>'),
            Row(
                Div(
                    'quantidade',
                    css_class='form-row form-div-endereco'
                ),
            ),
            HTML('<div class="form-buttons"><button class="form-button" type="submit">Criar Perfil</button></div>'),
        )