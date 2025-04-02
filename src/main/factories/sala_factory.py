from src.crud.sala_crud import SalaCrud
from src.database.database import get_db
from fastapi import Depends

def sala_factory(db=Depends(get_db)):
    return SalaCrud(db)  # Retorna a instância de BlocoCrud com o db