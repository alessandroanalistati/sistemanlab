from ..models import Estante

def cadastrar_estante(estante):
    Estante.objects.create(usuario=estante.usuario, nome=estante.nome, sigla=estante.sigla, tombo=estante.tombo, sala=estante.sala, obs=estante.obs )

def listar_estantes ():
    estantes = Estante.objects.all()
    return estantes

def listar_estante_id(id):
    estante = Estante.objects.get(id=id)
    return estante

def editar_estante(estante, estante_novo):
    # SQL Injection
    # with connection.cursor() as cursor:
    #     nome = "'Carlos' , email = 'ana@mail.com'"
    #     cursor.execute(f"UPDATE estantes_estante SET nome={nome} WHERE id=2")
    estante.usuario = estante_novo.usuario
    estante.nome = estante_novo.nome
    estante.sigla = estante_novo.sigla
    estante.tombo = estante_novo.tombo
    estante.sala = estante_novo.sala
    estante.obs = estante_novo.obs
    estante.save(force_update=True)
    

def remover_estante(estante):
    estante.delete()