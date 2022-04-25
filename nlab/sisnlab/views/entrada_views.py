import sys
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from ..forms import entrada_forms
from ..forms import itensentrada_forms
from ..entidades import entrada
from ..entidades import itensentrada
from ..services import entrada_service
from ..services import itensentrada_service
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from ..models import Entrada
from ..models import ItensEntrada
from ..models import Reagente
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_entrada(request):
    entradas = entrada_service.listar_entradas()
    return render(request, 'entradas/listar_entradas.html', {'entradas': entradas})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def inserir_entrada(request):
    if request.method == "POST":
        form_entrada = entrada_forms.EntradaForm(request.POST, request.FILES)      
        if form_entrada.is_valid():            
            usuario = form_entrada.cleaned_data["usuario"]
            nf = form_entrada.cleaned_data["nf"]
            fornecedor = form_entrada.cleaned_data["fornecedor"]
            data_cadastro = form_entrada.cleaned_data["data_cadastro"]             
            nf_foto = form_entrada.cleaned_data["nf_foto"]             
            obs = form_entrada.cleaned_data["obs"]          

            entrada_novo = entrada.Entrada(usuario=request.user, nf=nf, fornecedor=fornecedor, data_cadastro=data_cadastro,
                nf_foto=nf_foto, obs=obs)
                       
            entrada_service.cadastrar_entrada(entrada_novo) 
                   
            entrada_novo = Entrada.objects.filter(usuario=request.user).last()
            
            return render(request, 'entradas/itens_entrada.html', {'entrada_novo': entrada_novo})  
    else:
        form_entrada = entrada_forms.EntradaForm()   
    return render(request, 'entradas/form_entrada.html', {'form_entrada': form_entrada})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_entrada_id(request, id):
    entrada = entrada_service.listar_entrada_id(id)

    return render(request, 'entradas/lista_entrada.html', {'entrada': entrada})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def editar_entrada(request, id):
    entrada_antigo = entrada_service.listar_entrada_id(id)
    form_entrada = entrada_forms.EntradaForm(request.POST or None,  request.FILES or None, instance=entrada_antigo)   
    if form_entrada.is_valid():
        if form_entrada.is_valid():        
            usuario = form_entrada.cleaned_data["usuario"]
            nf = form_entrada.cleaned_data["nf"]
            fornecedor = form_entrada.cleaned_data["fornecedor"]
            data_cadastro = form_entrada.cleaned_data["data_cadastro"]             
            nf_foto = form_entrada.cleaned_data["nf_foto"]             
            obs = form_entrada.cleaned_data["obs"]          

            entrada_novo = entrada.Entrada(usuario=request.user, nf=nf, fornecedor=fornecedor, data_cadastro=data_cadastro,
                nf_foto=nf_foto, obs=obs)
            entrada_service.editar_entrada(entrada_antigo, entrada_novo)



            return redirect('sisnlab:listar_entradas')       
    return render(request, 'entradas/form_entrada.html', {'form_entrada': form_entrada})  @user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def remover_entrada(request, id):
    entrada = entrada_service.listar_entrada_id(id)
    if request.method == "POST":
        entrada_service.remover_entrada(entrada)
        return redirect('sisnlab:listar_entradas')
    return render(request, 'entradas/confirma_exclusao.html', {'entrada': entrada})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def visualizar_entrada(request, id):
    entrada = entrada_service.listar_entrada_id(id)    
    itensentrada = ItensEntrada.objects.filter(entrada_id=id)  
    
    if request.method == "POST":
        entrada_service.visualizar_entrada(entrada)
        return redirect('sisnlab:listar_entradas')
    return render(request, 'entradas/visualizar.html', {'entrada': entrada, 'itensentrada' : itensentrada})    

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def itens_entradas(request, entrada_id ):
    entrada = Entrada.objects.get(id=entrada_id)      
    if request.method == "POST":               
        form_itensentrada = itensentrada_forms.ItensEntradaForm(request.POST)      
        if form_itensentrada.is_valid():            
            usuario = form_itensentrada.cleaned_data["usuario"]              
            entrada_id = form_itensentrada.cleaned_data["entrada_id"]   
            reagente = form_itensentrada.cleaned_data["reagente"]
            unidade = form_itensentrada.cleaned_data["unidade"]                   
            quantidade = form_itensentrada.cleaned_data["quantidade"]              

        itensentrada_novo = itensentrada.ItensEntrada(usuario=request.user, entrada_id=entrada.id, reagente=reagente, unidade=unidade, 
        quantidade=quantidade)                    
    
        itensentrada_service.cadastrar_itensentrada(itensentrada_novo)  
        form_itensentrada = itensentrada_forms.ItensEntradaForm()            
            
    else:                
        form_itensentrada = itensentrada_forms.ItensEntradaForm()   

    return render(request, 'entradas/cadastrar_itens_entrada.html', {'form_itensentrada': form_itensentrada})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def visualizar_entradaitens(request, id):       
    entradaitens = Entrada.objects.filter(usuario=request.user).last() 
    itensentrada = ItensEntrada.objects.filter(entrada_id=id)  
    
    return redirect('sisnlab:listar_entradas')    


def dar_entrada_estoque(request, id):
    ultimo_id_entrada = Entrada.objects.filter(usuario=request.user).last() 
    itensentrada = ItensEntrada.objects.filter(entrada_id=ultimo_id_entrada.pk)  
    for item in itensentrada:
        reagente = Reagente.objects.get(pk=item.reagente_id)
        reagente.quantidade = reagente.quantidade + item.quantidade        
        reagente.save()   
             
    return redirect('sisnlab:pega_entrada')  
 
def pega_ultima_entrada(request):
    ultimo_id_entrada = Entrada.objects.filter(usuario=request.user).last() 
    entrada = Entrada.objects.get(id=ultimo_id_entrada.pk)
    itensentrada = ItensEntrada.objects.filter(entrada_id=ultimo_id_entrada.pk)  
    return render(request, 'entradas/visualizar.html', {'entrada': entrada, 'itensentrada' : itensentrada})    

  
  