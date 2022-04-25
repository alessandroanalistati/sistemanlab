from django import forms
from ..models import Prateleira, Armario, Bancada, Estante

class PrateleiraForm(forms.ModelForm):

    class Meta:
        model = Prateleira
        fields = ['usuario', 'nome', 'sigla', 'armario', 'bancada', 'estante', 'obs']

class PrateleiraFormExcluir(forms.ModelForm):
    class Meta:
        model = Prateleira
        fields = ['usuario', 'nome', 'sigla', 'armario', 'bancada', 'estante', 'obs']