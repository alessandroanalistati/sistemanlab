from ..models import Saida
from ..models import ItensSaida

def cadastrar_saida(saida):
    Saida.objects.create(usuario=saida.usuario, nf=saida.nf, destinatario=saida.destinatario, 
    data_cadastro=saida.data_cadastro, nf_foto=saida.nf_foto, obs=saida.obs )    

def listar_saidas ():
    saidas = Saida.objects.all()
    return saidas

def listar_saida_id(id):
    saida = Saida.objects.get(id=id)
    return saida

def editar_saida(saida, saida_novo):
    # SQL Injection
    # with connection.cursor() as cursor:
    #     nome = "'Carlos' , email = 'ana@mail.com'"
    #     cursor.execute(f"UPDATE saidas_saida SET nome={nome} WHERE id=2")
    saida.usuario = saida_novo.usuario   
    saida.nf = saida_novo.nf  
    saida.destinatario = saida_novo.destinatario    
    saida.data_cadastro = saida_novo.data_cadastro     
    saida.nf_foto = saida_novo.nf_foto     
    saida.obs = saida_novo.obs    

    saida.save(force_update=True)    

def remover_saida(saida):
    saida.delete()

def visualizar_saida(id):
    saida = Saida.objects.get(id=id)
    return saida

