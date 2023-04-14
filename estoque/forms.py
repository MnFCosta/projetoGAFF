from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML, Row, Column, Div, Submit
from .models import *

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        exclude = ['estoque_atual']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
                HTML('<h1>Novo item:</h1>'),
            Row(
                Div(
                'nome',
                'multiplicador', 
                'codigo_barras', 
                css_class='form-row form-div-info'
                ),
            ),
                 HTML('<h1>Observações sobre o item: </h1>'),
            Row(
                Div(
                Field('observacao'),
                css_class='form-row form-div-observacao'
                ),
            ),
                HTML('<div class="form-buttons"><button class="form-button" type="submit">Cadastrar novo item</button></div>'),
        )