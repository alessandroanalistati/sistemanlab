from ..models import Bancada

def cadastrar_bancada(bancada):
    Bancada.objects.create(usuario=bancada.usuario, nome=bancada.nome, sigla=bancada.sigla, tombo=bancada.tombo, sala=bancada.sala, obs=bancada.obs )

def listar_bancadas ():
    bancadas = Bancada.objects.all()
    return bancadas

def listar_bancada_id(id):
    bancada = Bancada.objects.get(id=id)
    return bancada

def editar_bancada(bancada, bancada_novo):
    # SQL Injection
    # with connection.cursor() as cursor:
    #     nome = "'Carlos' , email = 'ana@mail.com'"
    #     cursor.execute(f"UPDATE bancadas_bancada SET nome={nome} WHERE id=2")
    bancada.usuario = bancada_novo.usuario
    bancada.nome = bancada_novo.nome
    bancada.sigla = bancada_novo.sigla
    bancada.tombo = bancada_novo.tombo
    bancada.sala = bancada_novo.sala
    bancada.obs = bancada_novo.obs
    bancada.save(force_update=True)
    

def remover_bancada(bancada):
    bancada.delete()