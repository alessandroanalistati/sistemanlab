import sys
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from ..forms import diverso_forms
from ..entidades import diverso
from ..services import diverso_service
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_diverso(request):
    diversos = diverso_service.listar_diversos()
    return render(request, 'diversos/listar_diversos.html', {'diversos': diversos})

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def inserir_diverso(request):
    if request.method == "POST":
        form_diverso = diverso_forms.DiversoForm(request.POST, request.FILES)   
        if form_diverso.is_valid():
            usuario = form_diverso.cleaned_data["usuario"]   
            nome = form_diverso.cleaned_data["nome"]   
            marca = form_diverso.cleaned_data["marca"] 
            unidade = form_diverso.cleaned_data["unidade"]              
            quantidade = form_diverso.cleaned_data["quantidade"]                   
            ficha_tec = form_diverso.cleaned_data["ficha_tec"]                  
            sala = form_diverso.cleaned_data["sala"]
            armario = form_diverso.cleaned_data["armario"]
            bancada = form_diverso.cleaned_data["bancada"]
            estante = form_diverso.cleaned_data["estante"]
            prateleira = form_diverso.cleaned_data["prateleira"]
            gaveta = form_diverso.cleaned_data["gaveta"]                   
            obs = form_diverso.cleaned_data["obs"] 
            foto = form_diverso.cleaned_data["foto"]          

            diverso_novo = diverso.Diverso(usuario=request.user, nome=nome, marca=marca, unidade=unidade, quantidade=quantidade, 
            ficha_tec=ficha_tec, sala=sala, armario=armario, bancada=bancada, estante=estante, prateleira=prateleira, 
            gaveta=gaveta, obs=obs, foto=foto)
            
            
            diverso_service.cadastrar_diverso(diverso_novo)
            return redirect('sisnlab:listar_diversos')
    else:
        form_diverso = diverso_forms.DiversoForm()   
    return render(request, 'diversos/form_diverso.html', {'form_diverso': form_diverso})

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_diverso_id(request, id):
    diverso = diverso_service.listar_diverso_id(id)

    return render(request, 'diversos/lista_diverso.html', {'diverso': diverso})

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def editar_diverso(request, id):
    diverso_antigo = diverso_service.listar_diverso_id(id)
    form_diverso = diverso_forms.DiversoForm(request.POST, request.FILES or None, instance=diverso_antigo)   
    if form_diverso.is_valid():
            usuario = form_diverso.cleaned_data["usuario"]   
            nome = form_diverso.cleaned_data["nome"]   
            marca = form_diverso.cleaned_data["marca"] 
            unidade = form_diverso.cleaned_data["unidade"]              
            quantidade = form_diverso.cleaned_data["quantidade"]                   
            ficha_tec = form_diverso.cleaned_data["ficha_tec"]                  
            sala = form_diverso.cleaned_data["sala"]
            armario = form_diverso.cleaned_data["armario"]
            bancada = form_diverso.cleaned_data["bancada"]
            estante = form_diverso.cleaned_data["estante"]
            prateleira = form_diverso.cleaned_data["prateleira"]
            gaveta = form_diverso.cleaned_data["gaveta"]                   
            obs = form_diverso.cleaned_data["obs"] 
            foto = form_diverso.cleaned_data["foto"]          

            diverso_novo = diverso.Diverso(usuario=request.user, nome=nome, marca=marca, unidade=unidade, quantidade=quantidade, 
            ficha_tec=ficha_tec, sala=sala, armario=armario, bancada=bancada, estante=estante, prateleira=prateleira, 
            gaveta=gaveta, obs=obs, foto=foto)
            
            
            diverso_service.editar_diverso(diverso_antigo, diverso_novo)

            return redirect('sisnlab:listar_diversos')       
    return render(request, 'diversos/form_diverso.html', {'form_diverso': form_diverso})  
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def remover_diverso(request, id):
    diverso = diverso_service.listar_diverso_id(id)
    if request.method == "POST":
        diverso_service.remover_diverso(diverso)
        return redirect('sisnlab:listar_diversos')
    return render(request, 'diversos/confirma_exclusao.html', {'diverso': diverso})

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def visualizar_diverso(request, id):
    diverso = diverso_service.listar_diverso_id(id)
    if request.method == "POST":
        diverso_service.visualizar_diverso(diverso)
        return redirect('sisnlab:listar_diversos')
    return render(request, 'diversos/visualizar.html', {'diverso': diverso})