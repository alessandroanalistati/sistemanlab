from ..models import Vidraria

def cadastrar_vidraria(vidraria):
    Vidraria.objects.create(usuario=vidraria.usuario, nome=vidraria.nome, marca=vidraria.marca, data_compra=vidraria.data_compra, 
            origem=vidraria.origem, ficha_tec=vidraria.ficha_tec, especficacao_t=vidraria.especficacao_t, 
            quantidade=vidraria.quantidade, sala=vidraria.sala,  armario=vidraria.armario, bancada=vidraria.bancada, 
            estante=vidraria.estante, prateleira=vidraria.prateleira, gaveta=vidraria.gaveta, obs=vidraria.obs, foto=vidraria.foto )

def listar_vidrarias ():
    vidrarias = Vidraria.objects.all()
    return vidrarias

def listar_vidraria_id(id):
    vidraria = Vidraria.objects.get(id=id)
    return vidraria

def editar_vidraria(vidraria, vidraria_novo):
    # SQL Injection
    # with connection.cursor() as cursor:
    #     nome = "'Carlos' , email = 'ana@mail.com'"
    #     cursor.execute(f"UPDATE vidrarias_vidraria SET nome={nome} WHERE id=2")
    vidraria.usuario = vidraria_novo.usuario      
    vidraria.nome = vidraria_novo.nome      
    vidraria.marca = vidraria_novo.marca
    vidraria.data_compra = vidraria_novo.data_compra    
    vidraria.origem = vidraria_novo.origem
    vidraria.ficha_tec = vidraria_novo.ficha_tec
    vidraria.especficacao_t = vidraria_novo.especficacao_t    
    vidraria.sala = vidraria_novo.sala
    vidraria.quantidade = vidraria_novo.quantidade
    vidraria.armario = vidraria_novo.armario
    vidraria.bancada = vidraria_novo.bancada
    vidraria.estante = vidraria_novo.estante
    vidraria.prateleira = vidraria_novo.prateleira
    vidraria.gaveta = vidraria_novo.gaveta
    vidraria.obs = vidraria_novo.obs
    vidraria.foto = vidraria_novo.foto

    vidraria.save(force_update=True)
    

def remover_vidraria(vidraria):
    vidraria.delete()

def visualizar_vidraria(id):
    vidraria = Vidraria.objects.get(id=id)
    return vidraria