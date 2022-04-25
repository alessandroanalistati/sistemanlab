import sys
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from ..forms import vidraria_forms
from ..entidades import vidraria
from ..services import vidraria_service
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_vidraria(request):
    vidrarias = vidraria_service.listar_vidrarias()
    return render(request, 'vidrarias/listar_vidrarias.html', {'vidrarias': vidrarias})

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def inserir_vidraria(request):
    if request.method == "POST":
        form_vidraria = vidraria_forms.VidrariaForm(request.POST, request.FILES)   
        if form_vidraria.is_valid():
            usuario = form_vidraria.cleaned_data["usuario"]                   
            nome = form_vidraria.cleaned_data["nome"]                   
            marca = form_vidraria.cleaned_data["marca"]            
            data_compra = form_vidraria.cleaned_data["data_compra"]            
            origem = form_vidraria.cleaned_data["origem"]
            ficha_tec = form_vidraria.cleaned_data["ficha_tec"]
            especficacao_t = form_vidraria.cleaned_data["especficacao_t"]
            quantidade = form_vidraria.cleaned_data["quantidade"]
            sala = form_vidraria.cleaned_data["sala"]
            armario = form_vidraria.cleaned_data["armario"]
            bancada = form_vidraria.cleaned_data["bancada"]
            estante = form_vidraria.cleaned_data["estante"]
            prateleira = form_vidraria.cleaned_data["prateleira"]
            gaveta = form_vidraria.cleaned_data["gaveta"]           
            obs = form_vidraria.cleaned_data["obs"]
            foto = form_vidraria.cleaned_data["foto"]

            vidraria_novo = vidraria.Vidraria(usuario=request.user, nome=nome, marca=marca, data_compra=data_compra, origem=origem, ficha_tec=ficha_tec, 
            especficacao_t=especficacao_t, quantidade=quantidade, sala=sala, armario=armario, bancada=bancada, 
            estante=estante, prateleira=prateleira, gaveta=gaveta, obs=obs, foto=foto)
            
            vidraria_service.cadastrar_vidraria(vidraria_novo)
            return redirect('sisnlab:listar_vidrarias')
    else:
        form_vidraria = vidraria_forms.VidrariaForm()   
    return render(request, 'vidrarias/form_vidraria.html', {'form_vidraria': form_vidraria})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def listar_vidraria_id(request, id):
    vidraria = vidraria_service.listar_vidraria_id(id)

    return render(request, 'vidrarias/lista_vidraria.html', {'vidraria': vidraria})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def editar_vidraria(request, id):
    vidraria_antigo = vidraria_service.listar_vidraria_id(id)
    form_vidraria = vidraria_forms.VidrariaForm(request.POST or None,  request.FILES or None, instance=vidraria_antigo)   
    if form_vidraria.is_valid():
            usuario = form_vidraria.cleaned_data["usuario"]                   
            nome = form_vidraria.cleaned_data["nome"]                   
            marca = form_vidraria.cleaned_data["marca"]            
            data_compra = form_vidraria.cleaned_data["data_compra"]            
            origem = form_vidraria.cleaned_data["origem"]
            ficha_tec = form_vidraria.cleaned_data["ficha_tec"]
            especficacao_t = form_vidraria.cleaned_data["especficacao_t"]
            quantidade = form_vidraria.cleaned_data["quantidade"]
            sala = form_vidraria.cleaned_data["sala"]
            armario = form_vidraria.cleaned_data["armario"]
            bancada = form_vidraria.cleaned_data["bancada"]
            estante = form_vidraria.cleaned_data["estante"]
            prateleira = form_vidraria.cleaned_data["prateleira"]
            gaveta = form_vidraria.cleaned_data["gaveta"]           
            obs = form_vidraria.cleaned_data["obs"]
            foto = form_vidraria.cleaned_data["foto"]

            vidraria_novo = vidraria.Vidraria(usuario=request.user, nome=nome, marca=marca, data_compra=data_compra, origem=origem, ficha_tec=ficha_tec, 
            especficacao_t=especficacao_t, quantidade=quantidade, sala=sala, armario=armario, bancada=bancada, 
            estante=estante, prateleira=prateleira, gaveta=gaveta, obs=obs, foto=foto)

            vidraria_service.editar_vidraria(vidraria_antigo, vidraria_novo)
            return redirect('sisnlab:listar_vidrarias')
        
    return render(request, 'vidrarias/form_vidraria.html', {'form_vidraria': form_vidraria})  
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def remover_vidraria(request, id):
    vidraria = vidraria_service.listar_vidraria_id(id)
    if request.method == "POST":
        vidraria_service.remover_vidraria(vidraria)
        return redirect('sisnlab:listar_vidrarias')
    return render(request, 'vidrarias/confirma_exclusao.html', {'vidraria': vidraria})
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/nlab/login/')
def visualizar_vidraria(request, id):
    vidraria = vidraria_service.listar_vidraria_id(id)
    if request.method == "POST":
        vidraria_service.visualizar_vidraria(vidraria)
        return redirect('sisnlab:listar_vidrarias')
    return render(request, 'vidrarias/visualizar.html', {'vidraria': vidraria})


# form_vidraria = vidraria_forms.EquipamentoForm( initial={"armario": "1", "bancada": "1", "estante": "1", "prateleira": "1", "gaveta": "1",})   