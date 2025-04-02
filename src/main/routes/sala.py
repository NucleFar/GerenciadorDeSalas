from fastapi import APIRouter, Depends
from src.static.models.sala import SalaCreate
from src.main.factories.sala_factory import sala_factory

router = APIRouter(tags=["salas"])

@router.post("/blocos/{bloco_nome}/salas/")
async def criar_sala_no_bloco(bloco_nome: str, sala: SalaCreate, sala_crud=Depends(sala_factory)):
    return await sala_crud.criar_sala_com_associacao(bloco_nome, sala)