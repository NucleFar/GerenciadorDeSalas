# Usar a imagem oficial do Python como base
FROM python:3.12-slim

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar o arquivo de dependências para o contêiner
COPY requirements.txt /app/

# Instalar as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação para dentro do contêiner
COPY . /app/

# Expor a porta que o uvicorn vai rodar
EXPOSE 8000

# Comando para rodar a aplicação FastAPI com o Uvicorn
CMD ["uvicorn", "src.main.server.server:app", "--host", "0.0.0.0", "--port", "8000"]
