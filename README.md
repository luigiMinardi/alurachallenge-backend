<div align="center">
   <a href="https://github.com/alura-challenges/challenge-back-end">
    <img  src=".github/challenges-logo.svg" alt="Alura Challenges" width="160px">
  </a>
</div>
<p align="center">
  <a href="#english">In English:</a><br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="#installing">Installing</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#using-the-api">Using</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#running-tests">Testing</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#routes">Routes</a>—↴—————↴
  <br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="#português">Em Português:</a>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="#routes-to-videos">Videos</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#routes-to-categorias">Categorias</a>
  <br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="#instalando">Instalando</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#usando-a-api">Usando</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#rodando-os-testes">Testes</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#rotas">Rotas</a>—↴—————↴
  <br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;
  <a href="#rotas-dos-videos">Videos</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#rotas-das-categorias">Categorias</a>
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
    <img alt="GitHub license" src="https://img.shields.io/badge/license-MIT-%2300C86F">
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
  .venv\Scripts\activate.bat
  ```

* Install all the requirements:

  ```bash
  pip install -r requirements.txt
  ```

* Make the Migrations:

  ```bash
  python manage.py makemigrations
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

# Using the API

## Running Tests

For run our automated tests do:

```bash
python manage.py test
```

## Routes

### Routes to Videos

#### /videos/ Query Params

#### Search

You can search videos using the query param `search`.

##### Example 1:

> *Searching something that some of the videos in the database has in the title.*

Searching "Max" doing `/videos/?search=Max`

##### Return:

> *Returns all of the videos that match in the search.*
```json
[
  {
    "id": 2,
    "titulo": "You already know my max length",
    "descricao": "You already know my max length",
    "url": "http://must-be-a-valid-url-with-max-length-of-200.com",
    "categoriaId": 1
  },
  {
    "id": 3,
    "titulo": "Max length is 30",
    "descricao": "Max length is 300",
    "url": "http://must-be-a-valid-url-with-max-length-of-200.page",
    "categoriaId": 2
  }
]
```

##### Example 2:

> *Searching something that none of the videos in the database has in the title.*

Searching "any" doing `/videos/?search=any`

##### Return:

> *Returns an empty list of videos because we didn't have any video that match in the database.*
```json
[]
```

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
  "url": "http://must-be-a-valid-url-with-max-length-of-200.page",
  "categoriaId": 1
}
```

#### PUT /videos/:id/
###### The response code must be `200`.

Change all values in specified video in the database.

##### Request Body:

> *Changing the video we've **POST** earlier, at url `/videos/1/`*
```json
{
  "titulo": "You already know my max length",
  "descricao": "You already know my max length",
  "url": "http://must-be-a-valid-url-with-max-length-of-200.com",
  "categoriaId": 2
}
```

##### Response Body:

```json
{
  "id": 1,
  "titulo": "You already know my max length",
  "descricao": "You already know my max length",
  "url": "http://must-be-a-valid-url-with-max-length-of-200.com",
  "categoriaId": 2
}
```

#### PATCH /videos/:id/
###### The response code must be `200`.

Change some value in specified video in the database.

##### Request Body:

> *Changing the video with id 1 at `/videos/1/`*
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
  "url": "http://you-know-my-max-length-and-im-valid.com",
  "categoriaId": 2
}
```

#### DELETE /videos/:id/
###### The response code must be `200`.

Delete the specified video in the database.

##### Request:
> *Delete the video we've **POST** earlier, at `/videos/1/`*
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
    "url": "http://must-be-a-valid-url-with-max-length-of-200.com",
    "categoriaId": 1
  },
  {
    "id": 3,
    "titulo": "Max length is 30",
    "descricao": "Max length is 300",
    "url": "http://must-be-a-valid-url-with-max-length-of-200.page",
    "categoriaId": 2
  }
]
```

#### GET /videos/:id
###### The response code must be `200`.

Getting one specified video in the database.

##### Request:

> *Getting the video with id 2 at `/videos/2/`*

##### Response Body:

```json
{
  "id": 2,
  "titulo": "You already know my max length",
  "descricao": "You already know my max length",
  "url": "http://must-be-a-valid-url-with-max-length-of-200.com",
  "categoriaId": 1
}
```

### Routes to Categorias

#### GET /categorias/:id/videos/
###### The response code must be `200`.

Getting all videos inside some "categoria".

##### Response:

```json
[
  {
    "id": 2,
    "titulo": "You already know my max length",
    "descricao": "You already know my max length",
    "url": "http://must-be-a-valid-url-with-max-length-of-200.com",
    "categoriaId": 1
  }
]
```

#### /categorias/:id/videos/ Query Params:

##### Search

Search videos inside some "categoria"

##### Request:
> Works at the same way as the [Videos Search Query Param](#videos-query-params)

`/categorias/2/videos/?search=30`

#### Response:

```json
[
  {
    "id": 3,
    "titulo": "Max length is 30",
    "descricao": "Max length is 300",
    "url": "http://must-be-a-valid-url-with-max-length-of-200.page",
    "categoriaId": 2
  },
  {
    "id": 7,
    "titulo": "30 days to do an API",
    "descricao": "Yes, in this video you will learn how you can do this or that...",
    "url": "https://blank.page",
    "categoriaId": 2
  }
]
```

#### POST /categorias/
###### The response code must be `201`.

Add a new "categoria" in the database.

##### Request Body:

```json
{
  "titulo": "Max length is 30",
  "cor": "#AFaf09"
}
```

##### Response Body:

```json
{
  "id": 2,
  "titulo": "Max length is 30",
  "cor": "#AFaf09"
}
```

#### PUT /categorias/:id/
###### The response code must be `200`.

Change all values in specified "categoria" in the database.

##### Request Body:

> *Changing the "categoria" we've **POST** earlier, at url `/categorias/2/`*
```json
{
  "titulo": "You already know my max length",
  "cor": "#AFaf09"
}
```

##### Response Body:

```json
{
  "id": 2,
  "titulo": "You already know my max length",
  "cor": "#AFaf09"
}
```

#### PATCH /categorias/:id/
###### The response code must be `200`.

Change some value in specified "categoria" in the database.

##### Request Body:

> *Changing the "categoria" with id 2 at `/categorias/2/`*
```json
{
  "cor": "#0ff"
}
```

##### Response Body:

```json
{
  "id": 2,
  "titulo": "You already know my max length",
  "cor": "#0ff"
}
```

#### DELETE /categorias/:id/
###### The response code must be `200`.

Delete the specified "categoria" in the database.

##### Request:
> *Delete the "categoria" we've **POST** earlier, at `/categorias/2/`*
##### Response Body:

```json
{
  "detail": "Categoria deletada com sucesso!"
}
```

#### DELETE /categorias/1/
###### The response code must be `405`.

Delete the first "categoria" in the database.

##### Request:
> *Delete the first "categoria", at `/categorias/1/`*
##### Response Body:

```json
{
  "detail": "Você não pode deletar a categoria 1."
}
```

#### GET /categorias/
###### The response code must be `200`.

Getting all the "categoria"'s of the database.

##### Response Body:

```json
[
  {
    "id": 1,
    "titulo": "LIVRE",
    "cor": "#000"
  },
  {
    "id": 3,
    "titulo": "Max length is 30",
    "cor": "#AFaf09"
  },
  {
    "id": 4,
    "titulo": "You already know my max length",
    "cor": "#0ff"
  }
]
```

#### GET /categorias/:id
###### The response code must be `200`.

Getting one specified "categoria" in the database.

##### Request:

> *Getting the "categoria" with id 3 at `/categorias/3/`*

##### Response Body:

```json
{
  "id": 3,
  "titulo": "Max length is 30",
  "cor": "#AFaf09"
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
  .venv\Scripts\activate.bat
  ```

* Instale todos os requerimentos:

  ```bash
  pip install -r requirements.txt
  ```

* Crie as migrações no banco de dados:

  ```bash
  python manage.py makemigrations
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

# Usando a API

## Rodando os testes

Para rodar nossos testes automatizados basta rodar esse comando:

```bash
python manage.py test
```

## Rotas

### Rotas dos Videos

#### /videos/ Parâmetros de Consulta (Query Params)

#### Search

Você pode pesquisar videos usando o parâmetro `search`.

##### Example 1:

> *Pesquisar algo que algum dos videos no banco de dados tem no título.*

Pesquisando "máximo", fazendo `/videos/?search=máximo`

##### Return:

> *Retorna todos os videos que conferem com a pesquisa.*
```json
[
  {
    "id": 2,
    "titulo": "Vc já sabe meu tamanho máximo.",
    "descricao": "Vc já sabe meu tamanho máximo.",
    "url": "http://deve-ser-um-url-valido-com-comprimento-maximo-de-200.com",
    "categoriaId": 1
  },
  {
    "id": 3,
    "titulo": "Comprimento máximo é 30",
    "descricao": "Comprimento máximo é 300",
    "url": "http://deve-ser-um-url-valido-com-comprimento-maximo-de-200.page",
    "categoriaId": 2
  }
]
```

##### Example 2:

> *Pesquisando algo que nenhum dos videos no banco de dados tem no título.*

Pesquisando "qualquer", fazendo `/videos/?search=qualquer`

##### Return:

> *Retorna uma lista vazia de videos porque não tinha nada que inferisse a pesquisa.*
```json
[]
```

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
  "url": "http://deve-ser-um-url-valido-com-comprimento-maximo-de-200.page",
  "categoriaId": 1
}
```

#### PUT /videos/:id/
###### O código de resposta deve ser `200`.

Mudando todos os valores em um video específico no banco de dados.

##### Request Body:

> *Trocando os valores do video que demos **POST** mais cedo, usando a url `/videos/1/`*
```json
{
  "titulo": "Vc já sabe meu tamanho máximo.",
  "descricao": "Vc já sabe meu tamanho máximo.",
  "url": "http://deve-ser-um-url-valido-com-comprimento-maximo-de-200.com",
  "categoriaId": 2
}
```

##### Response Body:

```json
{
  "id": 1,
  "titulo": "Vc já sabe meu tamanho máximo.",
  "descricao": "Vc já sabe meu tamanho máximo.",
  "url": "http://deve-ser-um-url-valido-com-comprimento-maximo-de-200.com",
  "categoriaId": 2
}
```

#### PATCH /videos/:id/
###### O código de resposta deve ser `200`.

Mudando um valor em um video específico no banco de dados.

##### Request Body:

> *Mudando o video com o id 1 em `/videos/1/`*
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
  "url": "http://voce-sabe-meu-tamanho-maximo-e-eu-sou-um-url-valido.com",
  "categoriaId": 2
}
```

#### DELETE /videos/:id/
###### O código de resposta deve ser `200`.

Deletando um video específico no banco de dados.

##### Request:
> *Deletando o video que demos **POST** anteriormente, usando `/videos/1/`*
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
    "url": "http://deve-ser-um-url-valido-com-comprimento-maximo-de-200.com",
    "categoriaId": 1
  },
  {
    "id": 3,
    "titulo": "Comprimento máximo é 30",
    "descricao": "Comprimento máximo é 300",
    "url": "http://deve-ser-um-url-valido-com-comprimento-maximo-de-200.page",
    "categoriaId": 2
  }
]
```

#### GET /videos/:id
###### O código de resposta deve ser `200`.

Pegando um video específico no banco de dados.

##### Request:

> *Pegando o video em `/videos/2/`*

##### Response Body:

```json
{
  "id": 2,
  "titulo": "Vc já sabe meu tamanho máximo.",
  "descricao": "Vc já sabe meu tamanho máximo.",
  "url": "http://deve-ser-um-url-valido-com-comprimento-maximo-de-200.com",
  "categoriaId": 1
}
```

### Rotas das Categorias

#### GET /categorias/:id/videos/
###### O código de resposta deve ser `200`.

Pegando todos os videos de dentro de uma categoria.

##### Response:

```json
[
  {
    "id": 2,
    "titulo": "Vc já sabe meu tamanho máximo.",
    "descricao": "Vc já sabe meu tamanho máximo.",
    "url": "http://deve-ser-um-url-valido-com-comprimento-maximo-de-200.com",
    "categoriaId": 1
  }
]
```

#### /categorias/:id/videos/ Parâmetros de Consulta (Query Params)

##### Search

Pesquisando videos dentro de uma categoria

##### Request:
> O search funciona da mesma maneira que o [Query Param de Search dos Videos](#videos-parâmetros-de-consulta-query-params)

`/categorias/2/videos/?search=30`

#### Response:

```json
[
  {
    "id": 3,
    "titulo": "Comprimento máximo é 30",
    "descricao": "Comprimento máximo é 300",
    "url": "http://deve-ser-um-url-valido-com-comprimento-maximo-de-200.page",
    "categoriaId": 2
  },
  {
    "id": 7,
    "titulo": "30 dias pra fazer uma API",
    "descricao": "Sim, nesse video você vai aprender como você pode fazer isso ou aquilo...",
    "url": "https://blank.page",
    "categoriaId": 2
  }
]
```

#### POST /categorias/
###### O código de resposta deve ser `201`.

Adicionando uma nova categoria no banco de dados.

##### Request Body:

```json
{
  "titulo": "Comprimento máximo é 30",
  "cor": "#AFaf09"
}
```

##### Response Body:

```json
{
  "id": 2,
  "titulo": "Comprimento máximo é 30",
  "cor": "#AFaf09"
}
```

#### PUT /categorias/:id/
###### O código de resposta deve ser `200`.

Mudando todos os valores em uma categoria específica no banco de dados.

##### Request Body:

> *Trocando os valores da categoria que demos **POST** mais cedo, usando a url `/categorias/2/`*

```json
{
  "titulo": "Vc já sabe meu tamanho máximo.",
  "cor": "#AFaf09"
}
```

##### Response Body:

```json
{
  "id": 2,
  "titulo": "Vc já sabe meu tamanho máximo.",
  "cor": "#AFaf09"
}
```

#### PATCH /categorias/:id/
###### O código de resposta deve ser `200`.

Mudando um valor em uma categoria específica no banco de dados.

##### Request Body:

> *Mudando a categoria com o id 2 em `/categorias/2/`*

```json
{
  "cor": "#0ff"
}
```

##### Response Body:

```json
{
  "id": 2,
  "titulo": "Vc já sabe meu tamanho máximo.",
  "cor": "#0ff"
}
```

#### DELETE /categorias/:id/
###### O código de resposta deve ser `200`.

Deletando uma categoria específica no banco de dados.

##### Request:

> *Deletando a categoria que demos **POST** anteriormente, usando `/categorias/2/`*

##### Response Body:

```json
{
  "detail": "Categoria deletada com sucesso!"
}
```

#### DELETE /categorias/1/
###### O código de resposta deve ser `405`.

Deletando a primeira categoria do banco de dados.

##### Request:

> *Deletando a primeira categoria, usando `/categorias/1/`*

##### Response Body:

```json
{
  "detail": "Você não pode deletar a categoria 1."
}
```

#### GET /categorias/
###### O código de resposta deve ser `200`.

Pegando todas as categorias do banco de dados.

##### Response Body:

```json
[
  {
    "id": 1,
    "titulo": "LIVRE",
    "cor": "#000"
  },
  {
    "id": 3,
    "titulo": "Comprimento máximo é 30",
    "cor": "#AFaf09"
  },
  {
    "id": 4,
    "titulo": "Vc já sabe meu tamanho máximo.",
    "cor": "#0ff"
  }
]
```

#### GET /categorias/:id
###### O código de resposta deve ser `200`.

Pegando uma categoria específica no banco de dados.

##### Request:

> *Pegando a categoria em `/categorias/3/`*

##### Response Body:

```json
{
  "id": 3,
  "titulo": "Comprimento máximo é 30",
  "cor": "#AFaf09"
}
```
