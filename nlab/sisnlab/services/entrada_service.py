from ..models import Entrada
from ..models import ItensEntrada

def cadastrar_entrada(entrada):
    Entrada.objects.create(usuario=entrada.usuario, nf=entrada.nf, fornecedor=entrada.fornecedor, 
    data_cadastro=entrada.data_cadastro, nf_foto=entrada.nf_foto, obs=entrada.obs )    

def listar_entradas ():
    entradas = Entrada.objects.all()
    return entradas

def listar_entrada_id(id):
    entrada = Entrada.objects.get(id=id)
    return entrada

def editar_entrada(entrada, entrada_novo):
    # SQL Injection
    # with connection.cursor() as cursor:
    #     nome = "'Carlos' , email = 'ana@mail.com'"
    #     cursor.execute(f"UPDATE entradas_entrada SET nome={nome} WHERE id=2")
    entrada.usuario = entrada_novo.usuario   
    entrada.nf = entrada_novo.nf  
    entrada.fornecedor = entrada_novo.fornecedor    
    entrada.data_cadastro = entrada_novo.data_cadastro     
    entrada.nf_foto = entrada_novo.nf_foto     
    entrada.obs = entrada_novo.obs    

    entrada.save(force_update=True)    

def remover_entrada(entrada):
    entrada.delete()

def visualizar_entrada(id):
    entrada = Entrada.objects.get(id=id)
    return entrada

