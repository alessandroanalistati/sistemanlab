import sys     
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from nlab import settings
from sisnlab.views.sala_views import *
from sisnlab.views.armario_views import *
from sisnlab.views.estante_views import *
from sisnlab.views.tombo_views import *
from sisnlab.views.bancada_views import *
from sisnlab.views.prateleira_views import *
from sisnlab.views.gaveta_views import *
from sisnlab.views.marca_views import *
from sisnlab.views.equipamento_views import *
from sisnlab.views.unidade_views import *
from sisnlab.views.vidraria_views import *
from sisnlab.views.reagente_views import *
from sisnlab.views.diverso_views import *
from sisnlab.views.pedidosolucao_views import *
from sisnlab.views.login_views import *
from sisnlab.views.fornecedor_views import *
from sisnlab.views.entrada_views import *
from sisnlab.views.destinatario_views import *
from sisnlab.views.saida_views import *
from sisnlab.views.aulapratica_views import *
from sisnlab.views.solucao_views import *

from sisnlab.utils import sendemail

app_name = 'sisnlab'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_user),          
    path('login/submit', submit_login),
    path('logout/', logout_user, name='logout_user'),
    path('dashboard', inicio, name='dashboard'),
    
     
    #path('projeto2pdf', projeto2pdf, name='print_pdf'),
          
    path('listar_salas', listar_sala, name='listar_salas'),
    path('cadastrar_sala', inserir_sala, name='cadastrar_sala'),
    path('listar_sala/<int:id>', listar_sala_id, name='listar_sala_id'),
    path('editar_sala/<int:id>', editar_sala, name='editar_sala'),
    path('removersala/<int:id>', remover_sala, name='remover_sala'),
    
    path('listar_armarios', listar_armario, name='listar_armarios'),
    path('cadastrar_armario', inserir_armario, name='cadastrar_armario'),
    path('listar_armario/<int:id>', listar_armario_id, name='listar_armario_id'),
    path('editar_armario/<int:id>', editar_armario, name='editar_armario'),
    path('remover_armario/<int:id>', remover_armario, name='remover_armario'),
    path('visualizar_armario/<int:id>', visualizar_armario, name='visualizar_armario'),

    path('listar_tombos', listar_tombo, name='listar_tombos'),
    path('cadastrar_tombo', inserir_tombo, name='cadastrar_tombo'),
    path('listar_tombo/<int:id>', listar_tombo_id, name='listar_tombo_id'),
    path('editar_tombo/<int:id>', editar_tombo, name='editar_tombo'),
    path('remover_tombo/<int:id>', remover_tombo, name='remover_tombo'),


    path('listar_estantes', listar_estante, name='listar_estantes'),
    path('cadastrar_estante', inserir_estante, name='cadastrar_estante'),
    path('listar_estante/<int:id>', listar_estante_id, name='listar_estante_id'),
    path('editar_estante/<int:id>', editar_estante, name='editar_estante'),
    path('remover_estante/<int:id>', remover_estante, name='remover_estante'),

    path('listar_bancadas', listar_bancada, name='listar_bancadas'),
    path('cadastrar_bancada', inserir_bancada, name='cadastrar_bancada'),
    path('listar_bancada/<int:id>', listar_bancada_id, name='listar_bancada_id'),
    path('editar_bancada/<int:id>', editar_bancada, name='editar_bancada'),
    path('remover_bancada/<int:id>', remover_bancada, name='remover_bancada'),

    path('listar_prateleiras', listar_prateleira, name='listar_prateleiras'),
    path('cadastrar_prateleira', inserir_prateleira, name='cadastrar_prateleira'),
    path('listar_prateleira/<int:id>', listar_prateleira_id, name='listar_prateleira_id'),
    path('editar_prateleira/<int:id>', editar_prateleira, name='editar_prateleira'),
    path('remover_prateleira/<int:id>', remover_prateleira, name='remover_prateleira'),

    path('listar_gavetas', listar_gaveta, name='listar_gavetas'),
    path('cadastrar_gaveta', inserir_gaveta, name='cadastrar_gaveta'),
    path('listar_gaveta/<int:id>', listar_gaveta_id, name='listar_gaveta_id'),
    path('editar_gaveta/<int:id>', editar_gaveta, name='editar_gaveta'),
    path('remover_gaveta/<int:id>', remover_gaveta, name='remover_gaveta'),

    path('listar_marcas', listar_marca, name='listar_marcas'),
    path('cadastrar_marca', inserir_marca, name='cadastrar_marca'),
    path('listar_marca/<int:id>', listar_marca_id, name='listar_marca_id'),
    path('editar_marca/<int:id>', editar_marca, name='editar_marca'),
    path('remover_marca/<int:id>', remover_marca, name='remover_marca'),

    path('listar_equipamentos', listar_equipamento, name='listar_equipamentos'),
    path('cadastrar_equipamento', inserir_equipamento, name='cadastrar_equipamento'),
    path('listar_equipamento/<int:id>', listar_equipamento_id, name='listar_equipamento_id'),
    path('editar_equipamento/<int:id>', editar_equipamento, name='editar_equipamento'),
    path('remover_equipamento/<int:id>', remover_equipamento, name='remover_equipamento'),
    path('visualizar_equipamento/<int:id>', visualizar_equipamento, name='visualizar_equipamento'),
    
    path('ajax/load-armarios/', load_armarios, name='ajax_load_armarios'), # AJAX
    path('ajax/load-estantes/', load_estantes, name='ajax_load_estantes'), # AJAX
    path('ajax/load-bancadas/', load_bancadas, name='ajax_load_bancadas'), # AJAX
    path('ajax/load-prateleiras_arm/', load_prateleiras_arm, name='ajax_load_prateleiras_arm'), # AJAX
    path('ajax/load-prateleiras_est/', load_prateleiras_est, name='ajax_load_prateleiras_est'), # AJAX
    path('ajax/load-prateleiras_ban/', load_prateleiras_ban, name='ajax_load_prateleiras_ban'), # AJAX
    path('ajax/load-gavetas_arm/', load_gavetas_arm, name='ajax_load_gavetas_arm'), # AJAX
    path('ajax/load-gavetas_est/', load_gavetas_est, name='ajax_load_gavetas_est'), # AJAX
    path('ajax/load-gavetas_ban/', load_gavetas_ban, name='ajax_load_gavetas_ban'), # AJAX
 
    

    path('listar_unidades', listar_unidade, name='listar_unidades'),
    path('cadastrar_unidade', inserir_unidade, name='cadastrar_unidade'),
    path('listar_unidade/<int:id>', listar_unidade_id, name='listar_unidade_id'),
    path('editar_unidade/<int:id>', editar_unidade, name='editar_unidade'),
    path('remover_unidade/<int:id>', remover_unidade, name='remover_unidade'),    

    path('listar_vidrarias', listar_vidraria, name='listar_vidrarias'),
    path('cadastrar_vidraria', inserir_vidraria, name='cadastrar_vidraria'),
    path('listar_vidraria/<int:id>', listar_vidraria_id, name='listar_vidraria_id'),
    path('editar_vidraria/<int:id>', editar_vidraria, name='editar_vidraria'),
    path('remover_vidraria/<int:id>', remover_vidraria, name='remover_vidraria'),
    path('visualizar_vidraria/<int:id>', visualizar_vidraria, name='visualizar_vidraria'),
     
    
    path('listar_reagentes', listar_reagente, name='listar_reagentes'),
    path('cadastrar_reagente', inserir_reagente, name='cadastrar_reagente'),
    path('listar_reagente/<int:id>', listar_reagente_id, name='listar_reagente_id'),
    path('editar_reagente/<int:id>', editar_reagente, name='editar_reagente'),
    path('remover_reagente/<int:id>', remover_reagente, name='remover_reagente'),
    path('visualizar_reagente/<int:id>', visualizar_reagente, name='visualizar_reagente'),
    
    path('ajax/load-armarios_produtos/', load_armarios_produtos, name='ajax_load_armarios_produtos'), # AJAX
    path('ajax/load-estantes_produtos/', load_estantes_produtos, name='ajax_load_estantes_produtos'), # AJAX
    path('ajax/load-bancadas_produtos/', load_bancadas_produtos, name='ajax_load_bancadas_produtos'), # AJAX
    path('ajax/load-gavetas_arm_produtos/', load_gavetas_arm_produtos, name='ajax_load_gavetas_arm_produtos'), # AJAX
    path('ajax/load-gavetas_est_produtos/', load_gavetas_est_produtos, name='ajax_load_gavetas_est_produtos'), # AJAX
    path('ajax/load-gavetas_ban_produtos/', load_gavetas_ban_produtos, name='ajax_load_gavetas_ban_produtos'), # AJAX
    path('ajax/load-prateleiras_arm_produtos/', load_prateleiras_arm_produtos, name='ajax_load_prateleiras_arm_produtos'), # AJAX
    path('ajax/load-prateleiras_est_produtos/', load_prateleiras_est_produtos, name='ajax_load_prateleiras_est_produtos'), # AJAX
    path('ajax/load-prateleiras_ban_produtos/', load_prateleiras_ban_produtos, name='ajax_load_prateleiras_ban_produtos'), # AJAX
    
        
    path('listar_solucoes', listar_solucao, name='listar_solucoes'),
    path('cadastrar_solucao', inserir_solucao, name='cadastrar_solucao'),
    path('listar_solucao/<int:id>', listar_solucao_id, name='listar_solucao_id'),
    path('editar_solucao/<int:id>', editar_solucao, name='editar_solucao'),
    path('remover_solucao/<int:id>', remover_solucao, name='remover_solucao'),
    path('visualizar_solucao/<int:id>', visualizar_solucao, name='visualizar_solucao'),
    
    
    
    

    path('listar_diversos', listar_diverso, name='listar_diversos'),
    path('cadastrar_diverso', inserir_diverso, name='cadastrar_diverso'),
    path('listar_diverso/<int:id>', listar_diverso_id, name='listar_diverso_id'),
    path('editar_diverso/<int:id>', editar_diverso, name='editar_diverso'),
    path('remover_diverso/<int:id>', remover_diverso, name='remover_diverso'),
    path('visualizar_diverso/<int:id>', visualizar_diverso, name='visualizar_diverso'),
    
    path('listar_pedidosolucoes', listar_pedidosolucao, name='listar_pedidosolucoes'),
    path('cadastrar_pedidosolucao', inserir_pedidosolucao, name='cadastrar_pedidosolucao'),
    path('listar_pedidosolucao/<int:id>', listar_pedidosolucao_id, name='listar_pedidosolucao_id'),
    path('editar_pedidosolucao/<int:id>', editar_pedidosolucao, name='editar_pedidosolucao'),
    path('remover_pedidosolucao/<int:id>', remover_pedidosolucao, name='remover_pedidosolucao'),
    path('visualizar_pedidosolucao/<int:id>', visualizar_pedidosolucao, name='visualizar_pedidosolucao'),    
    path('itens_pedidosolucoes/<int:pedidosolucao_id>', itens_pedidosolucoes, name='itens_pedidosolucoes'),
    path('visualizar_pedidosolucaoitens/<int:id>', visualizar_pedidosolucaoitens, name='visualizar_pedidosolucaoitens'),
    path('baixa_estoque/<int:id>', dar_baixa_estoque, name='baixa_estoque'),
    
    
    path('ajax/load-armarios_psolucao/', load_armarios_psolucao, name='ajax_load_armarios_psolucao'), # AJAX    
    path('ajax/load-estantes_psolucao/', load_estantes_psolucao, name='ajax_load_estantes_psolucao'), # AJAX
    path('ajax/load-bancadas_psolucao/', load_bancadas_psolucao, name='ajax_load_bancadas_psolucao'), # AJAX
    path('ajax/load-gavetas_arm_psolucao/', load_gavetas_arm_psolucao, name='ajax_load_gavetas_arm_psolucao'), # AJAX
    path('ajax/load-gavetas_est_psolucao/', load_gavetas_est_psolucao, name='ajax_load_gavetas_est_psolucao'), # AJAX
    path('ajax/load-gavetas_ban_psolucao/', load_gavetas_ban_psolucao, name='ajax_load_gavetas_ban_psolucao'), # AJAX
    path('ajax/load-prateleiras_arm_psolucao/', load_prateleiras_arm_psolucao, name='ajax_load_prateleiras_arm_psolucao'), # AJAX
    path('ajax/load-prateleiras_est_psolucao/', load_prateleiras_est_psolucao, name='ajax_load_prateleiras_est_psolucao'), # AJAX
    path('ajax/load-prateleiras_ban_psolucao/', load_prateleiras_ban_psolucao, name='ajax_load_prateleiras_ban_psolucao'), # AJAX   
    
            
    path('listar_fornecedores', listar_fornecedor, name='listar_fornecedores'),
    path('cadastrar_fornecedor', inserir_fornecedor, name='cadastrar_fornecedor'),
    path('listar_fornecedor/<int:id>', listar_fornecedor_id, name='listar_fornecedor_id'),
    path('editar_fornecedor/<int:id>', editar_fornecedor, name='editar_fornecedor'),
    path('remover_fornecedor/<int:id>', remover_fornecedor, name='remover_fornecedor'),
    path('visualizar_fornecedor/<int:id>', visualizar_fornecedor, name='visualizar_fornecedor'),    
    
    
    path('listar_destinatarios', listar_destinatario, name='listar_destinatarios'),
    path('cadastrar_destinatario', inserir_destinatario, name='cadastrar_destinatario'),
    path('listar_destinatario<int:id>', listar_destinatario_id, name='listar_destinatarioid'),
    path('editar_destinatario<int:id>', editar_destinatario, name='editar_destinatario'),
    path('remover_destinatario<int:id>', remover_destinatario, name='remover_destinatario'),
    path('visualizar_destinatario<int:id>', visualizar_destinatario, name='visualizar_destinatario'),  
   
    path('listar_entradas', listar_entrada, name='listar_entradas'),
    path('cadastrar_entrada', inserir_entrada, name='cadastrar_entrada'),
    path('listar_entrada/<int:id>', listar_entrada_id, name='listar_entrada_id'),
    path('editar_entrada/<int:id>', editar_entrada, name='editar_entrada'),
    path('remover_entrada/<int:id>', remover_entrada, name='remover_entrada'),
    path('visualizar_entrada/<int:id>', visualizar_entrada, name='visualizar_entrada'), 
    path('pega_entrada', pega_ultima_entrada, name='pega_entrada'), 
    
    path('itens_entradas/<int:entrada_id>', itens_entradas, name='itens_entradas'),
    path('visualizar_entradaitens/<int:id>', visualizar_entradaitens, name='visualizar_entradaitens'),
    path('entrada_estoque/<int:id>', dar_entrada_estoque, name='entrada_estoque'), 
    path('pega_pedido_solucao', pega_ultima_solucao, name='pega_pedido_solucao'), 
    
    path('listar_saidas', listar_saida, name='listar_saidas'),
    path('cadastrar_saida', inserir_saida, name='cadastrar_saida'),
    path('listar_saida/<int:id>', listar_saida_id, name='listar_saida_id'),
    path('editar_saida/<int:id>', editar_saida, name='editar_saida'),
    path('remover_saida/<int:id>', remover_saida, name='remover_saida'),
    path('visualizar_saida/<int:id>', visualizar_saida, name='visualizar_saida'), 
    path('pega_saida', pega_ultima_saida, name='pega_saida'), 
    
    path('itens_saidas/<int:saida_id>', itens_saidas, name='itens_saidas'),
    path('visualizar_saidaitens/<int:id>', visualizar_saidaitens, name='visualizar_saidaitens'),
    path('saida_estoque/<int:id>', dar_saida_estoque, name='saida_estoque'), 
    path('pega_pedido_solucao', pega_ultima_solucao, name='pega_pedido_solucao'),     
     
  
    path('listar_aulapraticas', listar_aulapratica, name='listar_aulapraticas'),
    path('listar_aulapratica_email', listar_aulapratica_email, name='listar_aulapratica_email'),
    path('cadastrar_aulapratica', inserir_aulapratica, name='cadastrar_aulapratica'),
    path('listar_aulapratica/<int:id>', listar_aulapratica_id, name='listar_aulapratica_id'),
    path('editar_aulapratica/<int:id>', editar_aulapratica, name='editar_aulapratica'),
    path('editar_aulapraticanovamente/<int:id>', editar_aulapraticanovamente, name='editar_aulapraticanovamente'),
    path('remover_aulapratica/<int:id>', remover_aulapratica, name='remover_aulapratica'),
    path('visualizar_aulapratica/<int:id>', visualizar_aulapratica, name='visualizar_aulapratica'),  
    path('visualizar_aulapratica_editar/<int:id>', visualizar_aulapratica_editar, name='visualizar_aulapratica_editar'),        
    path('produtos_aulapraticas/<int:aulapratica_id>', produtos_aulapraticas, name='produtos_aulapraticas'),    
    path('equipamentos_aulapraticas/<int:aulapratica_id>', equipamentos_aulapraticas, name='equipamentos_aulapraticas'),    
    path('solucoes_aulapraticas/<int:aulapratica_id>', solucoes_aulapraticas, name='solucoes_aulapraticas'),    
    path('visualizar_aulapraticaitens/<int:id>', visualizar_aulapraticaitens, name='visualizar_aulapraticaitens'),
    
    path('remover_itensaulapratica/<int:id>', remover_itensaulapratica, name='remover_itensaulapratica'),
    path('remover_solucaoaulapratica/<int:id>', remover_solucaoaulapratica, name='remover_solucaoaulapratica'),
    path('remover_equipamentosaulapratica/<int:id>', remover_equipamentosaulapratica, name='remover_equipamentosaulapratica'),
    path('dar_saida_aula_pratica/<int:id>', dar_saida_aula_pratica, name='dar_saida_aula_pratica'),
    
    
  
   
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)