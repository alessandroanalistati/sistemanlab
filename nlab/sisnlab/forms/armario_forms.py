from django import forms
from ..models import Armario, Sala

class ArmarioForm(forms.ModelForm):  
   
    class Meta:
        model = Armario
        fields = ['usuario','nome', 'sigla', 'tombo', 'sala', 'obs', 'fotoarmario']
       

class ArmarioFormExcluir(forms.ModelForm): 
    class Meta:
        model = Armario
        fields = ['usuario','nome', 'sigla', 'tombo', 'sala', 'obs', 'fotoarmario']