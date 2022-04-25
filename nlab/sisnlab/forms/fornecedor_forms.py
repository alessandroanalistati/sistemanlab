from django import forms
from ..models import Fornecedor

class DateInput(forms.DateInput):
    input_type = 'date'        
    

class FornecedorForm(forms.ModelForm):  
   
    class Meta:
        model = Fornecedor
        fields = ['usuario','nome', 'cnpj', 'cpf', 'data_cadastro', 'endereco', 'telefone', 'cel', 'email', 'obs']
        widgets = {
            'data_cadastro': DateInput()
        }    
       

class FornecedorFormExcluir(forms.ModelForm): 
    class Meta:
        model = Fornecedor
        fields = ['usuario','nome', 'cnpj', 'cpf', 'data_cadastro', 'endereco', 'telefone', 'cel', 'email', 'obs']