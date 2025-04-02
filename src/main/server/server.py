from fastapi import FastAPI
from src.main.routes.bloco import router as bloco_router
from src.main.routes.sala import router as sala_router
from src.main.routes.reserva import router as reserva_router

app = FastAPI()

app.include_router(bloco_router)
app.include_router(sala_router)
app.include_router(reserva_router)
