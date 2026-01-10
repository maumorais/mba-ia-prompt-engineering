# upload_dataset.py

Responsável por enviar o conjunto de dados de teste (contendo códigos fonte e documentação de referência) para o LangSmith.

## Funcionalidades Principais

1.  **Leitura do Dataset Local**: Lê o arquivo `dataset.jsonl` localizado na mesma pasta.
    *   O dataset contém entradas com múltiplos arquivos de código (`files`) e saídas esperadas (`reference`).
2.  **Upload para LangSmith**: Utiliza a função `upload_langsmith_dataset` (do módulo compartilhado) para criar o dataset `dataset_docgen` no projeto.

## Uso

Deve ser executado obrigatoriamente antes da primeira execução do `run.py`, ou após o uso do `reset.py`.

```bash
python upload_dataset.py
```
