from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone

# Create your models here.

class CustomUserManager(UserManager):
    def _create_user(self, email, password,**extra_fields):
        if not email:
            raise ValueError("Voce não forneceu um email válido")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self,  email=None, password=None,**extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email,password, **extra_fields)
    
    def create_superuser(self,  email=None, password=None,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email,password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=True, default='', unique=True)
    celular = models.CharField(max_length=45, unique=True)
    rua = models.CharField(max_length=200)
    numero = models.CharField(max_length=30)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    unidade_federativa = models.CharField(max_length=2)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    data_de_ingresso = models.DateTimeField(default = timezone.now)


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["nome", "celular", "rua", "numero", "bairro", "cidade",
                        "unidade_federativa"]

    class Meta:
        verbose_name = "Colaborador"
        verbose_name_plural = "Colaboradores"

    def get_full_name(self):
        return self.nome
    
    def get_short_name(self):
        if ' ' in self.nome:
            first_name, last_name = self.nome.split(' ', 1)
        else:
            first_name = self.nome 
        return first_name
    