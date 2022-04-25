from django import forms
from django.contrib.auth.models import User
from ..models import Reagente, ItensSaida
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

class ItensSaidaForm(forms.ModelForm):
       
    class Meta:
        model = ItensSaida
        fields = ['usuario', 'saida_id', 'reagente', 'unidade', 'quantidade']       
        
        
class ItensSaidaFormExcluir(forms.ModelForm):
    class Meta:
        model = ItensSaida
        fields = ['usuario', 'saida_id', 'reagente', 'unidade', 'quantidade']       
