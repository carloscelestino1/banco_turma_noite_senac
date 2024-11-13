import requests #Importação para o funcionamento da busca do endereco pelo CEP
from django.shortcuts import render, redirect, get_list_or_404
from .models import client, Endereco
from django.http import JsonResponse

#=================================================================#
#Direcionando os clientes e seus endereços para um lista
def Client_List(request):
    clients = client.objects.all() #Puxar todos os dados da tabela de clients
    
    return render(request, '', {'clients':clients}) #Preencher com o link do html

    #----------------------------------------------------------#

def Endereco_List(request):
    enderecos = Endereco.object.all()#Puxar todos os dados da tabela de enderoço

    return render(request, '', {'enderecos':enderecos}) #Preencher com o link do html
#=================================================================#
def Add_Client(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        CPF = request.POST.get('CPF')
        email = request.POST.get('email')

        client.objects.create(nome=nome, telefone=telefone, CPF=CPF, email=email)

        return redirect('')#falta prencher com o link do html
    return render(request, '')#falta prencher com o link do html

    #----------------------------------------------------------#

def Add_Endereco(request):
    if request.method == 'POST':
        CEP = request.POST.get('CEP')
        logradouro = request.POST.get('logradouro')
        cidade  = request.POST.get('cidade')
        UF = request.POST.get('UF')
        pais = request.POST.get('pais')

        Endereco.objects.create(CEP=CEP, logradouro=logradouro, cidade=cidade, UF=UF, pais=pais)
    
        return redirect('')#falta prencher com o link do html
    return render(request, '')#falta prencher com o link do html
#=================================================================#

                #----Em costrução----#

def Consultar_CEP(request):
    if requests.method == 'GET':
        cep = requests.GET.get('cep', '')#Vai recuperar o valor do parâmetro 'cep' na URl






