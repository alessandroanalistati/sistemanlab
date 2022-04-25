from ..models import Tombo

def listar_tombos():
    tombos = Tombo.objects.all()
    return tombos

def listar_tombo_id(id):
    tombo = Tombo.objects.get(id=id)
    return tombo

def remover_tombo(tombo):
    tombo.delete()

def cadastrar_tombo(tombo):
    Tombo.objects.create(usuario=tombo.usuario, numero=tombo.numero, descricao=tombo.descricao)

def editar_tombo(tombo, tombo_novo):
    # SQL Injection
    # with connection.cursor() as cursor:
    #     nome = "'Carlos' , email = 'ana@mail.com'"
    #     cursor.execute(f"UPDATE tombos_tombo SET nome={nome} WHERE id=2")
    tombo.usuario = tombo_novo.usuario
    tombo.numero = tombo_novo.numero
    tombo.descricao = tombo_novo.descricao
    tombo.save(force_update=True)
