from fastapi import APIRouter, Depends, HTTPException
from src.static.models.reserva import ReservaCreate
from src.main.factories.reserva_factory import reserva_factory
from src.errors.http_not_found import ReservaNotFoundException
from src.static.models.reserva import DisponibilidadeRequest
from datetime import datetime
from src.crud.reserva_crud import ReservaCrud

router = APIRouter(tags=["reservas"])

# Rota para criar uma reserva
@router.post("/reservar/")
async def reservar_sala(reserva: ReservaCreate, reserva_crud=Depends(reserva_factory)):
    return await reserva_crud.criar_reserva(reserva)

# Rota para deletar uma reserva
@router.delete("/cancelar/{reserva_id}")
async def cancelar_reserva_route(reserva_id: str, reserva_crud=Depends(reserva_factory)):
    try:
        # Chamando a função do CRUD que agora retorna um objeto ReservaResponse
        reserva_response = await reserva_crud.cancelar_reserva(reserva_id)
        return {"message": "Reserva cancelada com sucesso!", "data": reserva_response}
    except ReservaNotFoundException as e:
        # Se a exceção de reserva não encontrada for levantada, trata-se aqui
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    
# Rota para verificar a disponibilidade de uma sala
@router.post("/disponibilidade/")
async def verificar_disponibilidade(request: DisponibilidadeRequest, reserva_crud=Depends(reserva_factory)):
    disponibilidade = await reserva_crud.verificar_disponibilidade(request.bloco, request.numero_sala, request.data_inicio, request.data_fim)
    
    if disponibilidade:
        return {"message": "A sala está disponível para as datas solicitadas."}
    else:
        raise HTTPException(status_code=400, detail="A sala não está disponível para o período solicitado.")
    
@router.get("/notificacoes/")
async def notificacoes(reserva_crud=Depends(reserva_factory)):
    try:
        # Recupera as reservas futuras usando a função do ReservaCrud
        reservas_futuras = await reserva_crud.find_reservas_futuras(datetime.now())

        if not reservas_futuras:
            return {"message": "Não há reservas futuras para notificar."}

        # Envia a notificação para cada reserva
        for reserva_dict in reservas_futuras:
            # Converte o dicionário em uma instância de ReservaCreate (ou ReservaResponse)
            reserva = ReservaCreate(**reserva_dict)  # Converte o dict para um objeto de ReservaCreate

            # Chama a função de enviar notificação
            await ReservaCrud.enviar_notificacao(reserva)

        return {"message": "Notificações enviadas com sucesso!"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao enviar notificações: {str(e)}")
