from src.static.models.reserva import ReservaCreate, ReservaResponse
from src.errors.http_not_found import ReservaNotFoundException
from src.errors.http_bad_request import HttpBadRequest
from datetime import datetime
from bson import ObjectId
import logging

class ReservaCrud:
    def __init__(self, db):
        self.reserva_collection = db["reservas"]

    # Função para criar uma reserva
    async def criar_reserva(self, reserva: ReservaCreate) -> ReservaResponse:
        # Verifica se a data de início da reserva já passou
        if reserva.data_inicio < datetime.now():
            raise HttpBadRequest("A data de início da reserva já passou e não pode ser criada.")
        
        reserva_dict = reserva.model_dump()
        reserva_dict['data_criacao'] = datetime.now()
        
        result = await self.reserva_collection.insert_one(reserva_dict)

        reserva_id = str(result.inserted_id)

        return ReservaResponse(
            id=str(reserva_id),
            bloco=reserva.bloco,
            numero_sala=reserva.numero_sala,
            data_inicio=reserva.data_inicio,
            data_fim=reserva.data_fim,
            nome_coordenador=reserva.nome_coordenador,
            motivo=reserva.motivo,
            frequencia=reserva.frequencia,
            dia_da_semana=reserva.dia_da_semana,
            numero_de_ocorrencias=reserva.numero_de_ocorrencias,
            data_criacao=reserva_dict['data_criacao']
        )

    # Função para cancelar uma reserva
    async def cancelar_reserva(self, reserva_id: str) -> str:
        reserva = await self.reserva_collection.find_one({"_id": ObjectId(reserva_id)})

        if not reserva:
            raise ReservaNotFoundException(reserva_id)

        await self.reserva_collection.delete_one({"_id": ObjectId(reserva_id)})
        return f"Reserva com ID {reserva_id} cancelada com sucesso!"

    # Função para verificar a disponibilidade de uma sala
    async def verificar_disponibilidade(self, bloco: str, numero_sala: int, data_inicio: datetime, data_fim: datetime) -> bool:
        reservas_existentes = await self.reserva_collection.find({
            "bloco": bloco,
            "numero_sala": numero_sala,
            "data_inicio": {"$lt": data_fim},
            "data_fim": {"$gt": data_inicio}
        }).to_list(length=100)  # Limita o número de reservas retornadas (pode ajustar conforme necessário)

        # Se houver alguma reserva, significa que a sala não está disponível
        return len(reservas_existentes) == 0
    
    # Função para simular notificação
    async def enviar_notificacao(reserva: ReservaCreate):
        logging.info(f"NOTIFICAÇÃO: A reserva para a {reserva.numero_sala} do bloco {reserva.bloco} foi feita para a data {reserva.data_inicio}. Coordenador: {reserva.nome_coordenador}.")

    # Função para encontrar reservas futuras
    async def find_reservas_futuras(self, current_time: datetime):
        # Consulta no banco de dados para encontrar as reservas futuras
        reservas_futuras = await self.reserva_collection.find({"data_inicio": {"$gt": current_time}}).to_list(length=None)
        return reservas_futuras