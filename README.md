# Teste Técnico Backend Python

## Descrição

Este repositório contém o **Teste Técnico Backend Python**, desenvolvido com o objetivo de avaliar as habilidades em Python, FastAPI, criação de CRUDs, consumo de APIs externas, utilização de bancos de dados com ORM e aplicação de técnicas de prompt engineering com Large Language Models (LLMs).

## Objetivo

Desenvolver uma aplicação backend utilizando **FastAPI** que permita a gestão de usuários e imóveis. A aplicação deve incluir:

1. **CRUD de Usuários**: Permitir operações de criação, leitura, atualização e exclusão de usuários.
2. **CRUD de Imóveis**: Permitir operações de criação, leitura, atualização e exclusão de imóveis.
3. **Geração Automática de Descrição de Imóveis**: Ao registrar ou atualizar um imóvel, a descrição deve ser gerada automaticamente por um LLM com base nas informações fornecidas.
4. **Geocodificação de Endereço**: Consumir a API do Nominatim para obter as coordenadas (latitude e longitude) com base no endereço do imóvel. Se não for possível encontrar as coordenadas, armazenar zero para latitude e longitude.

## Tecnologias e Requisitos Obrigatórios

- **Python**
- **FastAPI**
- **ORM SQLAlchemy** (recomendado: SQLite ou PostgreSQL)
- **Biblioteca LLM Ollama** (modelo recomendado: `llama3.2:1b`)
- **Código Limpo e SOLID**
- **CRUD no Padrão REST**
- **Entrega via Dockerfile**

## Requisitos Opcionais (Diferenciais)

- **Autenticação de Usuário via JWT**
- **Criptografia de Senha**
- **Utilização da Biblioteca LangChain-Ollama em Conjunto**
- **Testes Unitários**
- **Arquitetura Limpa ou Domain-Driven Design**
- **Cache para Recuperação de Todos os Imóveis**

## Como Participar  

1. Faça o clone deste repositório para sua máquina local.  
2. Complete o teste técnico conforme as instruções fornecidas.  
3. Envie a URL do repositório para o e-mail **contato@evig.com.br**, utilizando o assunto: **"Teste Técnico Python - [Seu Nome]"**.

## Instruções sobre a Entrega  

1. **API Desenvolvida**:  
   - Não é necessário que você crie arquivos como `docker-compose` ou configure a conteinerização do banco de dados ou da LLM Ollama.  
   - Utilize o `Dockerfile` fornecido para garantir que o código da API possa ser executado corretamente no ambiente disponibilizado.  

2. **Configuração**:  
   - Preencha o arquivo `env.example` com:  
     - `LLM_MODEL` e `LLM_URL` (modelo e URL do LLM utilizado).  
     - `DATABASE_URL` (URL do banco de dados que você utilizou).  
   - Por padrão, considere `localhost`, mas é fundamental que você informe esses valores para identificarmos o modelo de LLM e o banco de dados escolhidos.  

3. **Arquivos Base Disponibilizados**:  
   Para ajudá-lo no desenvolvimento, fornecemos os seguintes arquivos:  
   - `Dockerfile`  
   - `requirements.txt`  
   - `env.example`  
   - `setting.py`  

> **Importante**: O foco é avaliar seu desenvolvimento backend em Python. Não se preocupe em criar contêineres para o banco ou a LLM Ollama; concentre-se apenas em implementar as funcionalidades solicitadas.  

## Referências e Documentação

- **Ollama Docs**: [https://github.com/ollama/ollama](https://github.com/ollama/ollama)
- **Nominatim Docs**: [https://nominatim.org/release-docs/latest/](https://nominatim.org/release-docs/latest/)
- **FastAPI**: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
- **SQLAlchemy**: [https://www.sqlalchemy.org/](https://www.sqlalchemy.org/)
- **Docker**: [https://docs.docker.com/](https://docs.docker.com/)

---

**Boa sorte e bom desenvolvimento!**
