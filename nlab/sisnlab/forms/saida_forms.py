from django import forms
from django.contrib.auth.models import User
from ..models import Saida, Destinatario



class DateInput(forms.DateInput):
    input_type = 'date'      

class SaidaForm(forms.ModelForm):
       
    class Meta:
        model = Saida
        fields = ['usuario', 'nf', 'destinatario', 'data_cadastro', 'nf_foto', 'obs']       
        
        widgets = {
            'data_cadastro': DateInput()
        }   
        
        
class SaidaFormExcluir(forms.ModelForm):
    class Meta:
        model = Saida
        fields = ['usuario', 'nf', 'destinatario', 'data_cadastro', 'nf_foto', 'obs']       
        
