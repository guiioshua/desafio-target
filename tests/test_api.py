from fastapi.testclient import TestClient
from pytest import approx
from desafio_target.api.main import app

client = TestClient(app)

def test_handler_calcular_taxa_success():
    # 1. ARRANGE: I/O MOCK PARA OS TESTES
    test_request = {
        "taxa": 0.01,
        "cotas": [
            {"valor": 1000, "quantidades": [10, 100]},
            {"valor": 2000, "quantidades": [10, 100]}
        ]
    }
    # Resultado esperado:
    # 1000 * [10, 100] = [10000, 100000] * 0.01 = [100, 1000]
    # 2000 * [10, 100] = [20000, 200000] * 0.01 = [200, 2000]
    # Redução do eixo 0: [100+200, 1000+2000] =   [300, 3000]
    # [300, 3000] / 252 = [1.19, 11.90]
    test_mock_resultado = [1.19, 11.90]

    # 2. ACT: ENVIO DA REQUISIÇÃO POST
    resposta = client.post("/calcular-taxa", json=test_request)

    # 3. ASSERT: VERIFICAR DADOS DA RESPOSTA
    assert resposta.status_code == 200

    resposta_output = resposta.json()
    assert isinstance(resposta_output, list)
    assert len(resposta_output) == 2
    
    assert resposta_output[0] == approx(test_mock_resultado[0], abs=1e-2)
    assert resposta_output[1] == approx(test_mock_resultado[1], abs=1e-2)


def test_handler_calcular_taxa_failure():
    # 1. ARRANGE: I/O MOCK INCOMPLETO
    test_request = {
        "taxa": 0.01,

    }

    # 2. ACT: ENVIO DA REQUISIÇÃO
    resposta = client.post("/calcular-taxa", json=test_request)

    # 3. ASSERT: VERIFICAR FALHA NA RESPOSTA
    assert resposta.status_code == 422


