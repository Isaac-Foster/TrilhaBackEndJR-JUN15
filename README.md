
# Projeto de API de Tarefas com FastAPI

Este projeto é uma API para gerenciamento de tarefas que permite criar, ler, atualizar e deletar tarefas, além de implementar autenticação de usuários. A API é construída usando Python e FastAPI, com o gerenciador de pacotes Poetry.

## Objetivos
- Criar uma API que permita CRUD (Create, Read, Update, Delete) de tarefas.
- Implementar autenticação de usuários.
- Utilizar um banco de dados SQLite para armazenar as tarefas.
- Documentar todo o processo e apresentar as conclusões.

## Requisitos Funcionais
- **Criar Tarefa**: Endpoint para criar uma nova tarefa.
- **Listar Tarefas**: Endpoint para listar todas as tarefas.
- **Atualizar Tarefa**: Endpoint para atualizar uma tarefa existente.
- **Deletar Tarefa**: Endpoint para deletar uma tarefa existente.

## Autenticação de Usuários
- **Registro de Usuário**: Endpoint para registrar um novo usuário.
- **Login de Usuário**: Endpoint para autenticar um usuário e gerar um token JWT.
- **Proteção de Rotas**: Garantir que apenas usuários autenticados possam acessar os endpoints de tarefas.

## Banco de Dados
- Utilizar SQLite como banco de dados para armazenar informações de usuários e tarefas.

## Tecnologias Utilizadas
- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Poetry](https://python-poetry.org/)
- [SQLite](https://www.sqlite.org/)

## Instalação

1. Clone o repositório:
   \`\`\`bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   \`\`\`

2. Instale as dependências:
   \`\`\`bash
   poetry install
   \`\`\`

3. Crie o banco de dados SQLite:
   \`\`\`bash
   poetry run python create_db.py
   \`\`\`

4. Execute a aplicação:
   \`\`\`bash
   poetry run uvicorn app.main:app --reload
   \`\`\`

## Endpoints

### Tarefas
- **Criar Tarefa**
  - \`POST /task\`
- **Listar Tarefas**
  - \`GET /task\`
- **Atualizar Tarefa**
  - \`PUT /task/{id}\`
- **Deletar Tarefa**
  - \`DELETE /task/{id}\`

### Autenticação
- **Registro de Usuário**
  - \`POST /api/user/signup\`
- **Login de Usuário**
  - \`POST /api/user/signin\`

## Licença
Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
