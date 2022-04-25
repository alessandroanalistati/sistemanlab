from ..models import Solucao

def cadastrar_solucao(solucao):
    Solucao.objects.create(usuario=solucao.usuario, nome=solucao.nome, quantidade=solucao.quantidade, sala=solucao.sala,  armario=solucao.armario, bancada=solucao.bancada, 
            estante=solucao.estante, prateleira=solucao.prateleira, gaveta=solucao.gaveta, obs=solucao.obs)

def listar_solucoes ():
    solucoes = Solucao.objects.all()
    return solucoes

def listar_solucao_id(id):
    solucoes = Solucao.objects.get(id=id)
    return solucoes

def editar_solucao(solucao, solucao_novo):
    # SQL Injection
    # with connection.cursor() as cursor:
    #     nome = "'Carlos' , email = 'ana@mail.com'"
    #     cursor.execute(f"UPDATE solucoes_solucao SET nome={nome} WHERE id=2")
    solucao.usuario = solucao_novo.usuario   
    solucao.nome = solucao_novo.nome   
    solucao.quantidade = solucao_novo.quantidade  
    solucao.sala = solucao_novo.sala
    solucao.armario = solucao_novo.armario
    solucao.bancada = solucao_novo.bancada
    solucao.estante = solucao_novo.estante
    solucao.prateleira = solucao_novo.prateleira
    solucao.gaveta = solucao_novo.gaveta
    solucao.obs = solucao_novo.obs   

    solucao.save(force_update=True)
    

def remover_solucao(solucao):
    solucao.delete()
    
    

def visualizar_solucao(id):
    solucao = Solucao.objects.get(id=id)
    return solucao





