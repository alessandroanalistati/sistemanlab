class Entrada():
    def __init__(self, usuario, nf, fornecedor, data_cadastro, nf_foto, obs):
        self.__usuario = usuario
        self.__nf = nf
        self.__fornecedor = fornecedor
        self.__data_cadastro = data_cadastro
        self.__nf_foto = nf_foto              
        self.__obs = obs   
          

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario 
          
    @property
    def nf(self):
        return self.__nf

    @nf.setter
    def nf(self, nf):
        self.__nf = nf    
    
    @property
    def fornecedor(self):
        return self.__fornecedor

    @fornecedor.setter
    def fornecedor(self, fornecedor):
        self.__fornecedor = fornecedor    

    @property
    def data_cadastro(self):
        return self.__data_cadastro

    @data_cadastro.setter
    def data_cadastro(self, data_cadastro):
        self.__data_cadastro = data_cadastro   

    @property
    def nf_foto(self):
        return self.__nf_foto

    @nf_foto.setter
    def nf_foto(self, nf_foto):
        self.__nf_foto = nf_foto   
               
    @property
    def obs(self):
        return self.__obs

    @obs.setter
    def obs(self, obs):
        self.__obs = obs
    