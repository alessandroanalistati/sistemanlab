import sys
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from ..forms import pedidosolucao_forms
from ..forms import itenspedidosolucao_forms
from ..entidades import pedidosolucao
from ..entidades import itenspedidosolucao
from ..services import pedidosolucao_service
from ..services import itenspedidosolucao_service
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from ..models import PedidoSolucao
from ..models import ItensPedidoSolucao
from ..models import Reagente
from django.contrib.auth.decorators import user_passes_test
from ..models import Armario, Sala, Estante, Bancada, Prateleira, Gaveta


@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_pedidosolucao(request):
    pedidosolucoes = pedidosolucao_service.listar_pedidosolucoes()
    return render(request, 'pedidosolucoes/listar_pedidosolucoes.html', {'pedidosolucoes': pedidosolucoes})


@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def inserir_pedidosolucao(request):
    if request.method == "POST":
        form_pedidosolucao = pedidosolucao_forms.PedidoSolucaoForm(request.POST, request.FILES)      
        if form_pedidosolucao.is_valid():            
            usuario = form_pedidosolucao.cleaned_data["usuario"]
            nome = form_pedidosolucao.cleaned_data["nome"]
            concentracao = form_pedidosolucao.cleaned_data["concentracao"]
            data_producao = form_pedidosolucao.cleaned_data["data_producao"]             
            unidade = form_pedidosolucao.cleaned_data["unidade"]          
            quantidade = form_pedidosolucao.cleaned_data["quantidade"]  
            status = form_pedidosolucao.cleaned_data["status"]                                
            sala = form_pedidosolucao.cleaned_data["sala"]
            armario = form_pedidosolucao.cleaned_data["armario"]
            bancada = form_pedidosolucao.cleaned_data["bancada"]
            estante = form_pedidosolucao.cleaned_data["estante"]
            prateleira = form_pedidosolucao.cleaned_data["prateleira"]
            gaveta = form_pedidosolucao.cleaned_data["gaveta"]           
            obs = form_pedidosolucao.cleaned_data["obs"]            

            pedidosolucao_novo = pedidosolucao.PedidoSolucao(usuario=request.user, nome=nome, concentracao=concentracao, data_producao=data_producao, unidade=unidade, 
            quantidade=quantidade, status=status, sala=sala, armario=armario, bancada=bancada, estante=estante, prateleira=prateleira, gaveta=gaveta,
            obs=obs)
                       
            pedidosolucao_service.cadastrar_pedidosolucao(pedidosolucao_novo) 
                   
            pedidosolucao_novo = PedidoSolucao.objects.filter(usuario=request.user).last()
            
            return render(request, 'pedidosolucoes/itenssolucao.html', {'pedidosolucao_novo': pedidosolucao_novo})  
    else:
        form_pedidosolucao = pedidosolucao_forms.PedidoSolucaoForm()   
    return render(request, 'pedidosolucoes/form_pedidosolucao.html', {'form_pedidosolucao': form_pedidosolucao})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_pedidosolucao_id(request, id):
    pedidosolucao = pedidosolucao_service.listar_pedidosolucao_id(id)

    return render(request, 'pedidosolucoes/lista_pedidosolucao.html', {'pedidosolucao': pedidosolucao})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def editar_pedidosolucao(request, id):
    pedidosolucao_antigo = pedidosolucao_service.listar_pedidosolucao_id(id)
    form_pedidosolucao = pedidosolucao_forms.PedidoSolucaoForm(request.POST or None, instance=pedidosolucao_antigo)   
    if form_pedidosolucao.is_valid():
            usuario = form_pedidosolucao.cleaned_data["usuario"]
            nome = form_pedidosolucao.cleaned_data["nome"]
            concentracao = form_pedidosolucao.cleaned_data["concentracao"]
            data_producao = form_pedidosolucao.cleaned_data["data_producao"]             
            unidade = form_pedidosolucao.cleaned_data["unidade"]          
            quantidade = form_pedidosolucao.cleaned_data["quantidade"]  
            status = form_pedidosolucao.cleaned_data["status"]                                       
            sala = form_pedidosolucao.cleaned_data["sala"]
            armario = form_pedidosolucao.cleaned_data["armario"]
            bancada = form_pedidosolucao.cleaned_data["bancada"]
            estante = form_pedidosolucao.cleaned_data["estante"]
            prateleira = form_pedidosolucao.cleaned_data["prateleira"]
            gaveta = form_pedidosolucao.cleaned_data["gaveta"]           
            obs = form_pedidosolucao.cleaned_data["obs"]            

            pedidosolucao_novo = pedidosolucao.PedidoSolucao(usuario=usuario, nome=nome, concentracao=concentracao, data_producao=data_producao, unidade=unidade, 
            quantidade=quantidade, status=status, sala=sala, armario=armario, bancada=bancada, estante=estante, prateleira=prateleira, gaveta=gaveta,
            obs=obs)    
            pedidosolucao_service.editar_pedidosolucao(pedidosolucao_antigo, pedidosolucao_novo)

            return redirect('sisnlab:listar_pedidosolucoes')       
    return render(request, 'pedidosolucoes/form_pedidosolucao.html', {'form_pedidosolucao': form_pedidosolucao})  @user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def remover_pedidosolucao(request, id):
    pedidosolucao = pedidosolucao_service.listar_pedidosolucao_id(id)
    if request.method == "POST":
        pedidosolucao_service.remover_pedidosolucao(pedidosolucao)
        return redirect('sisnlab:listar_pedidosolucoes')
    return render(request, 'pedidosolucoes/confirma_exclusao.html', {'pedidosolucao': pedidosolucao})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def visualizar_pedidosolucao(request, id):
    pedidosolucao = pedidosolucao_service.listar_pedidosolucao_id(id)    
    itenspedidosolucao = ItensPedidoSolucao.objects.filter(pedidosolucao_id=id)  
    
    if request.method == "POST":
        pedidosolucao_service.visualizar_pedidosolucao(pedidosolucao)
        return redirect('sisnlab:listar_pedidosolucoes')
    return render(request, 'pedidosolucoes/visualizar.html', {'pedidosolucao': pedidosolucao, 'itenspedidosolucao' : itenspedidosolucao})    

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def itens_pedidosolucoes(request, pedidosolucao_id ):
    pedidosolucao = PedidoSolucao.objects.get(id=pedidosolucao_id)      
    if request.method == "POST":               
        form_itenspedidosolucao = itenspedidosolucao_forms.ItensPedidoSolucaoForm(request.POST)      
        if form_itenspedidosolucao.is_valid():            
            usuario = form_itenspedidosolucao.cleaned_data["usuario"]              
            pedidosolucao_id = form_itenspedidosolucao.cleaned_data["pedidosolucao_id"]   
            reagente = form_itenspedidosolucao.cleaned_data["reagente"]                           
            quantidade = form_itenspedidosolucao.cleaned_data["quantidade"]              

        itenspedidosolucao_novo = itenspedidosolucao.ItensPedidoSolucao(usuario=request.user, pedidosolucao_id=pedidosolucao.id, reagente=reagente, quantidade=quantidade)                       
    
        itenspedidosolucao_service.cadastrar_itenspedidosolucao(itenspedidosolucao_novo)  
        
        form_itenspedidosolucao = itenspedidosolucao_forms.ItensPedidoSolucaoForm()     
           
            
    else:                
        form_itenspedidosolucao = itenspedidosolucao_forms.ItensPedidoSolucaoForm()   

    return render(request, 'pedidosolucoes/cadastraritenssolucao.html', {'form_itenspedidosolucao': form_itenspedidosolucao})

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def visualizar_pedidosolucaoitens(request, id):       
    pedidosolucaoitens = PedidoSolucao.objects.filter(usuario=request.user).last() 
    itenspedidosolucao = ItensPedidoSolucao.objects.filter(pedidosolucao_id=id)  
    
    return redirect('sisnlab:listar_pedidosolucoes')   
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def dar_baixa_estoque(request, id):
    ultimo_id_solucao = PedidoSolucao.objects.filter(usuario=request.user).last() 
    itenspedidosolucao = ItensPedidoSolucao.objects.filter(pedidosolucao_id=ultimo_id_solucao.pk)  
    for item in itenspedidosolucao:
        reagente = Reagente.objects.get(pk=item.reagente_id)
        reagente.quantidade = reagente.quantidade - item.quantidade        
        reagente.save()   
             
    return redirect('sisnlab:listar_pedidosolucoes')    

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/') 
def pega_ultima_solucao(request):
    ultimo_id_solucao = PedidoSolucao.objects.filter(usuario=request.user).last() 
    pedidosolucao = PedidoSolucao.objects.get(id=ultimo_id_solucao.pk)
    itenspedidosolucao = ItensPedidoSolucao.objects.filter(pedidosolucao_id=ultimo_id_solucao.pk)  
    return render(request, 'pedidosolucoes/visualizar.html', {'pedidosolucao': pedidosolucao, 'itenspedidosolucao' : itenspedidosolucao})    


# AJAX
@login_required(login_url='/nlab/login/')
def load_armarios_psolucao(request):
    sala_id = request.GET.get('sala_id')
    armarios = Armario.objects.filter(sala_id=sala_id).all()     
    return render(request, 'pedidosolucoes/armario_dropdown_list_options.html', {'armarios': armarios})

@login_required(login_url='/nlab/login/')
def load_estantes_psolucao(request):
    sala_id = request.GET.get('sala_id')
    estantes = Estante.objects.filter(sala_id=sala_id).all()     
    return render(request, 'pedidosolucoes/estante_dropdown_list_options.html', {'estantes': estantes})

@login_required(login_url='/nlab/login/')
def load_bancadas_psolucao(request):
    sala_id = request.GET.get('sala_id')
    bancadas = Bancada.objects.filter(sala_id=sala_id).all()     
    return render(request, 'pedidosolucoes/bancada_dropdown_list_options.html', {'bancadas': bancadas})

@login_required(login_url='/nlab/login/')
def load_prateleiras_arm_psolucao(request):
    armario_id = request.GET.get('armario_id')
    prateleiras = Prateleira.objects.filter(armario_id=armario_id).all()     
    return render(request, 'pedidosolucoes/prateleira_arm_dropdown_list_options.html', {'prateleiras': prateleiras})

@login_required(login_url='/nlab/login/')
def load_prateleiras_est_psolucao(request):
    estante_id = request.GET.get('estante_id')
    prateleiras = Prateleira.objects.filter(estante_id=estante_id).all()     
    return render(request, 'pedidosolucoes/prateleira_est_dropdown_list_options.html', {'prateleiras': prateleiras})

@login_required(login_url='/nlab/login/')
def load_prateleiras_ban_psolucao(request):
    bancada_id = request.GET.get('bancada_id')
    prateleiras = Prateleira.objects.filter(bancada_id=bancada_id).all()     
    return render(request, 'pedidosolucoes/prateleira_est_dropdown_list_options.html', {'prateleiras': prateleiras})

@login_required(login_url='/nlab/login/')
def load_gavetas_arm_psolucao(request):
    armario_id = request.GET.get('armario_id')
    gavetas = Gaveta.objects.filter(armario_id=armario_id).all()     
    return render(request, 'pedidosolucoes/gaveta_arm_dropdown_list_options.html', {'gavetas': gavetas})

@login_required(login_url='/nlab/login/')
def load_gavetas_est_psolucao(request):
    estante_id = request.GET.get('estante_id')
    gavetas = Gaveta.objects.filter(estante_id=estante_id).all()     
    return render(request, 'pedidosolucoes/gaveta_est_dropdown_list_options.html', {'gavetas': gavetas})

@login_required(login_url='/nlab/login/')
def load_gavetas_ban_psolucao(request):
    bancada_id = request.GET.get('bancada_id')
    gavetas = Gaveta.objects.filter(bancada_id=bancada_id).all()     
    return render(request, 'pedidosolucoes/gaveta_est_dropdown_list_options.html', {'gavetas': gavetas})


  