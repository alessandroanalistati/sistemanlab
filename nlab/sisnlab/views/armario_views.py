import sys
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from ..forms import armario_forms
from ..entidades import armario
from ..services import armario_service
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_armario(request):
    armarios = armario_service.listar_armarios()
    return render(request, 'armarios/listar_armarios.html', {'armarios': armarios})


@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def inserir_armario(request):
    if request.method == "POST":
        form_armario = armario_forms.ArmarioForm(request.POST, request.FILES)   
        if form_armario.is_valid():
            usuario = form_armario.cleaned_data["usuario"]
            nome = form_armario.cleaned_data["nome"]
            sigla = form_armario.cleaned_data["sigla"]
            tombo = form_armario.cleaned_data["tombo"]
            sala = form_armario.cleaned_data["sala"]
            obs = form_armario.cleaned_data["obs"]
            fotoarmario = form_armario.cleaned_data["fotoarmario"] 
            armario_novo = armario.Armario(usuario=request.user, nome=nome, sigla=sigla, tombo=tombo, sala=sala, obs=obs, fotoarmario=fotoarmario)
            armario_service.cadastrar_armario(armario_novo)
            return redirect('sisnlab:listar_armarios')
    else:
        form_armario = armario_forms.ArmarioForm()      
    return render(request, 'armarios/form_armario.html', {'form_armario': form_armario})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_armario_id(request, id):
    armario = armario_service.listar_armario_id(id)

    return render(request, 'armarios/lista_armario.html', {'armario': armario})

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def editar_armario(request, id):
    armario_antigo = armario_service.listar_armario_id(id)
    form_armario = armario_forms.ArmarioForm(request.POST or None, request.FILES or None,  instance=armario_antigo)   
    
    if form_armario.is_valid(): 
         if form_armario.is_valid():      
            usuario = form_armario.cleaned_data["usuario"]
            nome = form_armario.cleaned_data["nome"]
            sigla = form_armario.cleaned_data["sigla"]
            tombo = form_armario.cleaned_data["tombo"]
            sala = form_armario.cleaned_data["sala"]
            obs = form_armario.cleaned_data["obs"]
            fotoarmario = form_armario.cleaned_data["fotoarmario"]                                 
                    
            armario_novo = armario.Armario(usuario=request.user, nome=nome, sigla=sigla, tombo=tombo, sala=sala, obs=obs, fotoarmario=fotoarmario)           
           
            armario_service.editar_armario(armario_antigo, armario_novo)
          

            return redirect('sisnlab:listar_armarios')   
    return render(request, 'armarios/form_armario.html', {'form_armario': form_armario})  


@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def remover_armario(request, id):
    armario = armario_service.listar_armario_id(id)
    if request.method == "POST":
        armario_service.remover_armario(armario)
        return redirect('sisnlab:listar_armarios')
    return render(request, 'armarios/confirma_exclusao.html', {'armario': armario})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def visualizar_armario(request, id):
    armario = armario_service.listar_armario_id(id)
    if request.method == "POST":
        armario_service.remover_armario(armario)
        return redirect('sisnlab:listar_armarios')
    return render(request, 'armarios/visualizar.html', {'armario': armario})





