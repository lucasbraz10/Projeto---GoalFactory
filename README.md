# GoalFactory

GoalFactory é um sistema desenvolvido em Python para gerenciamento e sorteio de chaveamentos de campeonatos. O projeto utiliza banco de dados MySQL para armazenamento das informações e oferece funcionalidades de CRUD para gerenciamento de equipes, além da geração automática de confrontos para torneios.

##  Funcionalidades

- Cadastro de equipes no banco de dados.
- Consulta de equipes cadastradas.
- Atualização de informações das equipes.
- Exclusão de equipes.
- Sorteio automático de chaveamentos.
- Suporte para campeonatos com:
  - 4 times
  - 6 times
  - 8 times
- Armazenamento persistente utilizando MySQL.
- Integração entre Python e MySQL através da biblioteca `mysql.connector`.

## Tecnologias Utilizadas

- Python 3
- MySQL
- mysql.connector

## Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/GoalFactory.git
```

### 2. Acesse a pasta do projeto

```bash
cd GoalFactory
```

### 3. Instale as dependências

```bash
pip install mysql-connector-python
```

### 4. Configure o banco de dados

Crie um banco de dados MySQL e execute o script SQL do projeto para gerar as tabelas necessárias.

Exemplo:

```sql
CREATE DATABASE goalfactory;
```

Depois execute o arquivo responsável pela criação das tabelas.

### 5. Configure a conexão

No arquivo de conexão com o banco, altere as credenciais:

```python
mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="goalfactory"
)
```

### 6. Execute o projeto

```bash
python main.py
```

## 🎲 Sistema de Chaveamentos

O GoalFactory realiza sorteios automáticos para diferentes quantidades de participantes:

### 4 Times

Formato eliminatório direto:

```text
Time A x Time B
Time C x Time D
```

### 6 Times

Os participantes são divididos em dois grupos de três equipes. Após a fase de grupos, os melhores classificados avançam para as semifinais.

```text
Grupo A
- Time 1
- Time 2
- Time 3

Grupo B
- Time 4
- Time 5
- Time 6
```

### 8 Times

Formato tradicional de mata-mata:

```text
Quartas de Final
↓
Semifinais
↓
Final
```

## Operações CRUD

O sistema permite:

- Create → Inserir equipes.
- Read → Consultar equipes cadastradas.
- Update → Alterar informações das equipes.
- Delete → Remover equipes do banco de dados.

##  Objetivo do Projeto

Este projeto foi desenvolvido para fins acadêmicos, com o objetivo de aplicar conceitos de:

- Lógica de Programação em Python
- Banco de Dados Relacional
- Integração Python + MySQL
- CRUD
- Estruturas de dados
- Organização de torneios esportivos

Projeto desenvolvido como trabalho acadêmico do curso de Análise e Desenvolvimento de Sistemas.
