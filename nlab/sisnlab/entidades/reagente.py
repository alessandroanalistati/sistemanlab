class Reagente():
    def __init__(self, usuario, nome, formula_q, grau_p, unidade, marca, quantidade, data_validade, controle_pfex, ficha_tec, massamolecular,
     densidade, disponibilidade, sala, armario, bancada, estante, prateleira, gaveta, obs, foto):
        self.__usuario = usuario
        self.__nome = nome
        self.__formula_q = formula_q
        self.__grau_p = grau_p
        self.__unidade= unidade
        self.__marca = marca        
        self.__quantidade = quantidade
        self.__data_validade = data_validade
        self.__controle_pfex = controle_pfex
        self.__ficha_tec = ficha_tec
        self.__massamolecular = massamolecular
        self.__densidade = densidade
        self.__disponibilidade = disponibilidade
        self.__sala = sala
        self.__armario = armario
        self.__bancada = bancada
        self.__estante = estante
        self.__prateleira = prateleira
        self.__gaveta = gaveta
        self.__obs = obs    
        self.__foto = foto    

    
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
    def formula_q(self):
        return self.__formula_q

    @formula_q.setter
    def formula_q(self, formula_q):
        self.__formula_q = formula_q    

    @property
    def grau_p(self):
        return self.__grau_p

    @grau_p.setter
    def grau_p(self, grau_p):
        self.__grau_p = grau_p   

    @property
    def unidade(self):
        return self.__unidade

    @unidade.setter
    def unidade(self, unidade):
        self.__unidade = unidade    
    
    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca   
        
    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade       

    @property
    def data_validade(self):
        return self.__data_validade

    @data_validade.setter
    def data_validade(self, data_validade):
        self.__data_validade = data_validade   
    
    @property
    def controle_pfex(self):
        return self.__controle_pfex

    @controle_pfex.setter
    def controle_pfex(self, controle_pfex):
        self.__controle_pfex = controle_pfex     

    @property
    def ficha_tec(self):
        return self.__ficha_tec

    @ficha_tec.setter
    def ficha_tec(self, ficha_tec):
        self.__ficha_tec = ficha_tec
        
    @property
    def massamolecular(self):
        return self.__massamolecular

    @massamolecular.setter
    def massamolecular(self, massamolecular):
        self.__massamolecular = massamolecular    

    @property
    def densidade(self):
        return self.__densidade

    @densidade.setter
    def densidade(self, densidade):
        self.__densidade = densidade      

    @property
    def disponibilidade(self):
        return self.__disponibilidade

    @disponibilidade.setter
    def disponibilidade(self, disponibilidade):
        self.__disponibilidade = disponibilidade

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
        
        
    @property
    def foto(self):
        return self.__foto

    @foto.setter
    def foto(self, foto):
        self.__foto = foto
