import sys
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from ..forms import unidade_forms
from ..entidades import unidade
from ..services import unidade_service
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_unidade(request):
    unidades = unidade_service.listar_unidades()
    return render(request, 'unidades/listar_unidades.html', {'unidades': unidades})

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def inserir_unidade(request):
    if request.method == "POST":
        form_unidade = unidade_forms.UnidadeForm(request.POST)   
        if form_unidade.is_valid():
            usuario = form_unidade.cleaned_data["usuario"]
            nome = form_unidade.cleaned_data["nome"]                        
            obs = form_unidade.cleaned_data["obs"]
            unidade_novo = unidade.Unidade(usuario=request.user, nome=nome, obs=obs)
            unidade_service.cadastrar_unidade(unidade_novo)
            return redirect('sisnlab:listar_unidades')
    else:
        form_unidade = unidade_forms.UnidadeForm()      
    return render(request, 'unidades/form_unidade.html', {'form_unidade': form_unidade})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_unidade_id(request, id):
    unidade = unidade_service.listar_unidade_id(id)

    return render(request, 'unidades/lista_unidade.html', {'unidade': unidade})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def editar_unidade(request, id):
    unidade_antigo = unidade_service.listar_unidade_id(id)
    form_unidade = unidade_forms.UnidadeForm(request.POST or None, instance=unidade_antigo)   
    if form_unidade.is_valid():
        if form_unidade.is_valid():
            usuario = form_unidade.cleaned_data["usuario"]
            nome = form_unidade.cleaned_data["nome"]                     
            obs = form_unidade.cleaned_data["obs"]
            unidade_novo = unidade.Unidade(usuario=request.user, nome=nome, obs=obs)
            unidade_service.editar_unidade(unidade_antigo, unidade_novo)

        return redirect('sisnlab:listar_unidades')
    return render(request, 'unidades/form_unidade.html', {'form_unidade': form_unidade})  
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def remover_unidade(request, id):
    unidade = unidade_service.listar_unidade_id(id)
    if request.method == "POST":
        unidade_service.remover_unidade(unidade)
        return redirect('sisnlab:listar_unidades')
    return render(request, 'unidades/confirma_exclusao.html', {'unidade': unidade})

