# EnergiaAPI
A EnergiaAPI é uma API RESTful que permite o registro de novos parceiros e  criação de dados sobre usinas de energia.

## Repositorio Frontend
- [Gerenciamento de Usinas](https://github.com/fjrjdev/Gerenciamento-de-Usinas)

## Rotas
A EnergiaAPI possui as seguintes rotas:

- (POST) - "/login/": gera um token JWT para autenticação de um usuário.
- (POST) - "/refresh": atualiza um token JWT expirado ou extende sua duração.

- (GET-POST) - "/partners/": permite criar um novo parceiro ou listar todos os parceiros cadastrados.
- (GET-PATCH-DELETE) - "/partners/:id/": permite obter, atualizar ou excluir informações sobre um parceiro específico, de acordo com o ID informado na URL.
- (GET) - "/partners/last-partners/": retorna os parceiros adicionados mais recentemente.

- (GET) - "/plants/": retorna uma lista de todas as usinas cadastradas.
- (GET-PATCH-DELETE) - "/plants/:id/": retorna as informações da usina correspondente ao ID informado na URL.
- (GET) - "/plants/top-capacity/": retorna as usinas com maior capacidade de geração de energia.

Mais informações sobre as rotas estão descritas na [Docs](http://localhost:8000/docs/) que pode ser accessada durante a execução da api.

## Tecnologias utilizadas
A API foi construída utilizando as seguintes tecnologias:

- Django: framework web em Python.
- Django Rest Framework: biblioteca para construção de APIs em Django.
- Django Rest Framework Simple JWT: biblioteca para autenticação com tokens JWT em Django.
- Banco de dados Postgresql: Banco de dados relacional.

## Instalando com o docker
- Clone o repositório para a sua máquina
- Defina suas variaveis de ambiente

```
    POSTGRES_DB='nomeBancoDeDados'
    POSTGRES_USER='seuUsuario'
    POSTGRES_PASSWORD='suaSenha'
    SECRET_KEY='suaSenhaSecreta'
    DB_HOST="db"
```
Caso queira rodar localmente é necessário definir DB_HOST="localhost" 

-  Builde o container da api:
```
docker compose up --build
```
- Acesse a documentação, 

```
http://localhost:8000/docs/
```

## Documentação

[Docs](http://localhost:8000/docs/)
