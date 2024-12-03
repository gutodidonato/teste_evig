# Etapa de build
FROM python:3.13-alpine AS build

# Instala as dependências do sistema
RUN apk add --no-cache gcc musl-dev libffi-dev

# Define o diretório de trabalho
WORKDIR /app

# Copia o arquivo de dependências
COPY requirements.txt .

# Instala as dependências no diretório de build
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Etapa final
FROM python:3.13-alpine

# Copia as dependências instaladas da etapa de build
COPY --from=build /install /usr/local

# Define o diretório de trabalho
WORKDIR /app

# Copia todos os arquivos do projeto para o container
COPY . /app

# Expõe a porta 8000
EXPOSE 8000

# Define o comando padrão para rodar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
