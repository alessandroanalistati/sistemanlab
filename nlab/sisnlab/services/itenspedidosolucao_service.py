from ..models import PedidoSolucao
from ..models import Reagente
from ..models import ItensPedidoSolucao
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def cadastrar_itenspedidosolucao(itenspedidosolucao):
    
    ItensPedidoSolucao.objects.create(usuario=itenspedidosolucao.usuario, pedidosolucao_id=itenspedidosolucao.pedidosolucao_id, 
        reagente=itenspedidosolucao.reagente, quantidade=itenspedidosolucao.quantidade ) 

def num_pedidosolucao_id(id):
    pedidosolucao_id = ItensPedidoSolucao.objects.get(id=id)
    
    return pedidosolucao_id  





