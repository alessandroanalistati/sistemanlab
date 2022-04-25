from ..models import Armario

def cadastrar_armario(armario):
    Armario.objects.create(usuario=armario.usuario, nome=armario.nome, sigla=armario.sigla, tombo=armario.tombo, sala=armario.sala, 
    obs=armario.obs, fotoarmario=armario.fotoarmario )

def listar_armarios ():
    armarios = Armario.objects.all()
    return armarios

def listar_armario_id(id):
    armario = Armario.objects.get(id=id)
    return armario

def editar_armario(armario, armario_novo):
    # SQL Injection
    # with connection.cursor() as cursor:
    #     nome = "'Carlos' , email = 'ana@mail.com'"
    #     cursor.execute(f"UPDATE armarios_armario SET nome={nome} WHERE id=2")  

    
    armario.usuario = armario_novo.usuario
    armario.nome = armario_novo.nome
    armario.sigla = armario_novo.sigla
    armario.tombo = armario_novo.tombo
    armario.sala = armario_novo.sala
    armario.obs = armario_novo.obs
    armario.fotoarmario = armario_novo.fotoarmario
            
    armario.save(force_update=True)

def remover_armario(armario):
    armario.delete()