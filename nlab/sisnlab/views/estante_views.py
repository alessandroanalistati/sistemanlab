import sys
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from ..forms import estante_forms
from ..entidades import estante
from ..services import estante_service
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_estante(request):
    estantes = estante_service.listar_estantes()
    return render(request, 'estantes/listar_estantes.html', {'estantes': estantes})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def inserir_estante(request):
    if request.method == "POST":
        form_estante = estante_forms.EstanteForm(request.POST)   
        if form_estante.is_valid():
            usuario = form_estante.cleaned_data["usuario"]
            nome = form_estante.cleaned_data["nome"]
            sigla = form_estante.cleaned_data["sigla"]
            tombo = form_estante.cleaned_data["tombo"]
            sala = form_estante.cleaned_data["sala"]
            obs = form_estante.cleaned_data["obs"]
            estante_novo = estante.Estante(usuario=request.user, nome=nome, sigla=sigla, tombo=tombo, sala=sala, obs=obs)
            estante_service.cadastrar_estante(estante_novo)
            return redirect('sisnlab:listar_estantes')
    else:
        form_estante = estante_forms.EstanteForm()      
    return render(request, 'estantes/form_estante.html', {'form_estante': form_estante})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_estante_id(request, id):
    estante = estante_service.listar_estante_id(id)

    return render(request, 'estantes/lista_estante.html', {'estante': estante})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def editar_estante(request, id):
    estante_antigo = estante_service.listar_estante_id(id)
    form_estante = estante_forms.EstanteForm(request.POST or None, instance=estante_antigo)   
    if request.method == "POST":
        form_estante = estante_forms.EstanteForm(request.POST)   
        if form_estante.is_valid():
            usuario = form_estante.cleaned_data["usuario"]
            nome = form_estante.cleaned_data["nome"]
            sigla = form_estante.cleaned_data["sigla"]
            tombo = form_estante.cleaned_data["tombo"]
            sala = form_estante.cleaned_data["sala"]
            obs = form_estante.cleaned_data["obs"]
            estante_novo = estante.Estante(usuario=request.user, nome=nome, sigla=sigla, tombo=tombo, sala=sala, obs=obs)
            estante_service.editar_estante(estante_antigo, estante_novo)

        return redirect('sisnlab:listar_estantes')
    return render(request, 'estantes/form_estante.html', {'form_estante': form_estante})  
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def remover_estante(request, id):
    estante = estante_service.listar_estante_id(id)
    if request.method == "POST":
        estante_service.remover_estante(estante)
        return redirect('sisnlab:listar_estantes')
    return render(request, 'estantes/confirma_exclusao.html', {'estante': estante})

