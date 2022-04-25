import sys
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from ..forms import marca_forms
from ..entidades import marca
from ..services import marca_service
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_marca(request):
    marcas = marca_service.listar_marcas()
    return render(request, 'marcas/listar_marcas.html', {'marcas': marcas})

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def inserir_marca(request):
    if request.method == "POST":
        form_marca = marca_forms.MarcaForm(request.POST)   
        if form_marca.is_valid():
            usuario = form_marca.cleaned_data["usuario"]
            nome = form_marca.cleaned_data["nome"]                        
            obs = form_marca.cleaned_data["obs"]
            marca_novo = marca.Marca(usuario=request.user, nome=nome, obs=obs)
            marca_service.cadastrar_marca(marca_novo)
            return redirect('sisnlab:listar_marcas')
    else:
        form_marca = marca_forms.MarcaForm()      
    return render(request, 'marcas/form_marca.html', {'form_marca': form_marca})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_marca_id(request, id):
    marca = marca_service.listar_marca_id(id)

    return render(request, 'marcas/lista_marca.html', {'marca': marca})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def editar_marca(request, id):
    marca_antigo = marca_service.listar_marca_id(id)
    form_marca = marca_forms.MarcaForm(request.POST or None, instance=marca_antigo)   
    if form_marca.is_valid():
        if form_marca.is_valid():
            usuario = form_marca.cleaned_data["usuario"]
            nome = form_marca.cleaned_data["nome"]                     
            obs = form_marca.cleaned_data["obs"]
            marca_novo = marca.Marca(usuario=request.user, nome=nome, obs=obs)
            marca_service.editar_marca(marca_antigo, marca_novo)

        return redirect('sisnlab:listar_marcas')
    return render(request, 'marcas/form_marca.html', {'form_marca': form_marca})  
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def remover_marca(request, id):
    marca = marca_service.listar_marca_id(id)
    if request.method == "POST":
        marca_service.remover_marca(marca)
        return redirect('sisnlab:listar_marcas')
    return render(request, 'marcas/confirma_exclusao.html', {'marca': marca})

