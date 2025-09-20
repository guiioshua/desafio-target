from typing import List
from fastapi import APIRouter

from desafio_target.api.schemas import RequisicaoTaxa, RespostaTaxa
from desafio_target.application.services import processar_request_taxa

route = APIRouter()

@route.post("/calcular-taxa", response_model = List[float])
def handler_calcular_taxa(body_model: RequisicaoTaxa) -> RespostaTaxa:

    resposta_taxa = processar_request_taxa(
        taxa=body_model.taxa,
        cotas=body_model.model_dump()["cotas"])
    
    return resposta_taxa