from django.db import models
from django.db.models import CASCADE
from django.forms import ValidationError
from django.utils import timezone
from django.core.validators import MinValueValidator

ESCOLHAS_PAPEL = (
        ('Pai', 'Pai'),
        ('Mãe', 'Mãe'),
        ('Filho/Filha', 'Filho/Filha'),
)

ESCOLHAS_MORADIA = (
        ('Própria', 'Própria'),
        ('Alugada', 'Alugada'),
        
)

ESCOLHAS_MATERIAL = (
        ('Alvenaria', 'Alvenaria'),
        ('Madeira', 'Madeira'),
        ('Mista', 'Mista'),
        ('Barraco', 'Barraco'),
        
)

ESCOLHAS_CONDICOES = (
        ('Excelente', 'Excelente'),
        ('Boa', 'Boa'),
        ('Ruim', 'Ruim'),
        ('Péssima', 'Péssima'),
        
)

# Create your models here.
class componenteFamilia(models.Model):
    nome = models.CharField(max_length=200, default=None)
    cpf = models.CharField(max_length=45, default=None, verbose_name="CPF")
    rg = models.CharField(max_length=45,default=None,verbose_name="RG")
    papel = models.CharField(
        max_length=11,
        choices=ESCOLHAS_PAPEL,
        default='Pai',
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
    nome = models.CharField(max_length=200, default=None, unique=True) 
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
    moradia = models.CharField(
        max_length=45,
        choices=ESCOLHAS_MORADIA,
        default='Casa',
    )
    casa_de = models.CharField(
        max_length=45,
        choices=ESCOLHAS_MATERIAL,
        default='Casa',
    )
    condicoes_casa = models.CharField(
        max_length=45,
        choices=ESCOLHAS_CONDICOES,
        default='Casa',
    )
    aluguel = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(0)], blank=True, null=True) 
    data_cadastro = models.DateTimeField(default=timezone.now) 
    realizado_por = models.CharField(max_length=100) 
    observacao = models.TextField() 

    def __str__(self):
        return self.nome
    
class RendaFamiliar(models.Model):
    familia = models.ForeignKey(Familia, verbose_name="Renda da Familia", on_delete=CASCADE)
    origem_renda = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(1)])

    class Meta:
        verbose_name = "Renda da Familia"
        verbose_name_plural = "Rendas das Familias"
