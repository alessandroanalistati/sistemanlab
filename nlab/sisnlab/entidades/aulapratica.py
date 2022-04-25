class AulaPratica():
    def __init__(self, usuario, nome, sala, data_inicio, horario_inicio, horario_fim, quantalunos, obs, status):
        self.__usuario = usuario
        self.__nome = nome
        self.__sala = sala
        self.__data_inicio = data_inicio
        self.__horario_inicio = horario_inicio
        self.__horario_fim = horario_fim                      
        self.quantalunos = quantalunos      
        self.__obs = obs           
        self.__status = status           

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
    def sala(self):
        return self.__sala

    @sala.setter
    def sala(self, sala):
        self.__sala = sala    

    @property
    def data_inicio(self):
        return self.__data_inicio

    @data_inicio.setter
    def data_inicio(self, data_inicio):
        self.__data_inicio = data_inicio   

    @property
    def horario_inicio(self):
        return self.__horario_inicio

    @horario_inicio.setter
    def horario_inicio(self, horario_inicio):
        self.__horario_inicio = horario_inicio   
        
        
    @property
    def horario_fim(self):
        return self.__horario_fim

    @horario_fim.setter
    def horario_fim(self, horario_fim):
        self.__horario_fim = horario_fim   
        
    @property
    def quantalunos(self):
        return self.__quantalunos

    @quantalunos.setter
    def quantalunos(self, quantalunos):
        self.__quantalunos = quantalunos   
               
    @property
    def obs(self):
        return self.__obs

    @obs.setter
    def obs(self, obs):
        self.__obs = obs
    
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status
    
