from ..models import Saida
from ..models import Reagente
from ..models import ItensSaida
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def cadastrar_itenssaida(itenssaida):    
    ItensSaida.objects.create(usuario=itenssaida.usuario, saida_id=itenssaida.saida_id, 
        reagente=itenssaida.reagente, unidade=itenssaida.unidade, quantidade=itenssaida.quantidade ) 

def num_saida_id(id):
    saida_id = ItensSaida.objects.get(id=id)
    
    return saida_id  
  