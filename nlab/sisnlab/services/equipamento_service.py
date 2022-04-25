from ..models import Equipamento

def cadastrar_equipamento(equipamento):
    Equipamento.objects.create(usuario=equipamento.usuario, nome=equipamento.nome, tombo=equipamento.tombo, marca=equipamento.marca, data_compra=equipamento.data_compra, 
            data_ultim_m=equipamento.data_ultim_m, origem=equipamento.origem, ficha_tec=equipamento.ficha_tec, especficacao_t=equipamento.especficacao_t, 
            calibragem=equipamento.calibragem, sala=equipamento.sala,  armario=equipamento.armario, bancada=equipamento.bancada, 
            estante=equipamento.estante, prateleira=equipamento.prateleira, gaveta=equipamento.gaveta, obs=equipamento.obs, foto=equipamento.foto)

def listar_equipamentos ():
    equipamentos = Equipamento.objects.all()
    return equipamentos

def listar_equipamento_id(id):
    equipamento = Equipamento.objects.get(id=id)
    return equipamento

def editar_equipamento(equipamento, equipamento_novo):
    # SQL Injection
    # with connection.cursor() as cursor:
    #     nome = "'Carlos' , email = 'ana@mail.com'"
    #     cursor.execute(f"UPDATE equipamentos_equipamento SET nome={nome} WHERE id=2")
    equipamento.usuario = equipamento_novo.usuario   
    equipamento.nome = equipamento_novo.nome   
    equipamento.tombo = equipamento_novo.tombo
    equipamento.marca = equipamento_novo.marca
    equipamento.data_compra = equipamento_novo.data_compra
    equipamento.data_ultim_m = equipamento_novo.data_ultim_m
    equipamento.origem = equipamento_novo.origem
    equipamento.ficha_tec = equipamento_novo.ficha_tec
    equipamento.especficacao_t = equipamento_novo.especficacao_t
    equipamento.calibragem = equipamento_novo.calibragem
    equipamento.sala = equipamento_novo.sala
    equipamento.armario = equipamento_novo.armario
    equipamento.bancada = equipamento_novo.bancada
    equipamento.estante = equipamento_novo.estante
    equipamento.prateleira = equipamento_novo.prateleira
    equipamento.gaveta = equipamento_novo.gaveta
    equipamento.obs = equipamento_novo.obs
    equipamento.foto = equipamento_novo.foto
    equipamento.save(force_update=True)
    

def remover_equipamento(equipamento):
    equipamento.delete()

def visualizar_equipamento(id):
    equipamento = Equipamento.objects.get(id=id)
    return equipamento