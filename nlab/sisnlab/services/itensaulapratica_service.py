from ..models import AulaPratica
from ..models import Reagente
from ..models import ItensAulaPratica
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def cadastrar_itensaulapratica(itensaulapratica):
    
    ItensAulaPratica.objects.create(usuario=itensaulapratica.usuario, aulapratica_id=itensaulapratica.aulapratica_id, 
    reagente=itensaulapratica.reagente, quant_reagente=itensaulapratica.quant_reagente  ) 

def num_aulapratica_id(id):
    aulapratica_id = ItensAulaPratica.objects.get(id=id)
    
    return aulapratica_id  


def remover_itensaulapratica_id(id):
    itensaulapratica_remover = ItensAulaPratica.objects.filter(id=id).delete()
    return itensaulapratica_remover


