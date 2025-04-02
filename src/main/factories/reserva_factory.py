from src.crud.reserva_crud import ReservaCrud
from src.database.database import get_db
from fastapi import Depends

def reserva_factory(db=Depends(get_db)):
    return ReservaCrud(db)