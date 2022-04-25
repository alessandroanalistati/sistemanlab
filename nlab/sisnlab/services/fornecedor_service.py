from ..models import Fornecedor

def cadastrar_fornecedor(fornecedor):
    Fornecedor.objects.create(usuario=fornecedor.usuario, nome=fornecedor.nome, cnpj=fornecedor.cnpj, cpf=fornecedor.cpf,
        data_cadastro=fornecedor.data_cadastro, endereco=fornecedor.endereco, telefone=fornecedor.telefone, cel=fornecedor.cel, 
        email=fornecedor.email, obs=fornecedor.obs)
    
def listar_fornecedores ():
    fornecedores = Fornecedor.objects.all()
    return fornecedores

def listar_fornecedor_id(id):
    fornecedor = Fornecedor.objects.get(id=id)
    return fornecedor

def editar_fornecedor(fornecedor, fornecedor_novo):
    # SQL Injection
    # with connection.cursor() as cursor:
    #     nome = "'Carlos' , email = 'ana@mail.com'"
    #     cursor.execute(f"UPDATE fornecedores_fornecedor SET nome={nome} WHERE id=2")
    fornecedor.usuario = fornecedor_novo.usuario
    fornecedor.nome = fornecedor_novo.nome
    fornecedor.cnpj = fornecedor_novo.cnpj
    fornecedor.cpf = fornecedor_novo.cpf
    fornecedor.data_cadastro = fornecedor_novo.data_cadastro
    fornecedor.endereco = fornecedor_novo.endereco
    fornecedor.telefone = fornecedor_novo.telefone
    fornecedor.cel = fornecedor_novo.cel
    fornecedor.email = fornecedor_novo.email
    fornecedor.obs = fornecedor_novo.obs
    fornecedor.save(force_update=True)
    

def remover_fornecedor(fornecedor):
    fornecedor.delete()