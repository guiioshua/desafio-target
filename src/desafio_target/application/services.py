from desafio_target.domain.services import calcular_taxa_administracao
from typing import List, Dict, Any

def processar_request_taxa(taxa: float, cotas: List[Dict[str, Any]]) -> List[float]:

    return calcular_taxa_administracao(taxa = taxa, cotas = cotas)