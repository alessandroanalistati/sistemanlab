from ..models import Gaveta

def cadastrar_gaveta(gaveta):
    Gaveta.objects.create(usuario=gaveta.usuario, nome=gaveta.nome, sigla=gaveta.sigla, armario=gaveta.armario, 
    bancada=gaveta.bancada, estante=gaveta.estante,  obs=gaveta.obs )

def listar_gavetas ():
    gavetas = Gaveta.objects.all()
    return gavetas

def listar_gaveta_id(id):
    gaveta = Gaveta.objects.get(id=id)
    return gaveta

def editar_gaveta(gaveta, gaveta_novo):
    # SQL Injection
    # with connection.cursor() as cursor:
    #     nome = "'Carlos' , email = 'ana@mail.com'"
    #     cursor.execute(f"UPDATE gavetas_gaveta SET nome={nome} WHERE id=2")
    gaveta.usuario = gaveta_novo.usuario
    gaveta.nome = gaveta_novo.nome
    gaveta.sigla = gaveta_novo.sigla 
    gaveta.armario = gaveta_novo.armario
    gaveta.bancada = gaveta_novo.bancada
    gaveta.estante = gaveta_novo.estante   
    gaveta.obs = gaveta_novo.obs
    gaveta.save(force_update=True)
    

def remover_gaveta(gaveta):
    gaveta.delete()