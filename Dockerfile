# Use uma imagem base do Python
FROM python:3.9

# Instale as dependências do sistema
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Instale o Ollama
RUN curl -sSL https://ollama.com/install.sh | bash

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos de requisitos e instale as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação
COPY ./app /app

# Copie o arquivo .env
COPY .env .env

# Exponha a porta 8080
EXPOSE 8080

# Comando para iniciar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]