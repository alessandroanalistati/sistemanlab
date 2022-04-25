import sys
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from ..forms import gaveta_forms
from ..entidades import gaveta
from ..services import gaveta_service
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_gaveta(request):
    gavetas = gaveta_service.listar_gavetas()
    return render(request, 'gavetas/listar_gavetas.html', {'gavetas': gavetas})

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def inserir_gaveta(request):
    if request.method == "POST":
        form_gaveta = gaveta_forms.GavetaForm(request.POST)   
        if form_gaveta.is_valid():
            usuario = form_gaveta.cleaned_data["usuario"]
            nome = form_gaveta.cleaned_data["nome"]
            sigla = form_gaveta.cleaned_data["sigla"]  
            armario = form_gaveta.cleaned_data["armario"]
            bancada = form_gaveta.cleaned_data["bancada"]
            estante = form_gaveta.cleaned_data["estante"]          
            obs = form_gaveta.cleaned_data["obs"]
            gaveta_novo = gaveta.Gaveta(usuario=request.user, nome=nome, sigla=sigla, armario=armario, bancada=bancada, estante=estante, obs=obs)
            gaveta_service.cadastrar_gaveta(gaveta_novo)
            return redirect('sisnlab:listar_gavetas')
    else:
        form_gaveta = gaveta_forms.GavetaForm()      
    return render(request, 'gavetas/form_gaveta.html', {'form_gaveta': form_gaveta})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_gaveta_id(request, id):
    gaveta = gaveta_service.listar_gaveta_id(id)

    return render(request, 'gavetas/lista_gaveta.html', {'gaveta': gaveta})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def editar_gaveta(request, id):
    gaveta_antigo = gaveta_service.listar_gaveta_id(id)
    form_gaveta = gaveta_forms.GavetaForm(request.POST or None, instance=gaveta_antigo)   
    if form_gaveta.is_valid():
        if form_gaveta.is_valid():
            usuario = form_gaveta.cleaned_data["usuario"]
            nome = form_gaveta.cleaned_data["nome"]
            sigla = form_gaveta.cleaned_data["sigla"]  
            armario = form_gaveta.cleaned_data["armario"]
            bancada = form_gaveta.cleaned_data["bancada"]
            estante = form_gaveta.cleaned_data["estante"]          
            obs = form_gaveta.cleaned_data["obs"]
            gaveta_novo = gaveta.Gaveta(usuario=request.user, nome=nome, sigla=sigla, armario=armario, bancada=bancada, estante=estante, obs=obs)
            gaveta_service.editar_gaveta(gaveta_antigo, gaveta_novo)

        return redirect('sisnlab:listar_gavetas')
    return render(request, 'gavetas/form_gaveta.html', {'form_gaveta': form_gaveta})  
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def remover_gaveta(request, id):
    gaveta = gaveta_service.listar_gaveta_id(id)
    if request.method == "POST":
        gaveta_service.remover_gaveta(gaveta)
        return redirect('sisnlab:listar_gavetas')
    return render(request, 'gavetas/confirma_exclusao.html', {'gaveta': gaveta})

