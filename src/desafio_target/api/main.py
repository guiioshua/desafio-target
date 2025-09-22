from fastapi import FastAPI
from .routes import router as api_router

app = FastAPI(
    title="API de Cálculo de Taxa de Administração de Fundos",
    version="1.0.0",
    description="Uma API para calcular a taxa de administração de fundos de investimento."
)

app.include_router(api_router)