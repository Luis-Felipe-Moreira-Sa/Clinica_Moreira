## Projeto de Clinica

# Este Projeto Consiste:
- Cadastrar especialidades
Deve ser possível cadastrar as especialidades médicas (ex: CARDIOLOGIA, PEDIATRIA) que a clínica atende.
- Cadastrar médicos
Deve ser possível cadastrar os médicos que podem atender na clínica fornecendo as seguintes informações:
● Nome: Nome do médico (obrigatório)
● CRM: Número do médico no conselho regional de medicina (obrigatório)
● E-mail: Endereço de e-mail do médico
● Telefone: Telefone do médico
● Especialidade: Especialidade na qual o médico atende
- Criar agenda para médico
Deve ser possível criar uma agenda para um médico em um dia  específico fornecendo
as seguintes informações:
● Médico: Médico que será alocado (obrigatório)
● Dia: Data de alocação do médico (obrigatório)
● Horários: Lista de horários na qual o médico deverá ser alocado para o dia
especificado (obrigatório)
- Crie uma página para os clientes realizarem um cadastro
Deve ser possível o cliente realizar o seu cadastro no sistema  ornecendo as seguintes informações:
● Nome: Nome do médico (obrigatório)
● CPF: Número do médico no conselho regional de medicina (obrigatório)
● E-mail: Endereço de e-mail do médico
● Sexo: Sexo do cliente (masculino ou feminino)
● Telefone: Telefone do médico
- Crie uma página para o cliente marque as consultas
Dado que o cliente já esteja logado no sistema ele poderá marcar uma consulta com um determinado médico para uma determinada data. O cliente pode realizar o login e logout do sistema.

## Configurando o ambiente para executar a aplicação web.
Faça o download deste repositorio:

```
$ git clone git@github.com:Luis-Felipe-Moreira-Sa/Clinica_Moreira.git
```

Crie um maquina virtual e instale a bibliotecas disponiveis no 
arquivo requirementes.txt:

Entre na pasta criada e inicie um ambiente virtual:
```
$ cd Clinica_Moreira
$ virtualenv env
```
Depois voce deve ativa-lo com o seguinte comando:

```
$ . /env/bin/activate
```
Apos ativado, instale as bibliotecas necessárias para executar o projeto:
```
 (env)$ pip install -r requirements.txt
```
Para poder ter o primeiro acesso e pode configurar o aplicação vamos executar o comando  'migrate' para gerar o banco de dados padrão do Django(SQLite).

```
(env)$ python3 manage.py migrate
```
E para ter acesso ao administrador do Django criaremos o superusuario:
```
(env)$ python3 manage.py createsuperuser
Usuário: admin
E-mail: admin@mail.com
Password: 
Password (again):
```
Para iniciar o servidor depois deste passo você deve:
```
(env)$ python3 manage.py runserver
```


Para visualizar se tudo esta executando como esperado vamos acessar o seguinte endereço pelo seu navegador de internet:
[http://localhost:8000/]

Ou você pode ter acesso a admin do Django:
[http://localhost:8000/admin]

# Clinica_Moreira
# Clinica_Moreira
# Clinica_Moreira
