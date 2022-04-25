from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

       
class Sala(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL,  null=True, blank=True, verbose_name="Sala_Usuário  :" )    
    nome = models.CharField(max_length=80,  unique=True, null=False, blank=False, verbose_name="Nome :")
    obs = models.TextField(verbose_name="Observação", blank=True)

    def __str__(self):
        return self.nome

class Tombo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="UsuarioTombo :" ) 
    numero = models.CharField(max_length=6, unique=True, null=False, blank=False, verbose_name="Número :" )
    descricao = models.TextField(verbose_name="Observação", blank=False, null=False )    

    def __str__(self):
        return self.numero + ' - ' + self.descricao

class Armario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL,  null=True, blank=True, verbose_name="Armario_Usuário  :" )    
    nome = models.CharField(max_length=100, null=False, blank=False, verbose_name="Nome :")
    sigla = models.CharField(max_length=50, null=True, blank=True, verbose_name="SIGLA :")
    tombo = models.OneToOneField(Tombo, on_delete=models.SET_NULL, null=True, related_name='Tombo_Armario')    
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT, null=False, blank=True, related_name='Sala_Armário')
    obs = models.TextField(verbose_name="Observação", blank=True)
    fotoarmario = models.ImageField(upload_to='imagens', null=True, blank=True,  default='imagens\campus_itapetinga.png', verbose_name="Foto_Armario")  

    class Meta:
        verbose_name = u'Modelo'
        verbose_name_plural = u'Armários'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Estante(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL,  null=True, blank=True, verbose_name="Estante_Usuário :" )  
    nome = models.CharField(max_length=100, null=False, blank=False, verbose_name="Nome :")
    sigla = models.CharField(max_length=50, null=True, blank=True, verbose_name="SIGLA :")
    tombo = models.OneToOneField(Tombo, on_delete=models.SET_NULL, null=True, related_name='Tombo_Estante')    
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT, null=False, related_name='Sala_Estante')
    obs = models.TextField(verbose_name="Observação", null=True, blank=True)

    class Meta:
        verbose_name = u'Modelo'
        verbose_name_plural = u'Estantes'
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Bancada(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL,  null=True, blank=True, verbose_name="Bancada_Usuário :" ) 
    nome = models.CharField(max_length=100, blank=False, null=False, verbose_name="Nome :")
    sigla = models.CharField(max_length=50, null=True, blank=True, verbose_name="SIGLA :")
    tombo = models.OneToOneField(Tombo, on_delete=models.SET_NULL, null=True, blank=True, related_name='Tombo_Bancada')    
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT, null=False, related_name='Sala_Bancada')
    obs = models.TextField(verbose_name="Observação", blank=True)

    class Meta:
        verbose_name = u'Modelo'
        verbose_name_plural = u'Bancadas'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Prateleira(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL,  null=True, blank=True, verbose_name="Prateleira_Usuário  :" ) 
    nome = models.CharField(max_length=100, null=False, verbose_name="Nome :")
    sigla = models.CharField(max_length=50, null=True, blank=True, verbose_name="SIGLA :") 
    armario = models.ForeignKey(Armario, on_delete=models.SET_NULL, null=True, blank=True, related_name='Prateleira_Armario')
    bancada = models.ForeignKey(Bancada, on_delete=models.SET_NULL, null=True, blank=True, related_name='Prateleira_bancada')
    estante = models.ForeignKey(Estante, on_delete=models.SET_NULL, null=True, blank=True, related_name='Prateleira_prateleira')    
    obs = models.TextField(verbose_name="Observação", null=True, blank=True)

    class Meta:
        verbose_name = u'Modelo'
        verbose_name_plural = u'Prateleira'
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Gaveta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL,  null=True, blank=True, verbose_name="Gaveta_Usuário  :" ) 
    nome = models.CharField(max_length=100, null=False, verbose_name="Nome :")
    sigla = models.CharField(max_length=50, null=True, blank=True, verbose_name="SIGLA :") 
    armario = models.ForeignKey(Armario, on_delete=models.SET_NULL, null=True, blank=True, related_name='Gaveta_Armario')
    bancada = models.ForeignKey(Bancada, on_delete=models.SET_NULL, null=True, blank=True, related_name='Gaveta_bancada')
    estante = models.ForeignKey(Estante, on_delete=models.SET_NULL, null=True, blank=True, related_name='Gaveta_prateleira')       
    obs = models.TextField(verbose_name="Observação", null=True, blank=True)

    class Meta:
        verbose_name = u'Modelo'
        verbose_name_plural = u'Gaveta'
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Marca(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL,  null=True, blank=True, verbose_name="Marca_Usuário :" ) 
    nome = models.CharField(max_length=100, unique=True, null=False, verbose_name="Nome :")      
    obs = models.TextField(verbose_name="Observação", null=True, blank=True)

    class Meta:
        verbose_name = u'Modelo'
        verbose_name_plural = u'Gaveta'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Unidade(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL,  null=True, blank=True, verbose_name="Unidade_Usuário :" ) 
    nome = models.CharField(max_length=100, unique=True, null=False, verbose_name="Nome :")    
    obs = models.TextField(verbose_name="Observação", null=True, blank=True)

    class Meta:
        verbose_name = u'Modelo'
        verbose_name_plural = u'Gaveta'
        ordering = ['nome']

    def __str__(self):
        return self.nome    
    
    
class Equipamento(models.Model):
    CALIB_CHOICES = (
        ("SIM", "SIM"),
        ("NAO", "NÃO"),
    )
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL,  null=True, blank=True, verbose_name="Prateleira_Usuario :" ) 
    nome = models.CharField(max_length=200, null=False, verbose_name="Nome :")
    tombo = models.OneToOneField(Tombo, on_delete=models.SET_NULL, null=True, related_name='Equipamento_tombo')   
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name='Equipamento_Marca')
    data_compra =  models.DateTimeField(default=timezone.now)
    data_ultim_m =  models.DateTimeField(default=timezone.now) 
    origem = models.FileField(upload_to='pdf', null=False, default='imagens\campus_itapetinga.png', blank=True, verbose_name="Anexar PDF:")
    ficha_tec = models.FileField(upload_to='ficha_tec', null=False, blank=True,  default='imagens\campus_itapetinga.png', verbose_name="Ficha Técnica :")
    especficacao_t = models.TextField(null=False, blank=True, verbose_name="Especificação Técnica")
    calibragem = models.CharField(max_length=3, null=False, blank=True, choices=CALIB_CHOICES)    
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT, null=False, related_name='Equipamento_Sala')
    armario = models.ForeignKey(Armario, on_delete=models.SET_NULL, null=True, blank=True, related_name='Equipamento_Armario')
    bancada = models.ForeignKey(Bancada, on_delete=models.SET_NULL, null=True, blank=True, related_name='Equipamento_bancada')
    estante = models.ForeignKey(Estante, on_delete=models.SET_NULL, null=True, blank=True, related_name='Equipamento_prateleira') 
    prateleira = models.ForeignKey(Prateleira, on_delete=models.SET_NULL, null=True, blank=True, related_name='Equipamento_gaveta') 
    gaveta = models.ForeignKey(Gaveta, on_delete=models.SET_NULL, null=True, blank=True, related_name='Equipamento_Gavera') 
    obs = models.TextField(verbose_name="Observação", blank=True)
    foto = models.ImageField(upload_to='imagens', null=True, blank=True, default='imagens\campus_itapetinga.png', verbose_name="Foto_Equipamento")   

    class Meta:
        verbose_name = u'Modelo'
        verbose_name_plural = u'Equipamentos'
        ordering = ['nome']           

    def __str__(self):
         return self.nome		   	
		
class Vidraria(models.Model):
    CALIB_CHOICES = (
        ("SIM", "SIM"),
        ("NAO", "NÃO"),
    )
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL,  null=True, blank=True, verbose_name="Vidraria_Usuario :" ) 
    nome = models.CharField(max_length=100, null=False, verbose_name="Nome :")    
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, null=True, blank=True, related_name='Vidraria_Marca')
    data_compra =  models.DateTimeField(default=timezone.now)
    origem = models.FileField(upload_to='pdf', null=True, blank=True, verbose_name="Anexar PDF Origem:")
    ficha_tec = models.FileField(upload_to='ficha_tec',  default='imagens\campus_itapetinga.png', null=True, blank=True, verbose_name="Anexar PDF Ficha Técnica :")
    especficacao_t = models.TextField(null=False, blank=True, verbose_name="Especificação Técnica")
    quantidade = models.PositiveIntegerField(null=False, blank=True)
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT, null=False, related_name='Vidrarias_Sala')
    armario = models.ForeignKey(Armario, on_delete=models.SET_NULL, null=True, blank=True, related_name='Vidraria_Armario')
    bancada = models.ForeignKey(Bancada, on_delete=models.SET_NULL, null=True, blank=True, related_name='Vidraria_bancada')
    estante = models.ForeignKey(Estante, on_delete=models.SET_NULL, null=True, blank=True, related_name='Vidraria_prateleira') 
    prateleira = models.ForeignKey(Prateleira, on_delete=models.SET_NULL, null=True, blank=True, related_name='Vidraria_gaveta') 
    gaveta = models.ForeignKey(Gaveta, on_delete=models.SET_NULL, null=True, blank=True, related_name='Vidraria_Gaveta') 
    obs = models.TextField(verbose_name="Vidraria_Observação", blank=True)
    foto = models.ImageField(upload_to='images', null=True, blank=True,  default='imagens\campus_itapetinga.png', verbose_name="Foto_Vidraria") 

    class Meta:
        verbose_name = u'Modelo'
        verbose_name_plural = u'Equipamentos'
        ordering = ['nome']

    def __str__(self):
         return self.nome

class Reagente(models.Model):
    DISPON_CHOICES = (
        ("SIM", "SIM"),
        ("NAO", "NÃO"),
    )
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL,  null=True, blank=True, verbose_name="Reagente_Diverso :" ) 
    nome = models.CharField(max_length=100, unique=True, null=False, verbose_name="Nome :")
    formula_q = models.CharField(max_length=100, null=False, blank=True, verbose_name="Formula Química :")
    grau_p = models.CharField(max_length=100, null=True, blank=True, verbose_name="Grau_pureza :")
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT, null=True, blank=True, related_name='unidade')
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name='reagente')
    quantidade = models.DecimalField(max_digits=9, decimal_places=2, default=0.00, null=True, verbose_name="Quantidade :")
    data_validade = models.DateTimeField(default=timezone.now, null=True, blank=True, verbose_name="Validade")
    controle_pfex = models.CharField(max_length=50, null=True, blank=True, verbose_name="Controle PF / Exercito :")
    ficha_tec = models.FileField(upload_to='ficha_tec', null=True, blank=True,  default='imagens\campus_itapetinga.png', verbose_name="Anexar PDF :")
    massamolecular = models.CharField(max_length=100, null=True, blank=True, verbose_name="Massa Molecular :")
    densidade = models.CharField(max_length=100, null=True, blank=True, verbose_name="Densidade :")
    disponibilidade = models.CharField(max_length=3, null=False, blank=True, choices=DISPON_CHOICES)   
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT, null=False, related_name='Reagente_Sala')
    armario = models.ForeignKey(Armario, on_delete=models.SET_NULL, null=True, blank=True, related_name='Reagente_Armario')
    bancada = models.ForeignKey(Bancada, on_delete=models.SET_NULL, null=True, blank=True, related_name='Reagente_bancada')
    estante = models.ForeignKey(Estante, on_delete=models.SET_NULL, null=True, blank=True, related_name='Reagente_prateleira') 
    prateleira = models.ForeignKey(Prateleira, on_delete=models.SET_NULL, null=True, blank=True, related_name='Reagente_gaveta') 
    gaveta = models.ForeignKey(Gaveta, on_delete=models.SET_NULL, null=True, blank=True, related_name='Reagente_Gaveta')
    obs = models.TextField( null=True, blank=True, verbose_name="Reagente_Observação :") 
    foto = models.ImageField(upload_to='imagens', null=True, blank=True,  default='imagens\campus_itapetinga.png', verbose_name="Foto_Reagente")      
    
    def __str__(self):
        #return self.nome    
        return self.nome +  ' - Unidade  : ' + str(self.unidade)     
    
            

class Diverso(models.Model):
    DISPON_CHOICES = (
        ("SIM", "SIM"),
        ("NAO", "NÃO"),
    ) 
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL,  null=True, blank=True, verbose_name="Diverso_Usuário :" )    
    nome = models.CharField(max_length=100, unique=True, null=False, verbose_name="Nome :")
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name='Diversos')
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT, null=True, blank=True, related_name='Diverso_unidade')
    quantidade = models.DecimalField(max_digits=9, decimal_places=2, default=0.00, null=True, verbose_name="Diverso_Quantidade :")    
    ficha_tec = models.FileField(upload_to='ficha_tec', null=True, blank=True,  default='imagens\campus_itapetinga.png', verbose_name="Diverso_Anexar_PDF :")    
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT, null=False, related_name='Diverso_Sala')
    armario = models.ForeignKey(Armario, on_delete=models.SET_NULL, null=True, blank=True, related_name='Diverso_Armario')
    bancada = models.ForeignKey(Bancada, on_delete=models.SET_NULL, null=True, blank=True, related_name='Diverso_bancada')
    estante = models.ForeignKey(Estante, on_delete=models.SET_NULL, null=True, blank=True, related_name='Diverso_prateleira') 
    prateleira = models.ForeignKey(Prateleira, on_delete=models.SET_NULL, null=True, blank=True, related_name='Diverso_gaveta') 
    gaveta = models.ForeignKey(Gaveta, on_delete=models.SET_NULL, null=True, blank=True, related_name='Diverso_Gaveta')    
    obs = models.TextField( blank=True, verbose_name="Diverso_Observação :")  
    foto = models.ImageField(upload_to='images', null=True,  default='imagens\campus_itapetinga.png', blank=True, verbose_name="Foto_Diverso")           
    
    def __str__(self):
        return self.nome

class PedidoSolucao(models.Model):     
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Usuario_Pedidosolução :" )    
    nome = models.CharField(max_length=200, null=False, verbose_name="Nome :")
    concentracao =  models.FloatField(null=True, blank=True, verbose_name="Concetração :")
    data_producao = models.DateTimeField(default=timezone.now, verbose_name="Data_Produção_Solucão") 
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT, related_name='Solução_unidade')  
    quantidade = models.DecimalField(max_digits=9, decimal_places=2, default=0.00, verbose_name="Solução_Quantidade :")
    status = models.CharField(
        default="Em Preparação",
        max_length=15,
        choices=(
            ('Preparada', 'Preparada'),
            ('Em Produção', 'Em Produção'),            
        )
    )      
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT, null=False, related_name='Solução_Sala')
    armario = models.ForeignKey(Armario, on_delete=models.SET_NULL, null=True, blank=True, related_name='PSolução_Armario')
    bancada = models.ForeignKey(Bancada, on_delete=models.SET_NULL, null=True, blank=True, related_name='PSolução_bancada')
    estante = models.ForeignKey(Estante, on_delete=models.SET_NULL, null=True, blank=True, related_name='PSolução_prateleira') 
    prateleira = models.ForeignKey(Prateleira, on_delete=models.SET_NULL, null=True, blank=True, related_name='PSolução_gaveta') 
    gaveta = models.ForeignKey(Gaveta, on_delete=models.SET_NULL, null=True, blank=True, related_name='PSolução_Gaveta')
    obs = models.TextField( blank=True, verbose_name="PSolução_Observação :")     
    
    def __str__(self):
        return self.id + ' - ' + self.nome   

class ItensPedidoSolucao(models.Model): 
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="UsuarioItensPedidosolução :" )    
    pedidosolucao_id = models.IntegerField(null=True, blank=True)   
    reagente = models.ForeignKey(Reagente, on_delete=models.PROTECT, related_name='Reagente_PSolução')      
    quantidade = models.DecimalField(max_digits=9, decimal_places=2, default=0.00, null=True, verbose_name="Quantidade Item :")
  
    def __str__(self):
        return self.pedidosolucao_id

class Fornecedor(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL,  null=True, blank=True, verbose_name="Fornecedor_Usuario :" ) 
    nome = models.CharField(max_length=150, unique=True, verbose_name="Fornecedor_Nome :" )      
    cnpj = models.CharField(unique=True, max_length=20, null=True, blank=True, verbose_name="Fornecedor_CNPJ :")
    cpf = models.CharField(unique=True, max_length=14, null=True, blank=True, verbose_name="Fornecedor_CPF :")
    data_cadastro =  models.DateTimeField(default=timezone.now, verbose_name="Fornecedor_Data_cadastro :")
    endereco = models.CharField(max_length=250, null=True, blank=True, verbose_name="Fornecedor_Endereço :")  
    telefone = models.CharField(max_length=15, null=True, blank=True, verbose_name="Fornecedor_Telefone :")
    cel= models.CharField(max_length=15, null=True, blank=True, verbose_name="Fornecedor_celular :")    
    email = models.EmailField(null=True, blank=True, verbose_name="Fornecedor_Email :")   
    obs = models.TextField(verbose_name="Fornecedor Observação", null=True, blank=True) 
    
    
    def __str__(self):
         return self.nome       

class Entrada(models.Model): 
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="UsuarioEntrada :" )    
    nf = models.PositiveIntegerField(null=True, blank=True)     
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT, related_name='fornecedor_Entrada')  
    data_cadastro =  models.DateTimeField(default=timezone.now, verbose_name="Data_de Cadastro Fornecedor") 
    nf_foto = models.FileField(upload_to='pdf/nf_entrada', null=False, blank=False, verbose_name="Foto_NFo") 
    obs = models.TextField( blank=True, verbose_name="Diverso_Observação :")  
    status = models.CharField(
        default="Em Preparação",
        max_length=15,
        choices=(
            ('Em Preparação', 'Em Preparação'),
            ('Em Preparada', 'Preparada OK'),            
        )
    )      
  
 
    def __str__(self):
        return self.nf          

class ItensEntrada(models.Model): 
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Usuario_Entrada :" )    
    entrada_id = models.IntegerField(null=True, blank=True)  
    reagente = models.ForeignKey(Reagente, on_delete=models.PROTECT, related_name='Reagente_Entrada') 
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT, related_name='Unidade_Entrada')  
    quantidade = models.DecimalField(max_digits=9, decimal_places=2, default=0.00, null=True, verbose_name="Quantidade_Entrada :")
         
    def __str__(self):
        return self.entrada_id    
    
        
 # estou aqui   
    
class Destinatario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL,  null=True, blank=True, verbose_name="Destinatario_Usuario :" ) 
    nome = models.CharField(max_length=150, unique=True, verbose_name="Destinatario_Nome :" )      
    cnpj = models.CharField(unique=True, max_length=20, null=True, blank=True, verbose_name="Destinatario_CNPJ :")
    cpf = models.CharField(unique=True, max_length=14, null=True, blank=True, verbose_name="Destinatario_CPF :")
    data_cadastro =  models.DateTimeField(default=timezone.now, verbose_name="Destinatario_Data_cadastro :")
    endereco = models.CharField(max_length=250, null=True, blank=True, verbose_name="Destinatario_Endereço :")  
    telefone = models.CharField(max_length=15, null=True, blank=True, verbose_name="Destinatario_Telefone :")
    cel= models.CharField(max_length=15, null=True, blank=True, verbose_name="Destinatario_celular :")    
    email = models.EmailField(null=True, blank=True, verbose_name="Destinatario_Email :")   
    obs = models.TextField(verbose_name="Destinatario Observação", null=True, blank=True)      

    def __str__(self):
         return self.nome       

class Saida(models.Model): 
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="UsuarioSaida :" )    
    nf = models.PositiveIntegerField(null=True, blank=True)     
    destinatario = models.ForeignKey(Destinatario, on_delete=models.PROTECT, related_name='Destinatario_Saida')  
    data_cadastro =  models.DateTimeField(default=timezone.now, verbose_name="Data_de Cadastro Destinatario") 
    nf_foto = models.FileField(upload_to='pdf/doc_saida',  null=False, blank=False, verbose_name="Foto_NFo") 
    obs = models.TextField( blank=True, verbose_name="Diverso_Observação :")  
  
 
    def __str__(self):
        return self.nf          

class ItensSaida(models.Model): 
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Usuario_Saida :" )    
    saida_id = models.IntegerField(null=True, blank=True)  
    reagente = models.ForeignKey(Reagente, on_delete=models.PROTECT, related_name='Reagente_Saida') 
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT, related_name='Unidade_Saida')  
    quantidade = models.DecimalField(max_digits=9, decimal_places=2, default=0.00, null=True, verbose_name="Quantidade_Saida :")
         
    def __str__(self):
        return self.saida_id    
       
		
class Solucao(models.Model):
    CALIB_CHOICES = (
        ("SIM", "SIM"),
        ("NAO", "NÃO"),
    )
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL,  null=True, blank=True, verbose_name="Solução_Usuario :" ) 
    nome = models.CharField(max_length=200, null=False, verbose_name="Solução_Nome :")    
    quantidade = models.DecimalField(max_digits=9, decimal_places=2, default=0.00, null=True, blank=True, verbose_name="Quantidade_Solução :")    
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT, null=True, blank=True, related_name='Soluçãos_Sala')
    armario = models.ForeignKey(Armario, on_delete=models.SET_NULL, null=True, blank=True, related_name='Solução_Armario')
    bancada = models.ForeignKey(Bancada, on_delete=models.SET_NULL, null=True, blank=True, related_name='Solução_bancada')
    estante = models.ForeignKey(Estante, on_delete=models.SET_NULL, null=True, blank=True, related_name='Solução_prateleira') 
    prateleira = models.ForeignKey(Prateleira, on_delete=models.SET_NULL, null=True, blank=True, related_name='Solução_gaveta') 
    gaveta = models.ForeignKey(Gaveta, on_delete=models.SET_NULL, null=True, blank=True, related_name='Solução_Gaveta') 
    obs = models.TextField(verbose_name="Solução_Observação", blank=True) 

    class Meta:
        verbose_name = u'Modelo'
        verbose_name_plural = u'Solução'
        ordering = ['nome']

    def __str__(self):
         return self.nome
 
    
    
class AulaPratica(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL,  null=True, blank=True, verbose_name="AulaPratica_Usuario :" ) 
    nome = models.CharField(max_length=150, null=True, blank=True, verbose_name="AulaPratica_Nome :" )     
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT, null=False, related_name='AulaPraticaa')   
    data_inicio =  models.DateTimeField(default=timezone.now, null=False, blank=False, verbose_name="Aula_Pratica_data_inicio :")
    horario_inicio =  models.CharField(max_length=5, null=True, blank=True, verbose_name="Horario_inicio :" )  
    horario_fim =  models.CharField(max_length=5, null=True, blank=True, verbose_name="Horario_fim :" )       
    quantalunos = models.IntegerField(null=False, blank=False)       
    obs = models.TextField(verbose_name="Aula_Pratica     ario Observação", null=True, blank=True) 
    status = models.CharField(
        default="Aula Solicitada", null=True, blank=True, verbose_name="Aula_Pratica_status :", max_length=15,
        choices=(
            ('Aula Preparada', 'Aula Preparada'),
            ('Aula Solicitada', 'Aula Solicitada'),                        
        )
     )            

    def __str__(self):
         return self.nome
        
   
class ItensAulaPratica(models.Model): 
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Usuario_Aula_Pratica')    
    aulapratica_id = models.IntegerField(null=True, blank=True)      
    reagente = models.ForeignKey(Reagente, on_delete=models.PROTECT, null=False, blank=False, related_name='Aula_Pratica_reagente') 
    quant_reagente = models.DecimalField(max_digits=9, decimal_places=2, default=0.00, null=False, blank=False, verbose_name='Quant_Aula_Pratica_Reagente')
            
    def __str__(self):
        return self.aulapratica_id  
         
        
class EquipamentosAulaPratica(models.Model): 
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Usuario_Aula_Pratica')    
    aulapratica_id = models.IntegerField(null=True, blank=True)  
    equipamentos = models.ForeignKey(Equipamento, on_delete=models.PROTECT, null=False, blank=False, related_name='Aula_Pratica_Equipamentos') 
    quant_equipamentos = models.DecimalField(max_digits=9, decimal_places=2, default=0.00, null=False, blank=False, verbose_name='Quant_Aula_Pratica_Equipamentos' )
   
         
    def __str__(self):
        return self.aulapratica_id   

        
class SolucaoAulaPratica(models.Model): 
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Usuario_Aula_Pratica')    
    aulapratica_id = models.IntegerField(null=True, blank=True)  
    solucao = models.ForeignKey(Solucao, on_delete=models.PROTECT, null=False, blank=False, related_name='Aula_Pratica_Solução') 
    quant_solucao = models.DecimalField(max_digits=9, decimal_places=2, default=0.00, null=False, blank=False, verbose_name='Quant_Aula_Pratica_Solucão' )

         
    def __str__(self):
        return self.aulapratica_id   
        