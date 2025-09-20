from pydantic import BaseModel

from typing import List

class CotaPorinvestidor(BaseModel):
    valor: float
    quantidade_por_investidor: List[float]

class RequisicaoTaxa(BaseModel):
    taxa: float
    cotas_por_investidor: List[CotaPorinvestidor]

class RespostaTaxa(BaseModel):
    taxas_por_investidor: List[float]