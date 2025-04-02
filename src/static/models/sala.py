from pydantic import BaseModel
from typing import Optional, List

class SalaModel(BaseModel):
    bloco_id: str
    nome_e_número: str
    capacidade: int
    recursos: List[str] = [] # Lista de recursos (inicialmente vazia)

class SalaCreate(SalaModel):
    pass

class Config:
    from_attributes = True

class SalaResponse(SalaModel):
    id: Optional[str] = None