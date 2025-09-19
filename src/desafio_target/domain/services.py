from typing import Any, Dict, List
import numpy as np


def calcular_taxa_admnistracao(taxa: float, cotas_diarias: List[Dict[str, Any]]) -> List[float]:
    
    if not cotas_diarias:
        return []

    # Um elemento de cada uma dessas listas para cada dia
    valores = [dia['valor'] for dia in cotas_diarias]
    quantidades = [dia['quantidades'] for dia in cotas_diarias]

    valores_vetor = np.array(valores)          # Formato (N,)
    quantidades_matriz = np.array(quantidades) # Formato (N, M)

    if quantidades_matriz == []:
        return []
    
    patrimonio_por_dia = quantidades_matriz * valores_vetor[:, np.newaxis] # Formato: (N, M)

    total_por_investidor = patrimonio_por_dia.sum(axis=0)

    taxas = (total_por_investidor * taxa) / 252

    return taxas.tolist()