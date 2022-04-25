class EquipamentosAulaPratica():
    def __init__(self, usuario, aulapratica_id, equipamentos, quant_equipamentos):
        self.__usuario = usuario
        self.__aulapratica_id = aulapratica_id        
        self.__equipamentos = equipamentos                   
        self.__quant_equipamentos = quant_equipamentos            

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
    def equipamentos(self):
        return self.__equipamentos
    
    @equipamentos.setter
    def equipamentos(self, equipamentos):
        self.__equipamentos = equipamentos    

    @property
    def quant_equipamentos(self):
        return self.__quant_equipamentos

    @quant_equipamentos.setter
    def quant_equipamentos(self, quant_equipamentos):
        self.__quant_equipamentos = quant_equipamentos   
    