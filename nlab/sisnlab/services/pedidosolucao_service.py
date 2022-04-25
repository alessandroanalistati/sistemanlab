from ..models import PedidoSolucao
from ..models import ItensPedidoSolucao

def cadastrar_pedidosolucao(pedidosolucao):
    PedidoSolucao.objects.create(usuario=pedidosolucao.usuario, nome=pedidosolucao.nome, concentracao=pedidosolucao.concentracao, 
    data_producao=pedidosolucao.data_producao, unidade=pedidosolucao.unidade, quantidade=pedidosolucao.quantidade,
    status=pedidosolucao.status, sala=pedidosolucao.sala, armario=pedidosolucao.armario, 
    bancada=pedidosolucao.bancada, estante=pedidosolucao.estante, prateleira=pedidosolucao.prateleira, 
    gaveta=pedidosolucao.gaveta, obs=pedidosolucao.obs)    

def listar_pedidosolucoes ():
    pedidosolucoes = PedidoSolucao.objects.all()
    return pedidosolucoes

def listar_pedidosolucao_id(id):
    pedidosolucao = PedidoSolucao.objects.get(id=id)
    return pedidosolucao

def editar_pedidosolucao(pedidosolucao, pedidosolucao_novo):
    # SQL Injection
    # with connection.cursor() as cursor:
    #     nome = "'Carlos' , email = 'ana@mail.com'"
    #     cursor.execute(f"UPDATE pedidosolucoes_pedidosolucao SET nome={nome} WHERE id=2")
    pedidosolucao.usuario = pedidosolucao_novo.usuario   
    pedidosolucao.nome = pedidosolucao_novo.nome   
    pedidosolucao.concentracao = pedidosolucao_novo.concentracao    
    pedidosolucao.data_producao = pedidosolucao_novo.data_producao     
    pedidosolucao.unidade = pedidosolucao_novo.unidade     
    pedidosolucao.quantidade = pedidosolucao_novo.quantidade    
    pedidosolucao.status = pedidosolucao_novo.status   
    pedidosolucao.sala = pedidosolucao_novo.sala
    pedidosolucao.quantidade = pedidosolucao_novo.quantidade
    pedidosolucao.armario = pedidosolucao_novo.armario
    pedidosolucao.bancada = pedidosolucao_novo.bancada
    pedidosolucao.estante = pedidosolucao_novo.estante
    pedidosolucao.prateleira = pedidosolucao_novo.prateleira
    pedidosolucao.gaveta = pedidosolucao_novo.gaveta
    pedidosolucao.obs = pedidosolucao_novo.obs

    pedidosolucao.save(force_update=True)    

def remover_pedidosolucao(pedidosolucao):
    pedidosolucao.delete()

def visualizar_pedidosolucao(id):
    pedidosolucao = PedidoSolucao.objects.get(id=id)
    return pedidosolucao

