from pydantic import BaseModel

from typing import List

class CotaPorAcionista(BaseModel):
    valor: float
    quantidade_por_acionista: List[float]

class RequisicaoTaxa(BaseModel):
    taxa: float
    cotas_por_acionista: List[CotaPorAcionista]