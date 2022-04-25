from django import forms
from ..models import Tombo


class TomboForm(forms.ModelForm):
       class Meta:
        model = Tombo
        fields = ['usuario', 'numero', 'descricao']


class TomboFormExcluir(forms.ModelForm):
    class Meta:
        model = Tombo
        fields = ['usuario', 'numero', 'descricao']
