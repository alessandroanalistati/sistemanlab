from django import forms
from ..models import Sala


class SalaForm(forms.ModelForm):
       class Meta:
        model = Sala
        fields = ['usuario', 'nome', 'obs']


class SalaFormExcluir(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['usuario', 'nome', 'obs']
