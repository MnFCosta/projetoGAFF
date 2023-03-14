from django.db import models
from django.utils import timezone


# Create your models here.
class componenteFamilia(models.Model):
    nome = models.CharField(max_length=200, default=None)
    cpf = models.CharField(max_length=45, default=None, verbose_name="CPF")
    rg = models.CharField(max_length=45,default=None,verbose_name="RG")
    #variáveis de papéis
    PAI = 'PAI'
    MAE = 'MÃE'
    FILHO = 'FILHO/FILHA'
    ESCOLHAS_PAPEL = [
        (PAI, 'Pai'),
        (MAE, 'Mãe'),
        (FILHO, 'Filho/Filha'),
    ]
    papel = models.CharField(
        max_length=11,
        choices=ESCOLHAS_PAPEL,
        default=PAI,
    )
    nascimento = models.DateField(default=None)
    NR_calcado = models.CharField(max_length=50)
    NR_roupa = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Integrante de Família"
        verbose_name_plural = "Integrantes de Família"

class Familia(models.Model):
    nome = models.CharField(max_length=200, default=None)
    componentes = models.ManyToManyField(componenteFamilia, verbose_name="Composição")
    rua = models.CharField(max_length=200)
    numero = models.CharField(max_length=30)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    unidade_federativa = models.CharField(max_length=2)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    cep = models.CharField(max_length=20, verbose_name="CEP")
    celular = models.CharField(max_length=45)
    moradia = models.CharField(max_length=45)
    casa_de = models.CharField(max_length=45)
    condicoes_casa = models.CharField(max_length=45,)
    aluguel = models.DecimalField(max_digits=20, decimal_places=2)
    data_cadastro = models.DateTimeField(default=timezone.now)
    realizado_por = models.CharField(max_length=100)
    observacao = models.TextField()

    def __str__(self):
        return self.nome
    
