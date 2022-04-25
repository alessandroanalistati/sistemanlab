import sys
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from ..forms import saida_forms
from ..forms import itenssaida_forms
from ..entidades import saida
from ..entidades import itenssaida
from ..services import saida_service
from ..services import itenssaida_service
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from ..models import Saida
from ..models import ItensSaida
from ..models import Reagente
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_saida(request):
    saidas = saida_service.listar_saidas()
    return render(request, 'saidas/listar_saidas.html', {'saidas': saidas})

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def inserir_saida(request):
    if request.method == "POST":
        form_saida = saida_forms.SaidaForm(request.POST, request.FILES)      
        if form_saida.is_valid():            
            usuario = form_saida.cleaned_data["usuario"]
            nf = form_saida.cleaned_data["nf"]
            destinatario = form_saida.cleaned_data["destinatario"]
            data_cadastro = form_saida.cleaned_data["data_cadastro"]             
            nf_foto = form_saida.cleaned_data["nf_foto"]             
            obs = form_saida.cleaned_data["obs"]          

            saida_novo = saida.Saida(usuario=request.user, nf=nf, destinatario=destinatario, data_cadastro=data_cadastro,
                nf_foto=nf_foto, obs=obs)
                       
            saida_service.cadastrar_saida(saida_novo) 
                   
            saida_novo = Saida.objects.filter(usuario=request.user).last()
            
            return render(request, 'saidas/itens_saida.html', {'saida_novo': saida_novo})  
    else:
        form_saida = saida_forms.SaidaForm()   
    return render(request, 'saidas/form_saida.html', {'form_saida': form_saida})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_saida_id(request, id):
    saida = saida_service.listar_saida_id(id)

    return render(request, 'saidas/lista_saida.html', {'saida': saida})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def editar_saida(request, id):
    saida_antigo = saida_service.listar_saida_id(id)
    form_saida = saida_forms.SaidaForm(request.POST or None, instance=saida_antigo)   
    if form_saida.is_valid():
            usuario = form_saida.cleaned_data["usuario"]
            nf = form_saida.cleaned_data["nf"]
            destinatario = form_saida.cleaned_data["destinatario"]
            data_cadastro = form_saida.cleaned_data["data_cadastro"]             
            nf_foto = form_saida.cleaned_data["nf_foto"]             
            obs = form_saida.cleaned_data["obs"]          

            saida_novo = saida.Saida(usuario=request.user, nf=nf, destinatario=destinatario, data_cadastro=data_cadastro,
                nf_foto=nf_foto, obs=obs)
            saida_service.editar_saida(saida_antigo, saida_novo)

            return redirect('sisnlab:listar_saidas')       
    return render(request, 'saidas/form_saida.html', {'form_saida': form_saida})  @user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def remover_saida(request, id):
    saida = saida_service.listar_saida_id(id)
    if request.method == "POST":
        saida_service.remover_saida(saida)
        return redirect('sisnlab:listar_saidas')
    return render(request, 'saidas/confirma_exclusao.html', {'saida': saida})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def visualizar_saida(request, id):
    saida = saida_service.listar_saida_id(id)    
    itenssaida = ItensSaida.objects.filter(saida_id=id)  
    
    if request.method == "POST":
        saida_service.visualizar_saida(saida)
        return redirect('sisnlab:listar_saidas')
    return render(request, 'saidas/visualizar.html', {'saida': saida, 'itenssaida' : itenssaida})   

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def itens_saidas(request, saida_id ):
    saida = Saida.objects.get(id=saida_id)      
    if request.method == "POST":               
        form_itenssaida = itenssaida_forms.ItensSaidaForm(request.POST)      
        if form_itenssaida.is_valid():            
            usuario = form_itenssaida.cleaned_data["usuario"]              
            saida_id = form_itenssaida.cleaned_data["saida_id"]   
            reagente = form_itenssaida.cleaned_data["reagente"]
            unidade = form_itenssaida.cleaned_data["unidade"]                   
            quantidade = form_itenssaida.cleaned_data["quantidade"]              

        itenssaida_novo = itenssaida.ItensSaida(usuario=request.user, saida_id=saida.id, reagente=reagente, unidade=unidade, 
        quantidade=quantidade)                    
    
        itenssaida_service.cadastrar_itenssaida(itenssaida_novo)  
        form_itenssaida = itenssaida_forms.ItensSaidaForm()            
            
    else:                
        form_itenssaida = itenssaida_forms.ItensSaidaForm()   

    return render(request, 'saidas/cadastrar_itens_saida.html', {'form_itenssaida': form_itenssaida})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def visualizar_saidaitens(request, id):       
    saidaitens = Saida.objects.filter(usuario=request.user).last() 
    itenssaida = ItensSaida.objects.filter(saida_id=id)  
    
    return redirect('sisnlab:listar_saidas')    

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def dar_saida_estoque(request, id):
    ultimo_id_saida = Saida.objects.filter(usuario=request.user).last() 
    itenssaida = ItensSaida.objects.filter(saida_id=ultimo_id_saida.pk)  
    for item in itenssaida:
        reagente = Reagente.objects.get(pk=item.reagente_id)
        reagente.quantidade = reagente.quantidade - item.quantidade        
        reagente.save()   
             
    return redirect('sisnlab:pega_saida')  
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def pega_ultima_saida(request):
    ultimo_id_saida = Saida.objects.filter(usuario=request.user).last() 
    saida = Saida.objects.get(id=ultimo_id_saida.pk)
    itenssaida = ItensSaida.objects.filter(saida_id=ultimo_id_saida.pk)  
    return render(request, 'saidas/visualizar.html', {'saida': saida, 'itenssaida' : itenssaida})    

  
  