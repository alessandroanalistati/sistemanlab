class Estante():
    def __init__(self, usuario, nome, sigla, tombo, sala, obs):
        self.__usuario = usuario
        self.__nome = nome
        self.__sigla = sigla
        self.__tombo = tombo
        self.__sala = sala
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
    def tombo(self):
        return self.__tombo

    @tombo.setter
    def tombo(self, tombo):
        self.__tombo = tombo    
    
    @property
    def sala(self):
        return self.__sala

    @sala.setter
    def sala(self, sala):
        self.__sala = sala
        
    @property
    def obs(self):
        return self.__obs

    @obs.setter
    def obs(self, obs):
        self.__obs = obs
