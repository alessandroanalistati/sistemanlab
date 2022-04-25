from ..models import Reagente

def cadastrar_reagente(reagente):
    Reagente.objects.create(usuario=reagente.usuario, nome=reagente.nome, formula_q=reagente.formula_q, grau_p=reagente.grau_p, unidade=reagente.unidade, 
    marca=reagente.marca, quantidade=reagente.quantidade, data_validade=reagente.data_validade, controle_pfex=reagente.controle_pfex,
    ficha_tec=reagente.ficha_tec, massamolecular=reagente.massamolecular, densidade=reagente.densidade, disponibilidade=reagente.disponibilidade, 
    sala=reagente.sala, armario=reagente.armario, bancada=reagente.bancada, estante=reagente.estante, prateleira=reagente.prateleira, 
    gaveta=reagente.gaveta, obs=reagente.obs, foto=reagente.foto)

def listar_reagentes ():
    reagentes = Reagente.objects.all()
    return reagentes

def listar_reagente_id(id):
    reagente = Reagente.objects.get(id=id)
    return reagente

def editar_reagente(reagente, reagente_novo):
    # SQL Injection
    # with connection.cursor() as cursor:
    #     nome = "'Carlos' , email = 'ana@mail.com'"
    #     cursor.execute(f"UPDATE reagentes_reagente SET nome={nome} WHERE id=2")
    reagente.usuario = reagente_novo.usuario   
    reagente.nome = reagente_novo.nome   
    reagente.formula_q = reagente_novo.formula_q    
    reagente.grau_p = reagente_novo.grau_p     
    reagente.unidade = reagente_novo.unidade     
    reagente.marca = reagente_novo.marca
    reagente.quantidade = reagente_novo.quantidade    
    reagente.data_validade = reagente_novo.data_validade
    reagente.controle_pfex = reagente_novo.controle_pfex 
    reagente.ficha_tec = reagente_novo.ficha_tec
    reagente.massamolecular = reagente_novo.massamolecular  
    reagente.disponibilidade = reagente_novo.disponibilidade   
    reagente.formula_q = reagente_novo.formula_q  
    reagente.sala = reagente_novo.sala
    reagente.quantidade = reagente_novo.quantidade
    reagente.armario = reagente_novo.armario
    reagente.bancada = reagente_novo.bancada
    reagente.estante = reagente_novo.estante
    reagente.prateleira = reagente_novo.prateleira
    reagente.gaveta = reagente_novo.gaveta
    reagente.obs = reagente_novo.obs
    reagente.foto = reagente_novo.foto

    reagente.save(force_update=True)    

def remover_reagente(reagente):
    reagente.delete()

def visualizar_reagente(id):
    reagente = Reagente.objects.get(id=id)
    return reagente