from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML, Row, Column, Div, Submit
from django.forms import DateInput
from django_select2.forms import Select2Widget
from .models import *

class EntregaForm(forms.ModelForm):
    class Meta:
        model = Entrega
        fields = '__all__'
        exclude = ['familia',]
        widgets = {
            'data_entrega': DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
                HTML('<h1>Data:</h1>'),
            Row(
                Div(
                'data_entrega',
                css_class='form-row form-single form-div-info'
                ),
            ),
                HTML('<div class="form-buttons"><button class="form-button" type="submit">Cadastrar nova entrega</button></div>'),
        )

class ItensForm(forms.ModelForm):
    item = forms.ModelChoiceField(
        label='',
        queryset=Item.objects.all(),
        widget=Select2Widget(attrs={'id': 'item-select'}),
        initial=None
    )

    class Meta:
        model = ItemEntrega
        fields = '__all__'
        exclude = ['entrega']
        labels = {
           'quantidade': " "
        }

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
            HTML('<div class="form-buttons"><button class="form-button" type="submit">Adicionar item a entrega</button></div>'),
        )

        self.helper.form_tag = False
