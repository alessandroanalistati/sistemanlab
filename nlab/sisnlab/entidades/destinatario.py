class Destinatario():
    def __init__(self, usuario, nome, cnpj, cpf, data_cadastro, endereco, telefone, cel, email, obs):
        self.__usuario = usuario
        self.__nome = nome
        self.__cnpj = cnpj
        self.__cpf = cpf
        self.__data_cadastro = data_cadastro
        self.__endereco = endereco
        self.__telefone = telefone         
        self.__cel = cel         
        self.__email = email         
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
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj
    
    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf    
    
    @property
    def data_cadastro(self):
        return self.__data_cadastro

    @data_cadastro.setter
    def data_cadastro(self, data_cadastro):
        self.__data_cadastro = data_cadastro
        
    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco
        
    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone 
           
    @property
    def cel(self):
        return self.__cel

    @cel.setter
    def cel(self, cel):
        self.__cel = cel
        
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email
        
    @property
    def obs(self):
        return self.__obs

    @obs.setter
    def obs(self, obs):
        self.__obs = obs