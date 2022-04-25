import sys
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from ..forms import solucao_forms
from ..entidades import solucao
from ..services import solucao_service
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_solucao(request):
    solucoes = solucao_service.listar_solucoes()
    return render(request, 'solucoes/listar_solucoes.html', {'solucoes': solucoes})

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def inserir_solucao(request):
    if request.method == "POST":
        form_solucao = solucao_forms.SolucaoForm(request.POST)   
        if form_solucao.is_valid():
            usuario = form_solucao.cleaned_data["usuario"] 
            nome = form_solucao.cleaned_data["nome"]     
            quantidade = form_solucao.cleaned_data["quantidade"]       
            sala = form_solucao.cleaned_data["sala"]            
            armario = form_solucao.cleaned_data["armario"]
            bancada = form_solucao.cleaned_data["bancada"]
            estante = form_solucao.cleaned_data["estante"]
            prateleira = form_solucao.cleaned_data["prateleira"]
            gaveta = form_solucao.cleaned_data["gaveta"]           
            obs = form_solucao.cleaned_data["obs"]
                        
            solucao_novo = solucao.Solucao(usuario=request.user, nome=nome, quantidade=quantidade, sala=sala,  armario=armario, bancada=bancada, 
                estante=estante, prateleira=prateleira, gaveta=gaveta, obs=obs)
            
            solucao_service.cadastrar_solucao(solucao_novo)
            
            return redirect('sisnlab:listar_solucoes')
    else:
        form_solucao = solucao_forms.SolucaoForm()   
        
    return render(request, 'solucoes/form_solucao.html', {'form_solucao': form_solucao})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_solucao_id(request, id):
    solucao = solucao_service.listar_solucao_id(id)

    return render(request, 'solucoes/lista_solucao.html', {'solucao': solucao})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def editar_solucao(request, id):
    solucao_antigo = solucao_service.listar_solucao_id(id)
    form_solucao = solucao_forms.SolucaoForm(request.POST or None, instance=solucao_antigo)   
    if form_solucao.is_valid():
        if form_solucao.is_valid():
            usuario = form_solucao.cleaned_data["usuario"] 
            nome = form_solucao.cleaned_data["nome"]            
            quantidade = form_solucao.cleaned_data["quantidade"]       
            sala = form_solucao.cleaned_data["sala"]            
            armario = form_solucao.cleaned_data["armario"]
            bancada = form_solucao.cleaned_data["bancada"]
            estante = form_solucao.cleaned_data["estante"]
            prateleira = form_solucao.cleaned_data["prateleira"]
            gaveta = form_solucao.cleaned_data["gaveta"]           
            obs = form_solucao.cleaned_data["obs"]
                        
            solucao_novo = solucao.Solucao(usuario=request.user, nome=nome, quantidade=quantidade, sala=sala,  armario=armario, bancada=bancada, 
                estante=estante, prateleira=prateleira, gaveta=gaveta, obs=obs)
            
            
            solucao_service.editar_solucao(solucao_antigo, solucao_novo)

            return redirect('sisnlab:listar_solucoes')
        
    return render(request, 'solucoes/form_solucao.html', {'form_solucao': form_solucao})  
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def remover_solucao(request, id):
    solucao = solucao_service.listar_solucao_id(id)
    if request.method == "POST":
        solucao_service.remover_solucao(solucao)
        return redirect('sisnlab:listar_solucoes')
    return render(request, 'solucoes/confirma_exclusao.html', {'solucao': solucao})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def visualizar_solucao(request, id):
    solucao = solucao_service.listar_solucao_id(id)
    if request.method == "POST":
        solucao_service.visualizar_solucao(solucao)
        return redirect('sisnlab:listar_solucoes')
    return render(request, 'solucoes/visualizar.html', {'solucao': solucao})


# form_solucao = solucao_forms.SolucaoForm( initial={"armario": "1", "bancada": "1", "estante": "1", "prateleira": "1", "gaveta": "1",})   