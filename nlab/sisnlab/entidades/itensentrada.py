class ItensEntrada():
    def __init__(self, usuario, entrada_id, reagente, unidade, quantidade):
        self.__usuario = usuario
        self.__entrada_id = entrada_id
        self.__reagente = reagente        
        self.__unidade= unidade              
        self.__quantidade = quantidade         
        

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario 
          
    @property
    def entrada_id(self):
        return self.__entrada_id

    @entrada_id.setter
    def entrada_id(self, entrada_id):
        self.__entrada_id = entrada_id    
    
    @property
    def reagente(self):
        return self.__reagente

    @reagente.setter
    def reagente(self, reagente):
        self.__reagente = reagente    

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

    