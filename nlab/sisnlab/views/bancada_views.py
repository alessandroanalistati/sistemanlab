import sys
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from ..forms import bancada_forms
from ..entidades import bancada
from ..services import bancada_service
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_bancada(request):
    bancadas = bancada_service.listar_bancadas()
    return render(request, 'bancadas/listar_bancadas.html', {'bancadas': bancadas})

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def inserir_bancada(request):
    if request.method == "POST":
        form_bancada = bancada_forms.BancadaForm(request.POST)   
        if form_bancada.is_valid():
            usuario = form_bancada.cleaned_data["usuario"]
            nome = form_bancada.cleaned_data["nome"]
            sigla = form_bancada.cleaned_data["sigla"]
            tombo = form_bancada.cleaned_data["tombo"]
            sala = form_bancada.cleaned_data["sala"]
            obs = form_bancada.cleaned_data["obs"]
            bancada_novo = bancada.Bancada(usuario=request.user, nome=nome, sigla=sigla, tombo=tombo, sala=sala, obs=obs)
            bancada_service.cadastrar_bancada(bancada_novo)
            return redirect('sisnlab:listar_bancadas')
    else:
        form_bancada = bancada_forms.BancadaForm()      
    return render(request, 'bancadas/form_bancada.html', {'form_bancada': form_bancada})

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_bancada_id(request, id):
    bancada = bancada_service.listar_bancada_id(id)

    return render(request, 'bancadas/lista_bancada.html', {'bancada': bancada})

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def editar_bancada(request, id):
    bancada_antigo = bancada_service.listar_bancada_id(id)
    form_bancada = bancada_forms.BancadaForm(request.POST or None, instance=bancada_antigo)   
    if form_bancada.is_valid():
        if form_bancada.is_valid():
            usuario = form_bancada.cleaned_data["usuario"]
            nome = form_bancada.cleaned_data["nome"]
            sigla = form_bancada.cleaned_data["sigla"]
            tombo = form_bancada.cleaned_data["tombo"]
            sala = form_bancada.cleaned_data["sala"]
            obs = form_bancada.cleaned_data["obs"]
            bancada_novo = bancada.Bancada(usuario=request.user, nome=nome, sigla=sigla, tombo=tombo, sala=sala, obs=obs)
            bancada_service.editar_bancada(bancada_antigo, bancada_novo)

        return redirect('sisnlab:listar_bancadas')
    return render(request, 'bancadas/form_bancada.html', {'form_bancada': form_bancada})  

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def remover_bancada(request, id):
    bancada = bancada_service.listar_bancada_id(id)
    if request.method == "POST":
        bancada_service.remover_bancada(bancada)
        return redirect('sisnlab:listar_bancadas')
    return render(request, 'bancadas/confirma_exclusao.html', {'bancada': bancada})

