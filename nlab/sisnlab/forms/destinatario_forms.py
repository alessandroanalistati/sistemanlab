from django import forms
from ..models import Destinatario

class DateInput(forms.DateInput):
    input_type = 'date'        

class DestinatarioForm(forms.ModelForm):  
   
    class Meta:
        model = Destinatario
        fields = ['usuario','nome', 'cnpj', 'cpf', 'data_cadastro', 'endereco', 'telefone', 'cel', 'email', 'obs']
        
        widgets = {
            'data_cadastro': DateInput()
        }    
    
       

class DestinatarioFormExcluir(forms.ModelForm): 
    class Meta:
        model = Destinatario
        fields = ['usuario','nome', 'cnpj', 'cpf', 'data_cadastro', 'endereco', 'telefone', 'cel', 'email', 'obs']