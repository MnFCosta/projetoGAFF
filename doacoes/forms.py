from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML, Row, Column, Div, Submit
from .models import *

class DoacaoForm(forms.ModelForm):
    class Meta:
        model = Doacao
        fields = '__all__'
        exclude = ['data_doacao']

class DoadorForm(forms.ModelForm):
    class Meta:
        model = Doador
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML('<h1>Nome e Contato: </h1>'),
            Row(
                Div(
                    'nome',
                    'celular',
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
                    css_class='form-row form-div-info'
                ),
            ),
            HTML('<div class="form-buttons"><button class="form-button" type="submit">Criar novo doador</button></div>'),
        )

        self.helper.form_tag = False

class ItensForm(forms.ModelForm):
    class Meta:
        model = ItemDoacao
        fields = '__all__'
        exclude = ['doacao']

    item = forms.ModelChoiceField(
        queryset=Item.objects.all(),
        widget=forms.Select(attrs={'id': 'item-select'}),
        initial=None
    )

    def clean_quantidade(self):
        quantidade = self.cleaned_data['quantidade']
        if quantidade < 0:
            raise forms.ValidationError("Quantidade não pode ser negativa.")
        return quantidade

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['quantidade'].widget.attrs['id'] = 'quantidade-input'

        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML('<h1>Item: </h1>'),
            Row(
                Div(
                    'item',
                    css_class='form-row form-div-ajax'
                ),
                Div(
                    HTML('<span id="unidades">QTD em estoque: N/A</span>'),
                    css_class='form-row form-div-ajax'
                ),
                css_class='form-row-ajax'
            ),
            HTML('<h1>Quantidade: </h1>'),
            Row(
                Div(
                    'quantidade',
                    css_class='form-row form-div-endereco'
                ),
            ),
            HTML('<div class="form-buttons"><button class="form-button" type="submit">Adicionar item a doação</button></div>'),
        )

        self.helper.form_tag = False