from django import forms
from django.contrib.auth.models import User
from ..models import Reagente, ItensAulaPratica
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

class ItensAulaPraticaForm(forms.ModelForm):
       
    class Meta:
        model = ItensAulaPratica
        fields = ['usuario', 'aulapratica_id', 'reagente', 'quant_reagente']       
        
        
class ItensAulaPraticaFormExcluir(forms.ModelForm):
    class Meta:
        model = ItensAulaPratica
        fields = ['usuario', 'aulapratica_id',  'reagente', 'quant_reagente']       
        
