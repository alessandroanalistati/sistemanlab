from ..models import Marca

def cadastrar_marca(marca):
    Marca.objects.create(usuario=marca.usuario, nome=marca.nome, obs=marca.obs )

def listar_marcas ():
    marcas = Marca.objects.all()
    return marcas

def listar_marca_id(id):
    marca = Marca.objects.get(id=id)
    return marca

def editar_marca(marca, marca_novo):
    # SQL Injection
    # with connection.cursor() as cursor:
    #     nome = "'Carlos' , email = 'ana@mail.com'"
    #     cursor.execute(f"UPDATE marcas_marca SET nome={nome} WHERE id=2")
    marca.nome = marca_novo.nome   
    marca.obs = marca_novo.obs
    marca.save(force_update=True)
    

def remover_marca(marca):
    marca.delete()