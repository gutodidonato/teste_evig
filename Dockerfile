# Use a imagem base do Python
FROM python:3.13.0

# Instale as dependências do sistema
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Configure o diretório de trabalho
WORKDIR /app

# Copie os requisitos
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante da aplicação
COPY ./app /app

# Copie o arquivo .env
COPY .env .env

# Exponha a porta 8080
EXPOSE 8080

# Comando para iniciar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
