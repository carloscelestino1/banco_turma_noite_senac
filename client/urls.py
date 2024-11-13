from django.urls import path
from . import views

urlpatterns = [
    path('', views.Client_List, name='Lista_Clientes'),
    path('', views.Endereco_List, name="Lista_Endereco"),
    #====================================================#
    path('', views.Add_Client, name='Adicionando_Cliente'),
    path('', views.Add_Endereco, name='Adicionar_Endereco'),
]
