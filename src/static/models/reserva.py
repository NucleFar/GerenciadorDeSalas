from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ReservaModel(BaseModel):
    bloco: str
    numero_sala: int
    data_inicio: datetime
    data_fim: datetime
    nome_coordenador: str
    motivo: str
    frequencia: str
    dia_da_semana: Optional[str]
    numero_de_ocorrencias: Optional[str]

class ReservaCreate(ReservaModel):
    pass

class Config:
    from_attributes = True

class ReservaResponse(ReservaModel):
    id: Optional[str] = None

class DisponibilidadeRequest(BaseModel):
    bloco: str
    numero_sala: int
    data_inicio: datetime
    data_fim: datetime