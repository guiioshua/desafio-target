from fastapi import APIRouter

from desafio_target.api.schemas import RequisicaoTaxa, RespostaTaxa
from desafio_target.application.services import processar_request_taxa

route = APIRouter()

@route.post("/calcular-taxa", response_model= RequisicaoTaxa)
def handler_calcular_taxa(body: RequisicaoTaxa) -> RespostaTaxa:

    resposta_taxa = processar_request_taxa(
        taxa=body.taxa,
        cotas_diarias=body.model_dump()["cotas_por_acionista"])
    
    return resposta_taxa