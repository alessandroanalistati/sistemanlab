import sys
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from ..forms import aulapratica_forms
from ..forms import itensaulapratica_forms
from ..forms import equipamentosaulapratica_forms
from ..forms import solucaoaulapratica_forms
from ..entidades import aulapratica
from ..entidades import itensaulapratica
from ..entidades import equipamentosaulapratica
from ..entidades import solucaoaulapratica
from ..services import aulapratica_service
from ..services import itensaulapratica_service
from ..services import equipamentosaulapratica_service
from ..services import solucaoaulapratica_service
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from ..models import AulaPratica
from ..models import ItensAulaPratica
from ..models import Reagente
from ..models import Solucao
from ..models import AulaPratica
from ..models import EquipamentosAulaPratica
from ..models import SolucaoAulaPratica
from ..models import User

import smtplib as smtp


#from sisnlab.utils import sendemail


@login_required(login_url='/nlab/login/')
def listar_aulapratica(request):
    aulapraticas = aulapratica_service.listar_aulapraticas()
    return render(request, 'aulapraticas/listar_aulapraticas.html', {'aulapraticas': aulapraticas})

@login_required(login_url='/nlab/login/')
def inserir_aulapratica(request):
    if request.method == "POST":
        form_aulapratica = aulapratica_forms.AulaPraticaForm(
            request.POST, request.FILES)
        if form_aulapratica.is_valid():
            usuario = form_aulapratica.cleaned_data["usuario"]
            nome = form_aulapratica.cleaned_data["nome"]
            sala = form_aulapratica.cleaned_data["sala"]
            data_inicio = form_aulapratica.cleaned_data["data_inicio"]
            horario_inicio = form_aulapratica.cleaned_data["horario_inicio"]
            horario_fim = form_aulapratica.cleaned_data["horario_fim"]
            quantalunos = form_aulapratica.cleaned_data["quantalunos"]
            obs = form_aulapratica.cleaned_data["obs"]
            status = form_aulapratica.cleaned_data["status"]

            aulapratica_novo = aulapratica.AulaPratica(usuario=request.user, nome=nome, sala=sala, data_inicio=data_inicio, 
            horario_inicio=horario_inicio, horario_fim=horario_fim, quantalunos=quantalunos, obs=obs, status=status)

            aulapratica_service.cadastrar_aulapratica(aulapratica_novo)

            aulapratica_novo = AulaPratica.objects.filter(usuario=request.user).last()

            return render(request, 'aulapraticas/itensaulapratica.html', {'aulapratica_novo': aulapratica_novo})
    else:
        form_aulapratica = aulapratica_forms.AulaPraticaForm()
    return render(request, 'aulapraticas/form_aulapratica.html', {'form_aulapratica': form_aulapratica})


@login_required(login_url='/nlab/login/')
def listar_aulapratica_id(request, id):
    aulapratica = aulapratica_service.listar_aulapratica_id(id)

    return render(request, 'aulapraticas/lista_aulapratica.html', {'aulapratica': aulapratica})


@login_required(login_url='/nlab/login/')
def editar_aulapratica(request, id):
    aulapratica_antigo = aulapratica_service.listar_aulapratica_id(id)
    form_aulapratica = aulapratica_forms.AulaPraticaForm(
        request.POST or None, instance=aulapratica_antigo)
    if form_aulapratica.is_valid():
            usuario = form_aulapratica.cleaned_data["usuario"]
            nome = form_aulapratica.cleaned_data["nome"]
            sala = form_aulapratica.cleaned_data["sala"]
            data_inicio = form_aulapratica.cleaned_data["data_inicio"]
            horario_inicio = form_aulapratica.cleaned_data["horario_inicio"]
            horario_fim = form_aulapratica.cleaned_data["horario_fim"]            
            quantalunos = form_aulapratica.cleaned_data["quantalunos"]
            obs = form_aulapratica.cleaned_data["obs"]
            status = form_aulapratica.cleaned_data["status"]

            aulapratica_novo = aulapratica.AulaPratica(usuario=request.user, nome=nome, sala=sala, data_inicio=data_inicio, horario_inicio=horario_inicio,
            horario_fim=horario_fim, quantalunos=quantalunos, obs=obs, status=status)
            
            aulapratica_service.editar_aulapratica( aulapratica_antigo, aulapratica_novo)

            aulapratica_novo = AulaPratica.objects.filter(
                usuario=request.user).last()

            return render(request, 'aulapraticas/itensaulapratica.html', {'aulapratica_novo': aulapratica_novo})

    return render(request, 'aulapraticas/form_aulapratica.html', {'form_aulapratica': form_aulapratica})


@login_required(login_url='/nlab/login/')
def editar_aulapraticanovamente(request, id):
    aulapratica_antigo = aulapratica_service.listar_aulapratica_id(id)
    form_aulapratica = aulapratica_forms.AulaPraticaForm(
        request.POST or None, instance=aulapratica_antigo)
    if form_aulapratica.is_valid():
            usuario = form_aulapratica.cleaned_data["usuario"]
            nome = form_aulapratica.cleaned_data["nome"]
            sala = form_aulapratica.cleaned_data["sala"]
            data_inicio = form_aulapratica.cleaned_data["data_inicio"]
            horario_inicio = form_aulapratica.cleaned_data["horario_inicio"]
            horario_fim = form_aulapratica.cleaned_data["horario_fim"]
            quantalunos = form_aulapratica.cleaned_data["quantalunos"]
            obs = form_aulapratica.cleaned_data["obs"]
            status = form_aulapratica.cleaned_data["status"]

            aulapratica_novo = aulapratica.AulaPratica(usuario=request.user, nome=nome, sala=sala, data_inicio=data_inicio, horario_inicio=horario_inicio,
            horario_fim=horario_fim, quantalunos=quantalunos, obs=obs, status=status)
            aulapratica_service.editar_aulapratica(aulapratica_antigo, aulapratica_novo)

            aulapratica_novo = AulaPratica.objects.filter(usuario=request.user).last()

            return render(request, 'aulapraticas/itensaulapratica.html', {'aulapratica_novo': aulapratica_novo})

    return render(request, 'aulapraticas/form_aulapratica.html', {'form_aulapratica': form_aulapratica})


@login_required(login_url='/nlab/login/')
def remover_aulapratica(request, id):
    aulapratica = aulapratica_service.listar_aulapratica_id(id)
    if request.method == "POST":
        aulapratica_service.remover_aulapratica(aulapratica)
        return redirect('sisnlab:listar_aulapraticas')
    return render(request, 'aulapraticas/confirma_exclusao.html', {'aulapratica': aulapratica})


@login_required(login_url='/nlab/login/')
def visualizar_aulapratica(request, id):
    aulapratica = aulapratica_service.listar_aulapratica_id(id)
    itensaulapratica = ItensAulaPratica.objects.filter(aulapratica_id=id)
    equipamentosaulapratica = EquipamentosAulaPratica.objects.filter(aulapratica_id=id)
    solucaoaulapratica = SolucaoAulaPratica.objects.filter(aulapratica_id=id)

    if request.method == "POST":
        aulapratica_service.visualizar_aulapratica(aulapratica)
        return redirect('sisnlab:listar_aulapraticas')

    return render(request, 'aulapraticas/visualizar.html', {'aulapratica': aulapratica, 'itensaulapratica': itensaulapratica, 'equipamentosaulapratica': equipamentosaulapratica,
        'solucaoaulapratica': solucaoaulapratica})


@login_required(login_url='/nlab/login/')
def visualizar_aulapratica_editar(request, id):
    aulapratica = aulapratica_service.listar_aulapratica_id(id)
    itensaulapratica = ItensAulaPratica.objects.filter(aulapratica_id=id)
    equipamentosaulapratica = EquipamentosAulaPratica.objects.filter(aulapratica_id=id)
    solucaoaulapratica = SolucaoAulaPratica.objects.filter(aulapratica_id=id)

    if request.method == "POST":
        aulapratica_service.visualizar_aulapratica(aulapratica)
        return redirect('sisnlab:listar_aulapraticas')

    return render(request, 'aulapraticas/visualizar_editar.html', {'aulapratica': aulapratica, 'itensaulapratica': itensaulapratica, 'equipamentosaulapratica': equipamentosaulapratica,
        'solucaoaulapratica': solucaoaulapratica})


@login_required(login_url='/nlab/login/')
def produtos_aulapraticas(request, aulapratica_id):
    aulapratica = AulaPratica.objects.get(id=aulapratica_id)
    if request.method == "POST":
        form_itensaulapratica = itensaulapratica_forms.ItensAulaPraticaForm(
            request.POST)
        if form_itensaulapratica.is_valid():
            usuario = form_itensaulapratica.cleaned_data["usuario"]
            aulapratica_id = form_itensaulapratica.cleaned_data["aulapratica_id"]
            reagente = form_itensaulapratica.cleaned_data["reagente"]
            quant_reagente = form_itensaulapratica.cleaned_data["quant_reagente"]

        itensaulapratica_novo = itensaulapratica.ItensAulaPratica(usuario=request.user, aulapratica_id=aulapratica.id,
            reagente=reagente, quant_reagente=quant_reagente)

        itensaulapratica_service.cadastrar_itensaulapratica(
            itensaulapratica_novo)

        aulapratica_novo = AulaPratica.objects.filter(
            usuario=request.user).last()
        return render(request, 'aulapraticas/itensaulapratica.html', {'aulapratica_novo': aulapratica_novo})

    else:
        form_itensaulapratica = itensaulapratica_forms.ItensAulaPraticaForm()
    return render(request, 'aulapraticas/cadastrariprodutosaula.html', {'form_itensaulapratica': form_itensaulapratica})


@login_required(login_url='/nlab/login/')
def equipamentos_aulapraticas(request, aulapratica_id):
    aulapratica = AulaPratica.objects.get(id=aulapratica_id)
    if request.method == "POST":
        form_equipamentosaulapratica = equipamentosaulapratica_forms.EquipamentosAulaPraticaForm(
            request.POST)
        if form_equipamentosaulapratica.is_valid():
            usuario = form_equipamentosaulapratica.cleaned_data["usuario"]
            aulapratica_id = form_equipamentosaulapratica.cleaned_data["aulapratica_id"]
            equipamentos = form_equipamentosaulapratica.cleaned_data["equipamentos"]
            quant_equipamentos = form_equipamentosaulapratica.cleaned_data["quant_equipamentos"]

        equipamentosaulapratica_novo = equipamentosaulapratica.EquipamentosAulaPratica(
            usuario=request.user, aulapratica_id=aulapratica.id, equipamentos=equipamentos, quant_equipamentos=quant_equipamentos)

        equipamentosaulapratica_service.cadastrar_equipamentosAulaPratica(
            equipamentosaulapratica_novo)
        aulapratica_novo = AulaPratica.objects.filter(
            usuario=request.user).last()
        return render(request, 'aulapraticas/itensaulapratica.html', {'aulapratica_novo': aulapratica_novo})

    else:
        form_equipamentosaulapratica = equipamentosaulapratica_forms.EquipamentosAulaPraticaForm()
    return render(request, 'aulapraticas/cadastrarequipamentosaula.html', {'form_equipamentosaulapratica': form_equipamentosaulapratica})


@login_required(login_url='/nlab/login/')
def solucoes_aulapraticas(request, aulapratica_id):
    aulapratica = AulaPratica.objects.get(id=aulapratica_id)
    if request.method == "POST":
        form_solucaoaulapratica = solucaoaulapratica_forms.SolucaoAulaPraticaForm(
            request.POST)
        if form_solucaoaulapratica.is_valid():
            usuario = form_solucaoaulapratica.cleaned_data["usuario"]
            aulapratica_id = form_solucaoaulapratica.cleaned_data["aulapratica_id"]
            solucao = form_solucaoaulapratica.cleaned_data["solucao"]
            quant_solucao = form_solucaoaulapratica.cleaned_data["quant_solucao"]

        solucaoaulapratica_novo = solucaoaulapratica.SolucaoAulaPratica(
            usuario=request.user, aulapratica_id=aulapratica.id, solucao=solucao, quant_solucao=quant_solucao)

        solucaoaulapratica_service.cadastrar_solucaoaulapratica(
            solucaoaulapratica_novo)
        aulapratica_novo = AulaPratica.objects.filter(
            usuario=request.user).last()
        return render(request, 'aulapraticas/itensaulapratica.html', {'aulapratica_novo': aulapratica_novo})

    else:
        form_solucaoaulapratica = solucaoaulapratica_forms.SolucaoAulaPraticaForm()
    return render(request, 'aulapraticas/cadastrarsolucaoaula.html', {'form_solucaoaulapratica': form_solucaoaulapratica})


@login_required(login_url='/nlab/login/')
def visualizar_aulapraticaitens(request, id):
    aulapraticaitens = AulaPratica.objects.filter(usuario=request.user).last()
    itensaulapratica = ItensAulaPratica.objects.filter(aulapratica_id=id)
    equipamentosaulapratica = EquipamentosAulaPratica.objects.filter(
        aulapratica_id=id)

    return redirect('sisnlab:listar_aulapraticas')


def pega_ultima_solucao(request):
    ultimo_id_solucao = AulaPratica.objects.filter(usuario=request.user).last()
    aulapratica = AulaPratica.objects.get(id=ultimo_id_solucao.pk)
    itensaulapratica = ItensAulaPratica.objects.filter(
        aulapratica_id=ultimo_id_solucao.pk)
    equipamentosaulapratica = EquipamentosAulaPratica.objects.filter(
        aulapratica_id=ultimo_id_solucao.pk)
    solucaoaulapratica = SolucaoAulaPratica.objects.filter(
        aulapratica_id=ultimo_id_solucao.pk)
    return render(request, 'aulapraticas/visualizar.html', {'aulapratica': aulapratica, 'itensaulapratica': itensaulapratica, 'equipamentosaulapratica': equipamentosaulapratica,
        'solucaoaulapratica': solucaoaulapratica})


@login_required(login_url='/nlab/login/')
def remover_itensaulapratica(request, id):
    itensaulapratica_remover = itensaulapratica_service.remover_itensaulapratica_id(
        id)

    ultimo_id_aulapratica = AulaPratica.objects.filter(
        usuario=request.user).last()
    aulapratica = AulaPratica.objects.get(id=ultimo_id_aulapratica.pk)
    itensaulapratica = ItensAulaPratica.objects.filter(
        aulapratica_id=ultimo_id_aulapratica.pk)
    equipamentosaulapratica = EquipamentosAulaPratica.objects.filter(
        aulapratica_id=ultimo_id_aulapratica.pk)
    solucaoaulapratica = SolucaoAulaPratica.objects.filter(
        aulapratica_id=ultimo_id_aulapratica.pk)

    if request.method == "POST":
        aulapratica_service.visualizar_aulapratica(aulapratica)
        return redirect('sisnlab:listar_aulapraticas')

    return render(request, 'aulapraticas/visualizar_editar.html', {'aulapratica': aulapratica, 'itensaulapratica': itensaulapratica, 'equipamentosaulapratica': equipamentosaulapratica,
        'solucaoaulapratica': solucaoaulapratica})


@login_required(login_url='/nlab/login/')
def remover_solucaoaulapratica(request, id):
    solucao_remover = solucaoaulapratica_service.remover_solucao_aula_id(id)

    ultimo_id_aulapratica = AulaPratica.objects.filter(
        usuario=request.user).last()
    aulapratica = AulaPratica.objects.get(id=ultimo_id_aulapratica.pk)
    itensaulapratica = ItensAulaPratica.objects.filter(
        aulapratica_id=ultimo_id_aulapratica.pk)
    equipamentosaulapratica = EquipamentosAulaPratica.objects.filter(
        aulapratica_id=ultimo_id_aulapratica.pk)
    solucaoaulapratica = SolucaoAulaPratica.objects.filter(
        aulapratica_id=ultimo_id_aulapratica.pk)

    if request.method == "POST":
        aulapratica_service.visualizar_aulapratica(aulapratica)
        return redirect('sisnlab:listar_aulapraticas')

    return render(request, 'aulapraticas/visualizar_editar.html', {'aulapratica': aulapratica, 'itensaulapratica': itensaulapratica, 'equipamentosaulapratica': equipamentosaulapratica,
        'solucaoaulapratica': solucaoaulapratica})


@login_required(login_url='/nlab/login/')
def remover_equipamentosaulapratica(request, id):
    equipamento_remover = equipamentosaulapratica_service.remover_equipamentos_aula_id(
        id)

    ultimo_id_aulapratica = AulaPratica.objects.filter(
        usuario=request.user).last()
    aulapratica = AulaPratica.objects.get(id=ultimo_id_aulapratica.pk)
    itensaulapratica = ItensAulaPratica.objects.filter(
        aulapratica_id=ultimo_id_aulapratica.pk)
    equipamentosaulapratica = EquipamentosAulaPratica.objects.filter(
        aulapratica_id=ultimo_id_aulapratica.pk)
    solucaoaulapratica = SolucaoAulaPratica.objects.filter(
        aulapratica_id=ultimo_id_aulapratica.pk)

    if request.method == "POST":
        aulapratica_service.visualizar_aulapratica(aulapratica)
        return redirect('sisnlab:listar_aulapraticas')

    return render(request, 'aulapraticas/visualizar_editar.html', {'aulapratica': aulapratica, 'itensaulapratica': itensaulapratica, 'equipamentosaulapratica': equipamentosaulapratica,
        'solucaoaulapratica': solucaoaulapratica})


def enviar_email():      
    de = "nlabifbaianoitapetinga@gmail.com" # Usuário do GMail para envio
    senha = 'ifbaiano@2020' # Senha
    para =  ["nlabifbaianoitapetinga@gmail.com"]# Destinatário
    mensagem = "Subject: Teste-SISNLAB\n\nCriado pedido de aula Pratica SISNLAB" # Mensagem a ser enviada
    try:
        with smtp.SMTP('smtp.gmail.com', 587) as s:
            s.starttls()
            s.login(de, senha) # Efetuando login com o usuário e senha
            s.sendmail(de, para, mensagem) # Enviando e-mail
            s.close() # Fechando a conexão
        print("E-mail enviado!")
    except Exception as erro:
        print("Não foi possível enviar o e-mail. Erro:", erro)
        
if __name__ == '__main__':
        enviar_email()
        
        
@login_required(login_url='/nlab/login/')
def listar_aulapratica_email(request):
    aulapraticas = aulapratica_service.listar_aulapraticas()    
    enviar_email()    
    
    return render(request, 'aulapraticas/listar_aulapraticas.html', {'aulapraticas': aulapraticas})
    
@login_required(login_url='/nlab/login/')
def dar_saida_aula_pratica(request, id):
    ultimo_id_aulapratica = AulaPratica.objects.filter(usuario=request.user).last()
    itensprodutos = ItensAulaPratica.objects.filter(aulapratica_id=ultimo_id_aulapratica.pk)
    itenssolucoes = SolucaoAulaPratica.objects.filter(aulapratica_id=ultimo_id_aulapratica.pk)    
   # itensequipamentos = ItensAulaPratica.objects.filter(saida_id=ultimo_id_saida.pk) Não precisa dar baixa
    aulapratica = aulapratica_service.listar_aulapratica_id(id)
    itensaulapratica = ItensAulaPratica.objects.filter(aulapratica_id=id)
    equipamentosaulapratica = EquipamentosAulaPratica.objects.filter(aulapratica_id=id)
    solucaoaulapratica = SolucaoAulaPratica.objects.filter(aulapratica_id=id)

    for item1 in itensprodutos:
        reagente = Reagente.objects.get(pk=item1.reagente_id)
        reagente.quantidade = reagente.quantidade - item1.quant_reagente
        reagente.save()

    for item2 in itenssolucoes:
        solucao = Solucao.objects.get(pk=item2.solucao_id)
        solucao.quantidade = solucao.quantidade - item2.quant_solucao
        solucao.save()
        
    enviar_email()   

    if request.method == "POST":
        aulapratica_service.visualizar_aulapratica(aulapratica)
        return redirect('sisnlab:listar_aulapraticas')

    return render(request, 'pdf/visualizar_pdf.html', {'aulapratica': aulapratica, 'itensaulapratica': itensaulapratica, 'equipamentosaulapratica': equipamentosaulapratica,
        'solucaoaulapratica': solucaoaulapratica})


