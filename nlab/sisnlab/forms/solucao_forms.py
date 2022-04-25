from django import forms
from ..models import Solucao, Marca, Armario, Bancada, Estante, Prateleira, Gaveta, Sala

class SolucaoForm(forms.ModelForm):
       
    class Meta:
        model = Solucao
        fields = ['usuario', 'nome', 'quantidade', 'sala', 'armario', 'bancada', 'estante', 'prateleira', 'gaveta', 'obs']

class SolucaoFormExcluir(forms.ModelForm):
    class Meta:
        model = Solucao
        fields =  ['usuario', 'nome', 'quantidade', 'sala', 'armario', 'bancada', 'estante', 'prateleira', 'gaveta', 'obs']
