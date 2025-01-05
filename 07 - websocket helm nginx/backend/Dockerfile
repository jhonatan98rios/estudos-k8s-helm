# Use a imagem oficial do Python como base
FROM python:3.9-slim

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie o arquivo requirements.txt para dentro do container
COPY requirements.txt /app/

# Instale as dependências necessárias
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o código da aplicação para o diretório de trabalho
COPY . /app/

# Exponha a porta em que o Flask estará ouvindo
EXPOSE 3000

# Comando para rodar a aplicação com Gunicorn e Gevent
CMD ["gunicorn", "-b", "0.0.0.0:3000", "app:app", "--worker-class", "gevent"]