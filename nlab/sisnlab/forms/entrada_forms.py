from django import forms
from django.contrib.auth.models import User
from ..models import Entrada, Fornecedor


class DateInput(forms.DateInput):
    input_type = 'date'      

class EntradaForm(forms.ModelForm):
       
    class Meta:
        model = Entrada
        fields = ['usuario', 'nf', 'fornecedor', 'data_cadastro', 'nf_foto', 'obs']  
        widgets = {
            'data_cadastro': DateInput()
        }        
        
        
class EntradaFormExcluir(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['usuario', 'nf', 'fornecedor', 'data_cadastro', 'nf_foto', 'obs']       
        
