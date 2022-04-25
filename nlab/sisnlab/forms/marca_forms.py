from django import forms
from ..models import Marca

class MarcaForm(forms.ModelForm):

    class Meta:
        model = Marca
        fields = ['usuario', 'nome', 'obs']

class MarcaFormExcluir(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['usuario', 'nome', 'obs']