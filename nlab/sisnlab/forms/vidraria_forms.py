from django import forms
from ..models import Vidraria, Marca, Sala, Armario, Bancada, Estante, Prateleira, Gaveta

class VidrariaForm(forms.ModelForm):
       
    class Meta:
        model = Vidraria
        fields = ['usuario', 'nome', 'marca', 'data_compra', 'origem', 'ficha_tec', 'especficacao_t', 'quantidade',
     'sala', 'armario', 'bancada', 'estante', 'prateleira', 'gaveta', 'obs', 'foto']

class VidrariaFormExcluir(forms.ModelForm):
    class Meta:
        model = Vidraria
        fields = ['usuario', 'nome', 'marca', 'data_compra', 'origem', 'ficha_tec', 'especficacao_t', 'quantidade',
     'sala', 'armario', 'bancada', 'estante', 'prateleira', 'gaveta', 'obs', 'foto']