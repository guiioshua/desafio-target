# API para Cálculo de Taxa de Administração

API RESTful desenvolvida em Python com FastAPI para o cálculo da taxa de administração de fundos de investimento, conforme a fórmula especificada. O projeto foi construído com foco em boas práticas de arquitetura de software para garantir um código limpo, testável e manutenível.

## Arquitetura Aplicada

A estrutura do projeto é baseada nos princípios da **Clean Architecture** e do **Domain-Driven Design (DDD)**. Esta abordagem visa a separação de responsabilidades, resultando em um sistema com alta coesão e baixo acoplamento entre os componentes.

A aplicação é dividida nas seguintes camadas:

* **1. Domínio (`domain`):** Camada mais interna, contém a lógica de negócio pura e as regras essenciais do sistema. É completamente agnóstica a frameworks e tecnologias externas (web, banco de dados, etc.).
    * **Justificativa:** Para o cálculo principal, que envolve operações matriciais, foi utilizada a biblioteca **NumPy**. Esta escolha evita algoritmos com laços de repetição aninhados (complexidade `O(N*M)` em Python puro), que possuem baixa escalabilidade para grandes volumes de dados. O NumPy executa operações vetorizadas em baixo nível (C), resultando em performance superior por não incorrer no overhead da tipagem dinâmica do Python.

* **2. Aplicação (`application`):** Atua como intermediária, orquestrando a interação entre a camada de interface e a camada de domínio. Não contém regras de negócio.
    * **Justificativa:** Atualmente, o serviço de aplicação atua como um *passthrough*, repassando os dados já validados pela API para o domínio. Este design modular permite a futura inclusão de lógicas de orquestração, como logging, operações de I/O em banco de dados ou chamadas a outros serviços, sem impactar o núcleo do sistema.

* **3. API (`api`):** Camada mais externa, responsável por expor a funcionalidade ao mundo exterior.
    * **Justificativa:** O framework **FastAPI** foi escolhido por sua performance e, principalmente, pela robustez na validação de dados de entrada e saída através de modelos **Pydantic**. O uso de type hints e schemas Pydantic cria contratos de API explícitos, garantindo a integridade dos dados na fronteira do sistema. Adicionalmente, o FastAPI gera documentação interativa (Swagger UI / ReDoc) de forma automática a partir do código, otimizando o processo de desenvolvimento e a usabilidade da API.

## Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Framework Web:** FastAPI
* **Validação de Dados:** Pydantic
* **Computação Numérica:** NumPy
* **Servidor ASGI:** Uvicorn
* **Testes:** Pytest

## Instalação e Execução

Para executar o projeto localmente, siga os passos abaixo.

1.  **Clonar o Repositório**
    ```bash
    git clone https://github.com/guiioshua/desafio-target
    cd desafio_target
    ```

2.  **Criar e Ativar Ambiente Virtual**
    ```bash
    # Criar o ambiente
    python -m venv venv

    # Ativar no Windows (Git Bash) ou Linux/macOS
    source venv/Scripts/activate
    ```

3.  **Instalar as Dependências**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Instalar o Projeto em Modo Editável**
    Este passo é necessário para reconhecimento dos módulos Python do projeto.
    ```bash
    pip install -e .
    ```

5.  **Iniciar o Servidor**
    Na root do projeto:
    ```bash
    uvicorn desafio_target.api.main:app --reload
    ```
    A API estará em execução em `http://127.0.0.1:8000`. A documentação interativa pode ser acessada em `http://127.0.0.1:8000/docs`.

## Uso da API

### Endpoint
* **URL:** `/calcular-taxa`
* **Método:** `POST`

### Corpo da Requisição

Para um exemplo detalhado do formato do corpo da requisição, consulte o arquivo:
[Ver Exemplo de Requisição](./docs/example_request.json)

Para testar o endpoint utilizando o Postman, siga os seguintes passos:

1.  Configure a requisição com o método **`POST`** e insira a URL: `http://127.0.0.1:8000/calcular-taxa`.
2.  Navegue até a aba **"Body"**.
3.  Selecione a opção **`raw`** e, no menu suspenso à direita, escolha **`JSON`**.
4.  Cole o conteúdo do arquivo [example_request.json](./docs/example_request.json) na área de texto.
5.  Clique em **"Send"** para enviar a requisição. 

### Exemplo de Resposta
```json
[
    60.56,
    302.19,
    15.2
]
```
## Testes

A suíte de testes foi projetada para garantir a integridade de cada camada:
* **Teste de Unidade (Domínio):** Valida a correção da lógica de cálculo pura.
* **Teste de Unidade com Mocks (Aplicação):** Garante que a camada de aplicação orquestra corretamente as chamadas para a camada de domínio.
* **Teste de Integração (API):** Valida o fluxo completo, desde a requisição HTTP até a resposta, utilizando o `TestClient` do FastAPI.

Para executar todos os testes, utilize o comando:
```bash
pytest
