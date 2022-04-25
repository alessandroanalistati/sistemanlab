from ..models import Destinatario

def cadastrar_destinatario(destinatario):
    Destinatario.objects.create(usuario=destinatario.usuario, nome=destinatario.nome, cnpj=destinatario.cnpj, cpf=destinatario.cpf,
        data_cadastro=destinatario.data_cadastro, endereco=destinatario.endereco, telefone=destinatario.telefone, cel=destinatario.cel, 
        email=destinatario.email, obs=destinatario.obs)
    
def listar_destinatarios ():
    destinatarios = Destinatario.objects.all()
    return destinatarios

def listar_destinatario_id(id):
    destinatario = Destinatario.objects.get(id=id)
    return destinatario

def editar_destinatario(destinatario, destinatario_novo):
    # SQL Injection
    # with connection.cursor() as cursor:
    #     nome = "'Carlos' , email = 'ana@mail.com'"
    #     cursor.execute(f"UPDATE destinatarios_destinatario SET nome={nome} WHERE id=2")
    destinatario.usuario = destinatario_novo.usuario
    destinatario.nome = destinatario_novo.nome
    destinatario.cnpj = destinatario_novo.cnpj
    destinatario.cpf = destinatario_novo.cpf
    destinatario.data_cadastro = destinatario_novo.data_cadastro
    destinatario.endereco = destinatario_novo.endereco
    destinatario.telefone = destinatario_novo.telefone
    destinatario.cel = destinatario_novo.cel
    destinatario.email = destinatario_novo.email
    destinatario.obs = destinatario_novo.obs
    destinatario.save(force_update=True)
    

def remover_destinatario(destinatario):
    destinatario.delete()