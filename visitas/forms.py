from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML, Row, Column, Div, Submit
from .models import *

class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = '__all__'
        exclude = ['familia',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
                HTML('<h1>Informações visita:</h1>'),
            Row(
                Div(
                'data',
                
                css_class='form-row form-div-info'
                ),
            ),
                HTML('<h1>Pedidos da visita: </h1>'),
            Row(
                Div(
                Field('pedidos'),
                css_class='form-row form-div-observacao'
                ),
            ),
                HTML('<h1>Observações sobre a visita: </h1>'),
            Row(
                Div(
                Field('observacao'),
                css_class='form-row form-div-observacao'
                ),
            ),
                HTML('<div class="form-buttons"><button class="form-button" type="submit">Criar nova visita</button></div>'),
        )

class ParticipantesForm(forms.ModelForm):
    participantes = forms.ModelMultipleChoiceField(queryset=User.objects.all(),widget=forms.SelectMultiple)
    class Meta:
        model = VisitaParticipantes
        exclude = ['visita']