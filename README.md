<div align="center">
   <a href="https://github.com/alura-challenges/challenge-back-end">
    <img  src=".github/challenges-logo.svg" alt="Alura Challenges" width="160px">
  </a>
</div>
<p align="center">
  <a href="#english">In English:</a><br>
  <a href="#installing">Installing</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#using-the-api">Using</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#running-tests">Testing</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#routes">Routes</a>
  <br><a href="#português">Em Português:</a><br>
  <a href="#instalando">Instalando</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#usando-a-api">Usando</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#rodando-os-testes">Testes</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#rotas">Rotas</a>

</p>
<div align="center">
  <a href="https://github.com/alura-challenges/challenge-back-end">
    <img alt="Alura Challenge Github" src="https://img.shields.io/badge/Alura-Challenge-%2300C86F">
  </a>
  <a href="https://www.python.org/downloads/">
    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/djangorestframework?color=%2300C86F">
  </a>
  <a href="https://www.django-rest-framework.org/#requirements">
    <img alt="PyPI - Django Version" src="https://img.shields.io/pypi/djversions/djangorestframework?color=%2300C86F">
  </a>
  <a href="https://github.com/luigiMinardi/alurachallenge-backend/blob/main/LICENSE">
    <img alt="GitHub license" src="https://img.shields.io/github/license/luigiMinardi/alurachallenge-backend?color=%2300C86F">
  </a>
  <a href="https://pypi.org/project/djangorestframework/">
    <img alt="PyPI - Status" src="https://img.shields.io/pypi/status/djangorestframework">
  </a>
</div>

# English

## DISCLAIMER
Although the README has the english and the portuguese version I did not translated the api exceptions or the database columns to english so feel free to ask me if you didn't know what something mean.

## Installing

* First things first, clone the repository:

  ```bash
  git clone https://github.com/luigiMinardi/alurachallenge-backend
  ```

* Then create a [Virtual Enviroment](https://outline.com/HaJ3zA) for you:

  ```bash
  python -m venv .venv
  ```
  
* Activate Your `venv`:

  Mac/Linux:
  ```bash
  source .venv/bin/activate 
  ```
  Windows:
  ```cmd
  venv/Scripts/activate.bat
  ```

* Install all the requirements:

  ```bash
  pip install -r requirements.txt
  ```

* Run the DataBase Migration:

  ```bash
  python manage.py migrate
  ```

* Create a Super User:
  ```bash
  python manage.py createsuperuser
  ```

* Run your server:

  ```bash
  python manage.py runserver
  ```

Now you are ready to use it.

## Using the API

### Running Tests

For run our automated tests do:

```bash
python manage.py test
```

### Routes

#### POST /videos/
###### The response code must be `201`.

Add a new video in the database.

##### Request Body:

```json
{
    "titulo": "Max length is 30",
    "descricao": "Max length is 300",
    "url": "http://must-be-a-valid-url-with-max-length-of-200.page"
}
```

##### Response Body:

```json
{
  "id": 1,
  "titulo": "Max length is 30",
  "descricao": "Max length is 300",
  "url": "http://must-be-a-valid-url-with-max-length-of-200.page"
}
```

#### PUT /videos/:id/
###### The response code must be `200`.

Change all values in specified video in the database.

##### Request Body:

*Changing the video we've **POST** earlier, at url `/videos/1/`*
```json
{
    "titulo": "You already know my max length",
    "descricao": "You already know my max length",
    "url": "http://must-be-a-valid-url-with-max-length-of-200.com"
}
```

##### Response Body:

```json
{
  "id": 1,
  "titulo": "You already know my max length",
  "descricao": "You already know my max length",
  "url": "http://must-be-a-valid-url-with-max-length-of-200.com"
}
```

#### PATCH /videos/:id/
###### The response code must be `200`.

Change some value in specified video in the database.

##### Request Body:

*Changing the video with id 1 at `/videos/1/`*
```json
{
	"url": "http://you-know-my-max-length-and-im-valid.com"
}
```

##### Response Body:

```json
{
  "id": 1,
  "titulo": "You already know my max length",
  "descricao": "You already know my max length",
  "url": "http://you-know-my-max-length-and-im-valid.com"
}
```

#### DELETE /videos/:id/
###### The response code must be `200`.

Delete the specified video in the database.

##### Request:
*Delete the video we've **POST** earlier, at `/videos/1/`*
##### Response Body:

```json
{
  "detail": "Vídeo deletado com sucesso!"
}
```

#### GET /videos/
###### The response code must be `200`.

Getting all the videos of the database.

##### Response Body:

```json
[
  {
    "id": 2,
    "titulo": "You already know my max length",
    "descricao": "You already know my max length",
    "url": "http://must-be-a-valid-url-with-max-length-of-200.com"
  },
  {
    "id": 3,
    "titulo": "Max length is 30",
    "descricao": "Max length is 300",
    "url": "http://must-be-a-valid-url-with-max-length-of-200.page"
  }
]
```

#### GET /videos/:id
###### The response code must be `200`.

Getting one specified video in the database.

##### Request:

*Getting the video with id 2 at `/videos/2/`*

##### Response Body:

```json
{
  "id": 2,
  "titulo": "You already know my max length",
  "descricao": "You already know my max length",
  "url": "http://must-be-a-valid-url-with-max-length-of-200.com"
}
```

# Português

## Instalando

* Primeiramente, clone o repositório:

  ```bash
  git clone https://github.com/luigiMinardi/alurachallenge-backend
  ```

* Então crie seu [Ambiente Virtual](https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais):

  ```bash
  python -m venv .venv
  ```
  Mac/Linux:
  ```bash
  source .venv/bin/activate 
  ```
  Windows:
  ```cmd
  venv/Scripts/activate.bat
  ```

* Instale todos os requerimentos:

  ```bash
  pip install -r requirements.txt
  ```

* Rode as migrações do banco de dados:

  ```bash
  python manage.py migrate
  ```

* Crie um Super Usuário:
  ```bash
  python manage.py createsuperuser
  ```

* Rode seu servidor:

  ```bash
  python manage.py runserver
  ```

Prontinho! Agora já pode usar a API.

## Usando a API

### Rodando os testes

Para rodar nossos testes automatizados basta rodar esse comando:

```bash
python manage.py test
```

### Rotas

#### POST /videos/
###### O código de resposta deve ser `201`.

Adicionando um novo video no banco de dados.

##### Request Body:

```json
{
    "titulo": "Comprimento máximo é 30",
    "descricao": "Comprimento máximo é 300",
    "url": "http://deve-ser-um-url-valido-com-comprimento-maximo-de-200.page"
}
```

##### Response Body:

```json
{
  "id": 1,
  "titulo": "Comprimento máximo é 30",
  "descricao": "Comprimento máximo é 300",
  "url": "http://deve-ser-um-url-valido-com-comprimento-maximo-de-200.page"
}
```

#### PUT /videos/:id/
###### O código de resposta deve ser `200`.

Mudando todos os valores em um video específico no banco de dados.

##### Request Body:

*Trocando os valores do video que demos **POST** mais cedo, usando a url `/videos/1/`*
```json
{
    "titulo": "Vc já sabe meu tamanho máximo.",
    "descricao": "Vc já sabe meu tamanho máximo.",
    "url": "http://deve-ser-um-url-valido-com-comprimento-maximo-de-200.com"
}
```

##### Response Body:

```json
{
  "id": 1,
  "titulo": "Vc já sabe meu tamanho máximo.",
  "descricao": "Vc já sabe meu tamanho máximo.",
  "url": "http://deve-ser-um-url-valido-com-comprimento-maximo-de-200.com"
}
```

#### PATCH /videos/:id/
###### O código de resposta deve ser `200`.

Mudando um valor em um video específico no banco de dados.

##### Request Body:

*Mudando o video com o id 1 em `/videos/1/`*
```json
{
	"url": "http://voce-sabe-meu-tamanho-maximo-e-eu-sou-um-url-valido.com"
}
```

##### Response Body:

```json
{
  "id": 1,
  "titulo": "Vc já sabe meu tamanho máximo.",
  "descricao": "Vc já sabe meu tamanho máximo.",
  "url": "http://voce-sabe-meu-tamanho-maximo-e-eu-sou-um-url-valido.com"
}
```

#### DELETE /videos/:id/
###### O código de resposta deve ser `200`.

Deletando um video específico no banco de dados.

##### Request:
*Deletando o video que demos **POST** anteriormente, usando `/videos/1/`*
##### Response Body:

```json
{
  "detail": "Vídeo deletado com sucesso!"
}
```

#### GET /videos/
###### O código de resposta deve ser `200`.

Pegando todos os videos do banco de dados.

##### Response Body:

```json
[
  {
    "id": 2,
    "titulo": "Vc já sabe meu tamanho máximo.",
    "descricao": "Vc já sabe meu tamanho máximo.",
    "url": "http://deve-ser-um-url-valido-com-comprimento-maximo-de-200.com"
  },
  {
    "id": 3,
    "titulo": "Comprimento máximo é 30",
    "descricao": "Comprimento máximo é 300",
    "url": "http://deve-ser-um-url-valido-com-comprimento-maximo-de-200.page"
  }
]
```

#### GET /videos/:id
###### O código de resposta deve ser `200`.

Pegando um video específico no banco de dados.

##### Request:

*Pegando o video em `/videos/2/`*

##### Response Body:

```json
{
  "id": 2,
  "titulo": "Vc já sabe meu tamanho máximo.",
  "descricao": "Vc já sabe meu tamanho máximo.",
  "url": "http://deve-ser-um-url-valido-com-comprimento-maximo-de-200.com"
}
```