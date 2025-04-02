import motor.motor_asyncio
from pymongo.database import Database
from typing import Any
from src.config.config import AppConfig  # Importando a configuração

# Criar a instância do cliente MongoDB (assíncrono) usando o AppConfig
client = motor.motor_asyncio.AsyncIOMotorClient(AppConfig.MONGO_URL)

# Obter o banco de dados
db = client[AppConfig.MONGO_DB_NAME]

# Função para obter a coleção do MongoDB
def get_collection(collection_name: str) -> Any:
    return db[collection_name]

# Função de dependência para fornecer o banco de dados nas rotas
def get_db() -> Database:
    return db
