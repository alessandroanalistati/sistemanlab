from ..models import Entrada
from ..models import Reagente
from ..models import ItensEntrada
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def cadastrar_itensentrada(itensentrada):    
    ItensEntrada.objects.create(usuario=itensentrada.usuario, entrada_id=itensentrada.entrada_id, 
        reagente=itensentrada.reagente, unidade=itensentrada.unidade, quantidade=itensentrada.quantidade ) 

def num_entrada_id(id):
    entrada_id = ItensEntrada.objects.get(id=id)
    
    return entrada_id  
  