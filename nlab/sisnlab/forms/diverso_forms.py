from django import forms
from ..models import Diverso, Marca, Sala, Armario, Bancada, Estante, Prateleira, Gaveta, Unidade

class DiversoForm(forms.ModelForm):
       
    class Meta:
        model = Diverso
        fields = ['usuario', 'nome', 'marca', 'unidade', 'quantidade', 'ficha_tec', 'sala', 'armario',
                  'bancada', 'estante', 'prateleira', 'gaveta', 'obs', 'foto']

class DiversoFormExcluir(forms.ModelForm):
    class Meta:
        model = Diverso
        fields = ['usuario', 'nome', 'marca', 'unidade', 'quantidade', 'ficha_tec', 'sala', 'armario',
                  'bancada', 'estante', 'prateleira', 'gaveta', 'obs', 'foto']
