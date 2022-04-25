from ..models import Sala

def listar_salas():
    salas = Sala.objects.all()
    return salas

def listar_sala_id(id):
    sala = Sala.objects.get(id=id)
    return sala

def remover_sala(sala):
    sala.delete()

def cadastrar_sala(sala):
    Sala.objects.create(usuario=sala.usuario, nome=sala.nome, obs=sala.obs)

def editar_sala(sala, sala_nova):
    # SQL Injection
    # with connection.cursor() as cursor:
    #     nome = "'Carlos' , email = 'ana@mail.com'"
    #     cursor.execute(f"UPDATE salas_sala SET nome={nome} WHERE id=2")
    sala.usuario = sala_nova.usuario
    sala.nome = sala_nova.nome
    sala.obs = sala_nova.obs
    sala.save(force_update=True)
