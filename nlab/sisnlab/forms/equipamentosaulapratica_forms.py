from django import forms
from django.contrib.auth.models import User
from ..models import Reagente, EquipamentosAulaPratica
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

class EquipamentosAulaPraticaForm(forms.ModelForm):
       
    class Meta:
        model = EquipamentosAulaPratica
        fields = ['usuario', 'aulapratica_id', 'equipamentos', 'quant_equipamentos']       
        
        
class EquipamentosAulaPraticaFormExcluir(forms.ModelForm):
    class Meta:
        model = EquipamentosAulaPratica
        fields = ['usuario', 'aulapratica_id', 'equipamentos', 'quant_equipamentos']             
        
