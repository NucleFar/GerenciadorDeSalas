from fastapi import HTTPException

class HttpNotFound(HTTPException):
    def __init__(self, detail: str) -> None:
        super().__init__(status_code=404, detail=detail)

class ReservaNotFoundException(Exception):
    def __init__(self, reserva_id: str):
        self.reserva_id = reserva_id
        self.status_code = 404
        self.detail = f"Reserva com ID {reserva_id} não encontrada."