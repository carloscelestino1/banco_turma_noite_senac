from django.db import models

class client(models.Model):
    Nome = models.CharField(max_length=100)
    Telefone = models.IntegerField()
    CPF = models.CharField(max_length=11)
    Email = models.EmailField()

    def __str__(self):
        return self.Nome

#==============================================#
class Endereco(models.Model):
    Client = models.ForeignKey(client, on_delete=models.CASCADE, related_name='enderecos') # Adicionando a ForeignKey
    CEP = models.CharField(max_length=8)
    Logradouro = models.CharField(max_length=150)
    Cidade = models.CharField(max_length=50)
    UF = models.CharField(max_length=2)
    Pais =models.CharField(max_length=35)

    def __str__(self):
        return f"{self.Logradouro}, {self.Cidade} - {self.UF}"

#==============================================#











