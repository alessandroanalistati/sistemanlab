from ..models import AulaPratica
from ..models import Reagente
from ..models import EquipamentosAulaPratica
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def cadastrar_equipamentosAulaPratica(equipamentosaulapratica):
    
    EquipamentosAulaPratica.objects.create(usuario=equipamentosaulapratica.usuario, aulapratica_id=equipamentosaulapratica.aulapratica_id, 
    equipamentos=equipamentosaulapratica.equipamentos, quant_equipamentos=equipamentosaulapratica.quant_equipamentos  ) 

def num_aulapratica_id(id):
    aulapratica_id = EquipamentosAulaPratica.objects.get(id=id)
    
    return aulapratica_id  



def remover_equipamentos_aula_id(id):
    equipamento_remover = EquipamentosAulaPratica.objects.filter(id=id).delete()
    return equipamento_remover




