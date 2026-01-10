# upload_dataset.py: Carga de Dados de Teste

Este é o script de setup inicial. Antes de rodar qualquer avaliação (`1-format-eval.py` etc.), os dados precisam estar na nuvem (LangSmith).

## O que este script faz?

1.  Lê o arquivo local `dataset.jsonl` (JSON Lines).
2.  Converte cada linha em um "Exemplo" (Example) compatível com o LangSmith.
3.  Faz o upload desses exemplos para um dataset chamado `evaluation_basic_dataset`.

## Conceitos Chave

1.  **Dataset KV (Key-Value)**: O LangSmith espera datasets no formato de pares Chave-Valor. Geralmente:
    *   **Inputs**: O que entra no modelo (ex: código a ser revisado).
    *   **Outputs (Reference)**: O que se espera que saia (ex: lista de bugs reais).
2.  **Versionamento**: Se você rodar este script múltiplas vezes sem rodar o `reset.py`, o LangSmith *adicionará* novos exemplos ao dataset existente, criando versões novas do dataset.

## Análise do Código

```python
count = upload_langsmith_dataset(
    DATASET_FILE,
    DATASET_NAME,
    "Shared dataset for basic evaluators",
    client
)
```
A função `upload_langsmith_dataset` (importada de `shared.datasets`) abstrai a complexidade de ler o arquivo linha a linha e chamar a API `client.create_example` para cada uma.

## Estrutura do `dataset.jsonl`
O script espera que o arquivo JSONL tenha campos que correspondam ao que seus prompts esperam. No nosso caso, os prompts usam a variável `{code}`, então o dataset deve ter uma chave correspondente nos inputs.

## Por que usar?

Centralizar seus casos de teste na nuvem permite que:
1.  Todo o time use os mesmos testes.
2.  Você possa rodar testes via interface web do LangSmith.
3.  Você mantenha histórico de qual versão do dataset foi usada em qual experimento.