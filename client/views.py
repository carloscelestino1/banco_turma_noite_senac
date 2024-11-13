import requests #Importação para o funcionamento da busca do endereco pelo CEP
from django.shortcuts import render, redirect, get_list_or_404
from .models import client, Endereco
from django.http import JsonResponse

#=================================================================#
#Direcionando os clientes e seus endereços para um lista
def Client_List(request):
    Clients = client.objects.all() #Puxar todos os dados da tabela de clients
    
    return render(request, '', {'Clients':Clients}) #Preencher com o link do html

    #----------------------------------------------------------#

def Endereco_List(request):
    Enderecos = Endereco.object.all()#Puxar todos os dados da tabela de enderoço

    return render(request, '', {'Enderecos':Enderecos}) #Preencher com o link do html
#=================================================================#
def Add_Client(request):
    if request.method == "POST":
        Nome = request.POST.get('nome')
        Telefone = request.POST.get('telefone')
        CPF = request.POST.get('CPF')
        Email = request.POST.get('email')

        client.objects.create(Nome=Nome, Telefone=Telefone, CPF=CPF, Email=Email)

        return redirect('')#falta prencher com o link do html
    return render(request, '')#falta prencher com o link do html

    #----------------------------------------------------------#

def Add_Endereco(request):
    if request.method == 'POST':
        CEP = request.POST.get('CEP')
        Logradouro = request.POST.get('logradouro')
        Cidade  = request.POST.get('cidade')
        UF = request.POST.get('UF')
        Pais = request.POST.get('pais')

        Endereco.objects.create(CEP=CEP, Logradouro=Logradouro, Cidade=Cidade, UF=UF, Pais=Pais)
    
        return redirect('')#falta prencher com o link do html
    return render(request, '')#falta prencher com o link do html
#=================================================================#

                #----Em costrução----#

def Consultar_CEP(request):
    if requests.method == 'GET':
        Cep = requests.GET.get('cep', '')#Vai recuperar o valor do parâmetro 'cep' na URl






