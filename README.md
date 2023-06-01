# projetoGAFF
Projeto desenvolvido para a matéria de extensão II

Passo 1: 

Clone o repositório para uma pasta local: git clone https://github.com/MnFCosta/projetoGAFF.git 

Passo 2: 

Crie uma venv: Comando Windows =  py -m venv venv, Comando Linux/Mac = python3 -m venv venv

Passo 3: 

Ative sua venv (para aplicações Django sempre utilize uma venv):  Comando para ativar a venv windows = venv\Scripts\activate, Comando para ativar a venv linux/mac = source venv/bin/activate

OBS: Para sistemas Windows, é bem provável que a execução de scripts esteja desativada, para ativar execute o Windows Powershell como administrador, execute o comando Set-ExecutionPolicy Unrestricted, selecione a opção "Sim para todos" reinicie sua IDE, e tente ativar a venv novamente.

Passo 4: 

Baixe todas as dependencias necessárias usando o pip: pip install -r requirements.txt

Passo 5:

Crie um banco de dados MySQL utilizando o MySQL Workbench.

Dentro do arquivo "settings.py" encontrado no diretório projetoGAFF, coloque os valores corretos da sua database.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': ' ', #adicione aqui o nome do banco de dados do mySQL
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root', #adicione aqui o nome do usuário do mySQL (por padrão é root)
        'PASSWORD': '', #adicione aqui a senha do mySQL (caso não tenha apenas deixe em branco)
    }
}

Passo 6:

Crie as migrações de banco necessárias com o comando: py (python3 para linux/mac) manage.py makemigrations

Caso o comando makemigrations retorne "no changes detected" mande as migrações para o banco com o comando: py (python3 para linux/mac) manage.py migrate  

Passo 7 (Este passo será feito todas vez que o sistema precise ser iniciado novamente):

Caso as migrações enviadas retornem OK, o sistema está configurado e já pode ser utilizado,  utilize o comando py (python3 para linux/mac) manage.py runserver para iniciar um servidor local

 Acesse a  URL: http://127.0.0.1:8000/ para utilizar o sistema, caso tenha uma conta cadastrada, faça o login, caso não cadastre-se na opção "Não possui uma conta? Cadastre-se aqui!"



