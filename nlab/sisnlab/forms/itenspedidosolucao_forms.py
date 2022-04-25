from django import forms
from django.contrib.auth.models import User
from ..models import Reagente, ItensPedidoSolucao
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

class ItensPedidoSolucaoForm(forms.ModelForm):
       
    class Meta:
        model = ItensPedidoSolucao
        fields = ['usuario', 'pedidosolucao_id', 'reagente',  'quantidade']       
        
        
class ItensPedidoSolucaoFormExcluir(forms.ModelForm):
    class Meta:
        model = ItensPedidoSolucao
        fields = ['usuario', 'pedidosolucao_id', 'reagente', 'quantidade']  
        
