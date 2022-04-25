import sys
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from ..forms import fornecedor_forms
from ..entidades import fornecedor
from ..services import fornecedor_service
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_fornecedor(request):
    fornecedores = fornecedor_service.listar_fornecedores()
    return render(request, 'fornecedores/listar_fornecedores.html', {'fornecedores': fornecedores})


@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def inserir_fornecedor(request):
    if request.method == "POST":
        form_fornecedor = fornecedor_forms.FornecedorForm(request.POST, request.FILES)   
        if form_fornecedor.is_valid():
            usuario = form_fornecedor.cleaned_data["usuario"]
            nome = form_fornecedor.cleaned_data["nome"]
            cnpj = form_fornecedor.cleaned_data["cnpj"]
            cpf = form_fornecedor.cleaned_data["cpf"]
            data_cadastro = form_fornecedor.cleaned_data["data_cadastro"]
            endereco = form_fornecedor.cleaned_data["endereco"]
            telefone = form_fornecedor.cleaned_data["telefone"]
            cel = form_fornecedor.cleaned_data["cel"]
            email = form_fornecedor.cleaned_data["email"]
            obs = form_fornecedor.cleaned_data["obs"] 
            
            fornecedor_novo = fornecedor.Fornecedor(usuario=request.user, nome=nome, cnpj=cnpj, cpf=cpf, data_cadastro=data_cadastro, 
                endereco=endereco, telefone=telefone, cel=cel, email=email, obs=obs )
            fornecedor_service.cadastrar_fornecedor(fornecedor_novo)
            return redirect('sisnlab:listar_fornecedores')
    else:
        form_fornecedor = fornecedor_forms.FornecedorForm()      
    return render(request, 'fornecedores/form_fornecedor.html', {'form_fornecedor': form_fornecedor})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_fornecedor_id(request, id):
    fornecedor = fornecedor_service.listar_fornecedor_id(id)

    return render(request, 'fornecedores/lista_fornecedor.html', {'fornecedor': fornecedor})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def editar_fornecedor(request, id):
    fornecedor_antigo = fornecedor_service.listar_fornecedor_id(id)
    form_fornecedor = fornecedor_forms.FornecedorForm(request.POST or None, instance=fornecedor_antigo)   
    if form_fornecedor.is_valid():
        if form_fornecedor.is_valid():
            usuario = form_fornecedor.cleaned_data["usuario"]
            nome = form_fornecedor.cleaned_data["nome"]
            cnpj = form_fornecedor.cleaned_data["cnpj"]
            cpf = form_fornecedor.cleaned_data["cpf"]
            data_cadastro = form_fornecedor.cleaned_data["data_cadastro"]
            endereco = form_fornecedor.cleaned_data["endereco"]
            telefone = form_fornecedor.cleaned_data["telefone"]
            cel = form_fornecedor.cleaned_data["cel"]
            email = form_fornecedor.cleaned_data["email"]
            obs = form_fornecedor.cleaned_data["obs"] 
            
            fornecedor_novo = fornecedor.Fornecedor(usuario=request.user, nome=nome, cnpj=cnpj, cpf=cpf, data_cadastro=data_cadastro,
                endereco=endereco, telefone=telefone, cel=cel, email=email, obs=obs )            
                
            fornecedor_service.editar_fornecedor(fornecedor_antigo, fornecedor_novo)

        return redirect('sisnlab:listar_fornecedores')
    return render(request, 'fornecedores/form_fornecedor.html', {'form_fornecedor': form_fornecedor})  
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def remover_fornecedor(request, id):
    fornecedor = fornecedor_service.listar_fornecedor_id(id)
    if request.method == "POST":
        fornecedor_service.remover_fornecedor(fornecedor)
        return redirect('sisnlab:listar_fornecedores')
    return render(request, 'fornecedores/confirma_exclusao.html', {'fornecedor': fornecedor})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def visualizar_fornecedor(request, id):
    fornecedor = fornecedor_service.listar_fornecedor_id(id)
    if request.method == "POST":
        fornecedor_service.remover_fornecedor(fornecedor)
        return redirect('sisnlab:listar_fornecedores')
    return render(request, 'fornecedores/visualizar.html', {'fornecedor': fornecedor})





