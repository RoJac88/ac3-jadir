# CRUD APP
**AC-03** - Desenvolvimento de aplicações distribuídas.

### Instalação

Instale as dependências do projeto:
```sh
pip install -r requirements.txt
```

Dentro da pasta do projeto, crie um arquivo "**.env**" com as credenciais do banco de dados e uma variável FLASK_APP com o valor "main.py". Por exemplo:

```txt
FLASK_APP=main.py
DB_HOST=uri.do.banco.com.br
DB_USER=username
DB_NAME=dbname
DB_PASSWORD=senha
```
Execute o arquivo db_ext.py para criar as tabelas no banco de dados:
```sh
python db_ext.py
```

Inicie a aplicação com o comando:
```sh
flask run
```
### Obs:

A rota principal mostra todas as tabelas do banco de dados. Visite a rota /alunos/ para editar a tabela do grupo.
