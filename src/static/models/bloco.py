from pydantic import BaseModel
from typing import Optional, List

class BlocoModel(BaseModel):
    nome: str
    identificador: str
    cursos: Optional[List[str]] = []  # Lista de IDs de cursos (inicialmente vazia)
    salas: Optional[List[str]] = []  # Lista de IDs de salas (inicialmente vazia)

class BlocoCreate(BlocoModel):
    pass

class Config:
    from_attributes = True

class BlocoResponse(BlocoModel):
    id: Optional[str] = None
