import sys
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from ..forms import reagente_forms
from ..entidades import reagente
from ..services import reagente_service
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test
from ..models import Armario, Sala, Estante, Bancada, Prateleira, Gaveta

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_reagente(request):
    reagentes = reagente_service.listar_reagentes()
    return render(request, 'reagentes/listar_reagentes.html', {'reagentes': reagentes})

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def inserir_reagente(request):
    if request.method == "POST":
        form_reagente = reagente_forms.ReagenteForm(request.POST, request.FILES)   
        if form_reagente.is_valid():
            usuario = form_reagente.cleaned_data["usuario"]
            nome = form_reagente.cleaned_data["nome"]
            formula_q = form_reagente.cleaned_data["formula_q"]
            grau_p = form_reagente.cleaned_data["grau_p"]
            unidade = form_reagente.cleaned_data["unidade"]                          
            marca = form_reagente.cleaned_data["marca"] 
            quantidade = form_reagente.cleaned_data["quantidade"]
            data_validade = form_reagente.cleaned_data["data_validade"]            
            controle_pfex = form_reagente.cleaned_data["controle_pfex"]
            ficha_tec = form_reagente.cleaned_data["ficha_tec"]
            massamolecular = form_reagente.cleaned_data["massamolecular"]
            densidade = form_reagente.cleaned_data["densidade"]
            disponibilidade = form_reagente.cleaned_data["disponibilidade"]                     
            sala = form_reagente.cleaned_data["sala"]
            armario = form_reagente.cleaned_data["armario"]
            bancada = form_reagente.cleaned_data["bancada"]
            estante = form_reagente.cleaned_data["estante"]
            prateleira = form_reagente.cleaned_data["prateleira"]
            gaveta = form_reagente.cleaned_data["gaveta"]           
            obs = form_reagente.cleaned_data["obs"]
            foto = form_reagente.cleaned_data["foto"]

            reagente_novo = reagente.Reagente(usuario=request.user, nome=nome, formula_q=formula_q, grau_p=grau_p, unidade=unidade, marca=marca, quantidade=quantidade, 
            data_validade=data_validade, controle_pfex=controle_pfex, ficha_tec=ficha_tec, massamolecular=massamolecular, densidade=densidade, disponibilidade=disponibilidade, 
            sala=sala, armario=armario, bancada=bancada, estante=estante, prateleira=prateleira, gaveta=gaveta,
            obs=obs, foto=foto)
            
            reagente_service.cadastrar_reagente(reagente_novo)
            return redirect('sisnlab:listar_reagentes')
    else:
        form_reagente = reagente_forms.ReagenteForm()   
    return render(request, 'reagentes/form_reagente.html', {'form_reagente': form_reagente})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_reagente_id(request, id):
    reagente = reagente_service.listar_reagente_id(id)

    return render(request, 'reagentes/lista_reagente.html', {'reagente': reagente})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def editar_reagente(request, id):
    reagente_antigo = reagente_service.listar_reagente_id(id)
    form_reagente = reagente_forms.ReagenteForm(request.POST or None, request.FILES or None, instance=reagente_antigo)   
    if form_reagente.is_valid():
            usuario = form_reagente.cleaned_data["usuario"]
            nome = form_reagente.cleaned_data["nome"]
            formula_q = form_reagente.cleaned_data["formula_q"]
            grau_p = form_reagente.cleaned_data["grau_p"]
            unidade = form_reagente.cleaned_data["unidade"]                          
            marca = form_reagente.cleaned_data["marca"] 
            quantidade = form_reagente.cleaned_data["quantidade"]
            data_validade = form_reagente.cleaned_data["data_validade"]            
            controle_pfex = form_reagente.cleaned_data["controle_pfex"]
            ficha_tec = form_reagente.cleaned_data["ficha_tec"]
            massamolecular = form_reagente.cleaned_data["massamolecular"]
            densidade = form_reagente.cleaned_data["densidade"]
            disponibilidade = form_reagente.cleaned_data["disponibilidade"]                     
            sala = form_reagente.cleaned_data["sala"]
            armario = form_reagente.cleaned_data["armario"]
            bancada = form_reagente.cleaned_data["bancada"]
            estante = form_reagente.cleaned_data["estante"]
            prateleira = form_reagente.cleaned_data["prateleira"]
            gaveta = form_reagente.cleaned_data["gaveta"]           
            obs = form_reagente.cleaned_data["obs"]
            foto = form_reagente.cleaned_data["foto"]

            reagente_novo = reagente.Reagente(usuario=request.user, nome=nome, formula_q=formula_q, grau_p=grau_p, unidade=unidade, marca=marca, quantidade=quantidade, 
            data_validade=data_validade, controle_pfex=controle_pfex, ficha_tec=ficha_tec, massamolecular=massamolecular, densidade=densidade, disponibilidade=disponibilidade, 
            sala=sala, armario=armario, bancada=bancada, estante=estante, prateleira=prateleira, gaveta=gaveta,
            obs=obs, foto=foto)
               
            reagente_service.editar_reagente(reagente_antigo, reagente_novo)

            return redirect('sisnlab:listar_reagentes')       
    return render(request, 'reagentes/form_reagente.html', {'form_reagente': form_reagente})  

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def remover_reagente(request, id):
    reagente = reagente_service.listar_reagente_id(id)
    if request.method == "POST":
        reagente_service.remover_reagente(reagente)
        return redirect('sisnlab:listar_reagentes')
    return render(request, 'reagentes/confirma_exclusao.html', {'reagente': reagente})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def visualizar_reagente(request, id):
    reagente = reagente_service.listar_reagente_id(id)
    if request.method == "POST":
        reagente_service.visualizar_reagente(reagente)
        return redirect('sisnlab:listar_reagentes')
    return render(request, 'reagentes/visualizar.html', {'reagente': reagente})


# AJAX
@login_required(login_url='/nlab/login/')
def load_armarios_produtos(request):
    sala_id = request.GET.get('sala_id')
    armarios = Armario.objects.filter(sala_id=sala_id).all()     
    return render(request, 'reagentes/armario_dropdown_list_options.html', {'armarios': armarios})

@login_required(login_url='/nlab/login/')
def load_estantes_produtos(request):
    sala_id = request.GET.get('sala_id')
    estantes = Estante.objects.filter(sala_id=sala_id).all()     
    return render(request, 'reagentes/estante_dropdown_list_options.html', {'estantes': estantes})

@login_required(login_url='/nlab/login/')
def load_bancadas_produtos(request):
    sala_id = request.GET.get('sala_id')
    bancadas = Bancada.objects.filter(sala_id=sala_id).all()     
    return render(request, 'reagentes/bancada_dropdown_list_options.html', {'bancadas': bancadas})

@login_required(login_url='/nlab/login/')
def load_prateleiras_arm_produtos(request):
    armario_id = request.GET.get('armario_id')
    prateleiras = Prateleira.objects.filter(armario_id=armario_id).all()     
    return render(request, 'reagentes/prateleira_arm_dropdown_list_options.html', {'prateleiras': prateleiras})

@login_required(login_url='/nlab/login/')
def load_prateleiras_est_produtos(request):
    estante_id = request.GET.get('estante_id')
    prateleiras = Prateleira.objects.filter(estante_id=estante_id).all()     
    return render(request, 'reagentes/prateleira_est_dropdown_list_options.html', {'prateleiras': prateleiras})

@login_required(login_url='/nlab/login/')
def load_prateleiras_ban_produtos(request):
    bancada_id = request.GET.get('bancada_id')
    prateleiras = Prateleira.objects.filter(bancada_id=bancada_id).all()     
    return render(request, 'reagentes/prateleira_est_dropdown_list_options.html', {'prateleiras': prateleiras})

@login_required(login_url='/nlab/login/')
def load_gavetas_arm_produtos(request):
    armario_id = request.GET.get('armario_id')
    gavetas = Gaveta.objects.filter(armario_id=armario_id).all()     
    return render(request, 'reagentes/gaveta_arm_dropdown_list_options.html', {'gavetas': gavetas})

@login_required(login_url='/nlab/login/')
def load_gavetas_est_produtos(request):
    estante_id = request.GET.get('estante_id')
    gavetas = Gaveta.objects.filter(estante_id=estante_id).all()     
    return render(request, 'reagentes/gaveta_est_dropdown_list_options.html', {'gavetas': gavetas})

@login_required(login_url='/nlab/login/')
def load_gavetas_ban_produtos(request):
    bancada_id = request.GET.get('bancada_id')
    gavetas = Gaveta.objects.filter(bancada_id=bancada_id).all()     
    return render(request, 'reagentes/gaveta_est_dropdown_list_options.html', {'gavetas': gavetas})
