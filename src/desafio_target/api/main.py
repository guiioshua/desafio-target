from fastapi import FastAPI
from .routes import route as api_router

# 1. Create the FastAPI app instance with metadata
app = FastAPI(
    title="API de Cálculo de Taxa de Administração de Fundos",
    version="1.0.0",
    description="Uma API para calcular a taxa de administração de fundos de investimento."
)

# 2. Include the router from routes.py
app.include_router(api_router)