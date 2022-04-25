from ..models import Prateleira

def cadastrar_prateleira(prateleira):
    Prateleira.objects.create(usuario=prateleira.usuario, nome=prateleira.nome, sigla=prateleira.sigla, armario=prateleira.armario, 
    bancada=prateleira.bancada, estante=prateleira.estante,  obs=prateleira.obs )

def listar_prateleiras ():
    prateleiras = Prateleira.objects.all()
    return prateleiras

def listar_prateleira_id(id):
    prateleira = Prateleira.objects.get(id=id)
    return prateleira

def editar_prateleira(prateleira, prateleira_novo):
    # SQL Injection
    # with connection.cursor() as cursor:
    #     nome = "'Carlos' , email = 'ana@mail.com'"
    #     cursor.execute(f"UPDATE prateleiras_prateleira SET nome={nome} WHERE id=2")
    prateleira.usuario = prateleira_novo.usuario
    prateleira.nome = prateleira_novo.nome
    prateleira.sigla = prateleira_novo.sigla  
    prateleira.armario = prateleira_novo.armario
    prateleira.bancada = prateleira_novo.bancada
    prateleira.estante = prateleira_novo.estante
    prateleira.obs = prateleira_novo.obs
    prateleira.save(force_update=True)
    

def remover_prateleira(prateleira):
    prateleira.delete()