class PedidoSolucao():
    def __init__(self, usuario, nome, concentracao, data_producao, unidade, quantidade, status, sala, armario, bancada, 
                 estante, prateleira, gaveta, obs):
        self.__usuario = usuario
        self.__nome = nome
        self.concentracao = concentracao
        self.__data_producao = data_producao
        self.__unidade= unidade              
        self.__quantidade = quantidade         
        self.__status = status         
        self.__sala = sala
        self.__armario = armario
        self.__bancada = bancada
        self.__estante = estante
        self.__prateleira = prateleira
        self.__gaveta = gaveta
        self.__obs = obs           

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario 
          
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome    
    
    @property
    def concetracao(self):
        return self.__concetracao

    @concetracao.setter
    def concetracao(self, concetracao):
        self.__concetracao = concetracao    

    @property
    def data_producao(self):
        return self.__data_producao

    @data_producao.setter
    def data_producao(self, data_producao):
        self.__data_producao = data_producao   

    @property
    def unidade(self):
        return self.__unidade

    @unidade.setter
    def unidade(self, unidade):
        self.__unidade = unidade   
        
    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade   

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status   
     
    @property
    def sala(self):
        return self.__sala

    @sala.setter
    def sala(self, sala):
        self.__sala = sala    

    @property
    def armario(self):
        return self.__armario

    @armario.setter
    def armario(self, armario):
        self.__armario = armario       

    @property
    def bancada(self):
        return self.__bancada

    @bancada.setter
    def bancada(self, bancada):
        self.__bancada = bancada

    @property
    def estante(self):
        return self.__estante

    @estante.setter
    def estante(self, estante):
        self.__estante = estante       

    @property
    def prateleira(self):
        return self.__prateleira
    @prateleira.setter
    def prateleira(self, prateleira):
        self.__prateleira = prateleira

    @property
    def gaveta(self):
        return self.__gaveta

    @gaveta.setter
    def gaveta(self, gaveta):
        self.__gaveta = gaveta
        
           
    @property
    def obs(self):
        return self.__obs

    @obs.setter
    def obs(self, obs):
        self.__obs = obs
    
