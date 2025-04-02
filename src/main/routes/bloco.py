from fastapi import APIRouter, Depends
from src.static.models.bloco import BlocoCreate, BlocoResponse
from src.main.factories.bloco_factory import bloco_factory

router = APIRouter(tags=["blocos"])

@router.post("/blocos/", response_model=BlocoResponse)
async def criar_bloco(bloco: BlocoCreate, bloco_crud=Depends(bloco_factory)):
    return await bloco_crud.criar_bloco(bloco)
