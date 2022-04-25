from ..models import AulaPratica
from ..models import SolucaoAulaPratica
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def cadastrar_solucaoaulapratica(solucaoaulapratica):
    
    SolucaoAulaPratica.objects.create(usuario=solucaoaulapratica.usuario, aulapratica_id=solucaoaulapratica.aulapratica_id, 
    solucao=solucaoaulapratica.solucao, quant_solucao=solucaoaulapratica.quant_solucao  ) 

def num_aulapratica_id(id):
    aulapratica_id = SolucaoAulaPratica.objects.get(id=id)
    
    return aulapratica_id  


def remover_solucao_aula_id(id):
    solucao_remover = SolucaoAulaPratica.objects.filter(id=id).delete()
    return solucao_remover

