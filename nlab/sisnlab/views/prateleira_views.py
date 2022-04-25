import sys
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from ..forms import prateleira_forms
from ..entidades import prateleira
from ..services import prateleira_service 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_prateleira(request):
    prateleiras = prateleira_service.listar_prateleiras()
    return render(request, 'prateleiras/listar_prateleiras.html', {'prateleiras': prateleiras})

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def inserir_prateleira(request):
    if request.method == "POST":
        form_prateleira = prateleira_forms.PrateleiraForm(request.POST) 
        if form_prateleira.is_valid():
            usuario = form_prateleira.cleaned_data["usuario"]
            nome = form_prateleira.cleaned_data["nome"]
            sigla = form_prateleira.cleaned_data["sigla"]  
            armario = form_prateleira.cleaned_data["armario"]
            bancada = form_prateleira.cleaned_data["bancada"]
            estante = form_prateleira.cleaned_data["estante"]          
            obs = form_prateleira.cleaned_data["obs"]
            
            prateleira_novo = prateleira.Prateleira(usuario=request.user, nome=nome, sigla=sigla, armario=armario, bancada=bancada, estante=estante, obs=obs)
            prateleira_service.cadastrar_prateleira(prateleira_novo)
            return redirect('sisnlab:listar_prateleiras')
    else:
        form_prateleira = prateleira_forms.PrateleiraForm()      
    return render(request, 'prateleiras/form_prateleira.html', {'form_prateleira': form_prateleira})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_prateleira_id(request, id):
    prateleira = prateleira_service.listar_prateleira_id(id)

    return render(request, 'prateleiras/lista_prateleira.html', {'prateleira': prateleira})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')

def editar_prateleira(request, id):
    prateleira_antigo = prateleira_service.listar_prateleira_id(id)
    form_prateleira = prateleira_forms.PrateleiraForm(request.POST or None, instance=prateleira_antigo)   
    if form_prateleira.is_valid():
            usuario = form_prateleira.cleaned_data["usuario"]
            nome = form_prateleira.cleaned_data["nome"]
            sigla = form_prateleira.cleaned_data["sigla"]  
            armario = form_prateleira.cleaned_data["armario"]
            bancada = form_prateleira.cleaned_data["bancada"]
            estante = form_prateleira.cleaned_data["estante"]          
            obs = form_prateleira.cleaned_data["obs"]
            
            prateleira_novo = prateleira.Prateleira(usuario=request.user, nome=nome, sigla=sigla, armario=armario, bancada=bancada, estante=estante, obs=obs)
            prateleira_service.editar_prateleira(prateleira_antigo, prateleira_novo)
            return redirect('sisnlab:listar_prateleiras')    
    return render(request, 'prateleiras/form_prateleira.html', {'form_prateleira': form_prateleira})  

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def remover_prateleira(request, id):
    prateleira = prateleira_service.listar_prateleira_id(id)
    if request.method == "POST":
        prateleira_service.remover_prateleira(prateleira)
        return redirect('sisnlab:listar_prateleiras')
    return render(request, 'prateleiras/confirma_exclusao.html', {'prateleira': prateleira})

