from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from ..models import AulaPratica, Reagente, Marca, Sala, Unidade
from django import forms
from datetime import date
 


class DateInput(forms.DateInput):
    input_type = 'date'        
    
    

class AulaPraticaForm(forms.ModelForm):
       
    class Meta:
        model = AulaPratica
        fields = ['usuario', 'nome', 'sala', 'data_inicio', 'horario_inicio', 'horario_fim', 'quantalunos', 'obs', 'status']  
        
        
        widgets = {
            'data_inicio': DateInput()
        }    
    
             
        
        
class AulaPraticaFormExcluir(forms.ModelForm):
    class Meta:
        model = AulaPratica
        fields = ['usuario', 'nome', 'sala', 'data_inicio', 'horario_inicio', 'horario_fim', 'quantalunos', 'obs', 'status']    
        
        
