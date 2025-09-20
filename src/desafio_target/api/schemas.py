from pydantic import BaseModel

from typing import List

class CotaPorinvestidor(BaseModel):
    valor: float
    quantidades: List[float]

class RequisicaoTaxa(BaseModel):
    taxa: float
    cotas: List[CotaPorinvestidor]

class RespostaTaxa(BaseModel):
    taxas_por_investidor: List[float]