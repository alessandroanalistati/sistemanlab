from django import forms
from django.contrib.auth.models import User
from ..models import SolucaoAulaPratica
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

class SolucaoAulaPraticaForm(forms.ModelForm):
       
    class Meta:
        model = SolucaoAulaPratica
        fields = ['usuario', 'aulapratica_id', 'solucao', 'quant_solucao']       
        
        
class SolucaoAulaPraticaFormExcluir(forms.ModelForm):
    class Meta:
        model = SolucaoAulaPratica
        fields = ['usuario', 'aulapratica_id', 'solucao', 'quant_solucao']             
        
