from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from ..forms.tombo_forms import TomboForm
from ..entidades import tombo
from ..services import tombo_service
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_tombo(request):
    tombos = tombo_service.listar_tombos()
    return render(request, 'tombos/listar_tombos.html', {'tombos': tombos})

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def inserir_tombo(request):
    if request.method == "POST":
        form = TomboForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data["usuario"]
            numero = form.cleaned_data["numero"]
            descricao = form.cleaned_data["descricao"]

            tombo_novo = tombo.Tombo(usuario=request.user, numero=numero, descricao=descricao)
            tombo_service.cadastrar_tombo(tombo_novo)

            return redirect('sisnlab:listar_tombos')
    else:
        form = TomboForm()
    return render(request, 'tombos/form_tombo.html', {'form': form})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_tombo_id(request, id):
    tombo = tombo_service.listar_tombo_id(id)

    return render(request, 'tombos/lista_tombo.html', {'tombo': tombo})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def editar_tombo(request, id):
    tombo_antigo = tombo_service.listar_tombo_id(id)
    form = TomboForm(request.POST or None, instance=tombo_antigo)
    if form.is_valid():
        usuario = form.cleaned_data["usuario"]
        numero = form.cleaned_data["numero"]
        descricao = form.cleaned_data["descricao"]

        tombo_novo = tombo.Tombo(usuario=request.user, numero=numero, descricao=descricao)
        tombo_service.editar_tombo(tombo_antigo, tombo_novo)
        return redirect('sisnlab:listar_tombos')
    return render(request, 'tombos/form_tombo.html', {'form': form})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def remover_tombo(request, id):
    tombo = tombo_service.listar_tombo_id(id)
    if request.method == "POST":
        tombo_service.remover_tombo(tombo)
        return redirect('sisnlab:listar_tombos')
    return render(request, 'tombos/confirma_exclusao.html', {'tombo': tombo})

