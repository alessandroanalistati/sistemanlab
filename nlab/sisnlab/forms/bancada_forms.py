from django import forms
from ..models import Bancada, Sala


class BancadaForm(forms.ModelForm):    
    class Meta:
        model = Bancada
        fields = ['usuario', 'nome', 'sigla', 'tombo', 'sala', 'obs']

class BancadaFormExcluir(forms.ModelForm):
    class Meta:
        model = Bancada
        fields = ['usuario', 'nome', 'sigla', 'tombo', 'sala', 'obs']