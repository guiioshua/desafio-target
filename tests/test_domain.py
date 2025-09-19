import numpy as np
from desafio_target.domain.services import calcular_taxa_admnistracao

def test_fee_calculation_with_numpy():
    """
    Tests that the administration fee calculation is correct.
    """
    # 1. INPUT PARA OS TESTES
    taxa_input = 0.01
    cotas_input = [
        {"valor": 10.0, "quantidades": [100, 200, 50]},
        {"valor": 10.1, "quantidades": [100, 200, 50]},
        {"valor": 9.9,  "quantidades": [100, 210, 50]}, # Note a change for investor 1
    ]

    # Manually calculate the correct, expected result for the assertion
    # For investor 0: (100*10.0 + 100*10.1 + 100*9.9) * 0.01 / 252
    expected_fee_0 = ((100 * 10.0) + (100 * 10.1) + (100 * 9.9)) * 0.01 / 252
    
    # For investor 1: (200*10.0 + 200*10.1 + 210*9.9) * 0.01 / 252
    expected_fee_1 = ((200 * 10.0) + (200 * 10.1) + (210 * 9.9)) * 0.01 / 252

    # For investor 2: (50*10.0 + 50*10.1 + 50*9.9) * 0.01 / 252
    expected_fee_2 = ((50 * 10.0) + (50 * 10.1) + (50 * 9.9)) * 0.01 / 252
    
    expected_output = [expected_fee_0, expected_fee_1, expected_fee_2]

    # 2. FUNÇÃO SENDO TESTADA
    actual_output = calcular_taxa_admnistracao(taxa_input, cotas_input)

    # 3. COMPARA OS DOIS ARRAYS APROXIMADAMENTE
    np.testing.assert_allclose(actual_output, expected_output)

def test_fee_calculation_with_empty_input():
    # ARRANGE
    taxa_input = 0.01
    cotas_input = []
    expected_output = []

    # ACT
    actual_output = calcular_taxa_admnistracao(taxa_input, cotas_input)

    # ASSERT
    assert actual_output == expected_output