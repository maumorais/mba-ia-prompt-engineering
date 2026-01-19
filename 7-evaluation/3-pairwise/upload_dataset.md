# upload_dataset.py

Este script é responsável por carregar o conjunto de dados (dataset) que será utilizado para avaliar e comparar os prompts.

## Funcionalidades Principais

1.  **Leitura de Dados**: Localiza o arquivo `dataset.jsonl` no diretório do script.
2.  **Upload para LangSmith**: Utiliza funções compartilhadas (`shared.datasets`) para criar ou atualizar o dataset chamado `pairwise_initial_comparison` no LangSmith.

## Uso

Deve ser executado para popular o LangSmith com os casos de teste antes de rodar qualquer avaliação (`run.py`).

```bash
python upload_dataset.py
```
