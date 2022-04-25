from ..models import Unidade

def cadastrar_unidade(unidade):
    Unidade.objects.create(usuario=unidade.usuario, nome=unidade.nome, obs=unidade.obs )

def listar_unidades ():
    unidades = Unidade.objects.all()
    return unidades

def listar_unidade_id(id):
    unidade = Unidade.objects.get(id=id)
    return unidade

def editar_unidade(unidade, unidade_novo):
    # SQL Injection
    # with connection.cursor() as cursor:
    #     nome = "'Carlos' , email = 'ana@mail.com'"
    #     cursor.execute(f"UPDATE unidades_unidade SET nome={nome} WHERE id=2")
    unidade.usuario = unidade_novo.usuario   
    unidade.nome = unidade_novo.nome   
    unidade.obs = unidade_novo.obs
    unidade.save(force_update=True)
    

def remover_unidade(unidade):
    unidade.delete()