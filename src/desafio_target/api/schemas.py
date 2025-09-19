from pydantic import BaseModel

from typing import List

class CotaDiaria(BaseModel):
    valor: float
    quantidades: List[float]

class RequisicaoTaxa(BaseModel):
    taxa: float
    cotas: List[float]