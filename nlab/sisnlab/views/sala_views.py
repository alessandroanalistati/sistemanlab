from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from ..forms.sala_forms import SalaForm
from ..entidades import sala
from ..services import sala_service
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_sala(request):
    salas = sala_service.listar_salas()
    return render(request, 'salas/listar_salas.html', {'salas': salas})

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def inserir_sala(request):
    if request.method == "POST":
        form = SalaForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data["usuario"]
            nome = form.cleaned_data["nome"]
            obs = form.cleaned_data["obs"]

            sala_nova = sala.Sala(usuario=request.user, nome=nome, obs=obs)
            sala_service.cadastrar_sala(sala_nova)

            return redirect('sisnlab:listar_salas')
    else:
        form = SalaForm()
    return render(request, 'salas/form_sala.html', {'form': form})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_sala_id(request, id):
    sala = sala_service.listar_sala_id(id)

    return render(request, 'salas/lista_sala.html', {'sala': sala})

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def editar_sala(request, id):
    sala_antiga = sala_service.listar_sala_id(id)
    form = SalaForm(request.POST or None, instance=sala_antiga)
    if form.is_valid():
        usuario = form.cleaned_data["usuario"]
        nome = form.cleaned_data["nome"]
        obs = form.cleaned_data["obs"]

        sala_nova = sala.Sala(usuario=request.user, nome=nome, obs=obs)
        sala_service.editar_sala(sala_antiga, sala_nova)
        return redirect('sisnlab:listar_salas')
    return render(request, 'salas/form_sala.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def remover_sala(request, id):
    sala = sala_service.listar_sala_id(id)
    if request.method == "POST":
        sala_service.remover_sala(sala)
        return redirect('sisnlab:listar_salas')
    return render(request, 'salas/confirma_exclusao.html', {'sala': sala})






