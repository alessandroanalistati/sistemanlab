from django import forms
from django.contrib.auth.models import User
from ..models import Reagente, ItensEntrada
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

class ItensEntradaForm(forms.ModelForm):
       
    class Meta:
        model = ItensEntrada
        fields = ['usuario', 'entrada_id', 'reagente', 'unidade', 'quantidade']       
        
        
class ItensEntradaFormExcluir(forms.ModelForm):
    class Meta:
        model = ItensEntrada
        fields = ['usuario', 'entrada_id', 'reagente', 'unidade', 'quantidade']       
