# upload_dataset.py

Responsável por popular o Langfuse com os dados de teste para os experimentos de análise de código Go.

## Funcionalidades Principais

1.  **Leitura do Dataset**: Carrega dados do arquivo local `dataset2.jsonl`.
2.  **Upload para Langfuse**:
    *   Cria ou atualiza o dataset chamado `go-ds` no Langfuse.
    *   Utiliza a função `upload_langfuse_dataset` para gerenciar os itens e metadados.

## Detalhes

*   **Arquivo Fonte**: `dataset2.jsonl`
*   **Nome no Langfuse**: `go-ds`

## Uso

Execute antes de rodar avaliações de correção (`1-correctness-langfuse.py`) ou o pipeline completo (`run.py`) se este depender dos mesmos dados.

```bash
python upload_dataset.py
```
