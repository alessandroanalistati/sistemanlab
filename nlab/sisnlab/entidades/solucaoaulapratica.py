class SolucaoAulaPratica():
    def __init__(self, usuario, aulapratica_id, solucao, quant_solucao):
        self.__usuario = usuario
        self.__aulapratica_id = aulapratica_id        
        self.__solucao = solucao                   
        self.__quant_solucao = quant_solucao            

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario 
          
    @property
    def aulapratica_id(self):
        return self.__aulapratica_id

    @aulapratica_id.setter
    def aulapratica_id(self, aulapratica_id):
        self.__aulapratica_id = aulapratica_id             
    
    @property
    def solucao(self):
        return self.__solucao
    
    @solucao.setter
    def solucao(self, solucao):
        self.__solucao = solucao    

    @property
    def quant_solucao(self):
        return self.__quant_solucao

    @quant_solucao.setter
    def quant_solucao(self, quant_solucao):
        self.__quant_solucao = quant_solucao   
    