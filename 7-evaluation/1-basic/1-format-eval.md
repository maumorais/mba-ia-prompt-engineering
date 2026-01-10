# 1-format-eval.py: Validação Determinística de Formato

Este script representa a camada mais básica e essencial de qualquer pipeline de IA em produção: garantir que a saída do modelo seja estruturalmente válida antes de tentar processá-la.

## O que este script faz?

Diferente dos outros scripts desta pasta, este **não utiliza um LLM para avaliar outro LLM**. Ele utiliza validação programática (código Python clássico) para verificar se a resposta é um JSON válido e se adere a um esquema (schema) específico.

## Conceitos Chave

1.  **Avaliação Determinística**: O resultado é binário e objetivo. Não há "interpretação". Ou o JSON é válido, ou não é. É rápido e custa zero tokens.
2.  **Schema Validation**: Não basta ser um JSON; precisa ter os campos certos. O script define um `EXPECTED_SCHEMA` que obriga a resposta a ter uma lista de `findings` e um resumo `summary`.

## Análise do Código

### 1. Configuração do Avaliador de Validade JSON
```python
json_eval = LangChainStringEvaluator(
    "json_validity",
    prepare_data=prepare_prediction_only
)
```
Este avaliador nativo do LangChain verifica apenas se a string de saída (`prediction`) pode ser convertida (parsed) via `json.loads`. Se o modelo devolver texto antes ou depois do JSON, isso falhará (a menos que o parser seja permissivo, mas aqui o objetivo é rigor).

### 2. Validação de Schema (Lógica Customizada)
```python
def validate_schema(run, example):
    try:
        output = run.outputs.get("output", "")
        data = json.loads(output)
        jsonschema.validate(instance=data, schema=EXPECTED_SCHEMA)
        return {"score": 1.0, "comment": "Valid schema"}
    except ...
```
Aqui criamos uma função python pura que recebe a `run` (execução do LangSmith).
*   **Sucesso (Score 1.0)**: O JSON contém todos os campos obrigatórios (`findings`, `summary`, etc.) e os tipos corretos.
*   **Falha (Score 0.0)**: O JSON está quebrado ou falta campos obrigatórios.

## Por que usar?

Em sistemas reais, se o seu agente precisa salvar dados num banco ou chamar uma API, uma resposta em formato errado quebra a aplicação. Esta é a primeira linha de defesa e deve ser monitorada para saber com que frequência seu prompt falha em seguir instruções de formatação.