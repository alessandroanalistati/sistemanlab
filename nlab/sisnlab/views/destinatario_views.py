import sys
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from ..forms import destinatario_forms
from ..entidades import destinatario
from ..services import destinatario_service
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_destinatario(request):
    destinatarios = destinatario_service.listar_destinatarios()
    return render(request, 'destinatarios/listar_destinatarios.html', {'destinatarios': destinatarios})

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def inserir_destinatario(request):
    if request.method == "POST":
        form_destinatario = destinatario_forms.DestinatarioForm(request.POST, request.FILES)   
        if form_destinatario.is_valid():
            usuario = form_destinatario.cleaned_data["usuario"]
            nome = form_destinatario.cleaned_data["nome"]
            cnpj = form_destinatario.cleaned_data["cnpj"]
            cpf = form_destinatario.cleaned_data["cpf"]
            data_cadastro = form_destinatario.cleaned_data["data_cadastro"]
            endereco = form_destinatario.cleaned_data["endereco"]
            telefone = form_destinatario.cleaned_data["telefone"]
            cel = form_destinatario.cleaned_data["cel"]
            email = form_destinatario.cleaned_data["email"]
            obs = form_destinatario.cleaned_data["obs"] 
            
            destinatario_novo = destinatario.Destinatario(usuario=request.user, nome=nome, cnpj=cnpj, cpf=cpf, data_cadastro=data_cadastro, 
                endereco=endereco, telefone=telefone, cel=cel, email=email, obs=obs )
            destinatario_service.cadastrar_destinatario(destinatario_novo)
            return redirect('sisnlab:listar_destinatarios')
    else:
        form_destinatario = destinatario_forms.DestinatarioForm()      
    return render(request, 'destinatarios/form_destinatario.html', {'form_destinatario': form_destinatario})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_destinatario_id(request, id):
    destinatario = destinatario_service.listar_destinatario_id(id)

    return render(request, 'destinatarios/lista_destinatario.html', {'destinatario': destinatario})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def editar_destinatario(request, id):
    destinatario_antigo = destinatario_service.listar_destinatario_id(id)
    form_destinatario = destinatario_forms.DestinatarioForm(request.POST or None, instance=destinatario_antigo)   
    if form_destinatario.is_valid():
        if form_destinatario.is_valid():
            usuario = form_destinatario.cleaned_data["usuario"]
            nome = form_destinatario.cleaned_data["nome"]
            cnpj = form_destinatario.cleaned_data["cnpj"]
            cpf = form_destinatario.cleaned_data["cpf"]
            data_cadastro = form_destinatario.cleaned_data["data_cadastro"]
            endereco = form_destinatario.cleaned_data["endereco"]
            telefone = form_destinatario.cleaned_data["telefone"]
            cel = form_destinatario.cleaned_data["cel"]
            email = form_destinatario.cleaned_data["email"]
            obs = form_destinatario.cleaned_data["obs"] 
            
            destinatario_novo = destinatario.Destinatario(usuario=request.user, nome=nome, cnpj=cnpj, cpf=cpf, data_cadastro=data_cadastro,
                endereco=endereco, telefone=telefone, cel=cel, email=email, obs=obs )            
                
            destinatario_service.editar_destinatario(destinatario_antigo, destinatario_novo)

        return redirect('sisnlab:listar_destinatarios')
    return render(request, 'destinatarios/form_destinatario.html', {'form_destinatario': form_destinatario})  
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def remover_destinatario(request, id):
    destinatario = destinatario_service.listar_destinatario_id(id)
    if request.method == "POST":
        destinatario_service.remover_destinatario(destinatario)
        return redirect('sisnlab:listar_destinatarios')
    return render(request, 'destinatarios/confirma_exclusao.html', {'destinatario': destinatario})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def visualizar_destinatario(request, id):
    destinatario = destinatario_service.listar_destinatario_id(id)
    if request.method == "POST":
        destinatario_service.remover_destinatario(destinatario)
        return redirect('sisnlab:listar_destinatarios')
    return render(request, 'destinatarios/visualizar.html', {'destinatario': destinatario})





