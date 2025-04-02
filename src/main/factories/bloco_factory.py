from src.crud.bloco_crud import BlocoCrud
from src.database.database import get_db
from fastapi import Depends

def bloco_factory(db=Depends(get_db)):
    return BlocoCrud(db)  # Retorna a instância de BlocoCrud com o db