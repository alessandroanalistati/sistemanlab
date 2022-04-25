class Prateleira():
    def __init__(self, usuario, nome, sigla, armario, bancada, estante, obs):
        self.__usuario = usuario
        self.__nome = nome
        self.__sigla = sigla  
        self.__armario = armario 
        self.__bancada = bancada 
        self.__estante = estante         
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
    def sigla(self):
        return self.__sigla

    @sigla.setter
    def sigla(self, sigla):
        self.__sigla = sigla    
    
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
    def obs(self):
        return self.__obs

    @obs.setter
    def obs(self, obs):
        self.__obs = obs


