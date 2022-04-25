from ..models import AulaPratica
from ..models import ItensAulaPratica

def cadastrar_aulapratica(aulapratica):
    AulaPratica.objects.create(usuario=aulapratica.usuario, nome=aulapratica.nome, sala=aulapratica.sala, 
    data_inicio=aulapratica.data_inicio, horario_inicio=aulapratica.horario_inicio, horario_fim=aulapratica.horario_fim, 
    quantalunos=aulapratica.quantalunos, obs=aulapratica.obs, status=aulapratica.status)    

def listar_aulapraticas ():
    aulapraticas = AulaPratica.objects.all()
    return aulapraticas

def listar_aulapratica_id(id):
    aulapratica = AulaPratica.objects.get(id=id)
    return aulapratica

def editar_aulapratica(aulapratica, aulapratica_novo):
    # SQL Injection
    # with connection.cursor() as cursor:
    #     nome = "'Carlos' , email = 'ana@mail.com'"
    #     cursor.execute(f"UPDATE aulapraticas_aulapratica SET nome={nome} WHERE id=2")
    aulapratica.usuario = aulapratica_novo.usuario   
    aulapratica.nome = aulapratica_novo.nome   
    aulapratica.sala = aulapratica_novo.sala    
    aulapratica.data_inicio = aulapratica_novo.data_inicio     
    aulapratica.horario_inicio = aulapratica_novo.horario_inicio
    aulapratica.horario_fim = aulapratica_novo.horario_fim         
    aulapratica.quantalunos = aulapratica_novo.quantalunos    
    aulapratica.obs = aulapratica_novo.obs
    aulapratica.status= aulapratica_novo.status
    aulapratica.save(force_update=True)    

def remover_aulapratica(aulapratica):
    aulapratica.delete()

def visualizar_aulapratica(id):
    aulapratica = AulaPratica.objects.get(id=id)
    return aulapratica
