from typing import List
from fastapi import APIRouter

from desafio_target.api.schemas import RequisicaoTaxa, RespostaTaxa
from desafio_target.application.services import processar_request_taxa

router = APIRouter()

@router.post("/calcular-taxa", response_model = List[float])
def handler_calcular_taxa(body: RequisicaoTaxa) -> RespostaTaxa:

    resposta_taxa = processar_request_taxa(
        taxa=body.taxa,
        cotas=body.model_dump()["cotas"])
    
    resposta_formatada = [round(taxa, 2) for taxa in resposta_taxa]
    
    return resposta_formatada