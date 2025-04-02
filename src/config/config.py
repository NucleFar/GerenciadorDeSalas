from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env
load_dotenv()

class AppConfig:
    # Aqui você coloca a URL do MongoDB
    MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "GerenciadorUni")
    SECRET_KEY = os.getenv("SECRET_KEY")
