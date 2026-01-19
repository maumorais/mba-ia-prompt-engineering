# reset.py

Utilitário de limpeza para remover datasets antigos ou conflitantes do LangSmith antes de iniciar uma nova bateria de testes.

## Funcionalidades Principais

1.  **Conexão com LangSmith**: Instancia o cliente.
2.  **Remoção de Dataset**: Tenta localizar e deletar o dataset chamado `dataset_docgen`.
    *   Se o dataset existir, ele é apagado para garantir que o upload subsequente (`upload_dataset.py`) crie uma versão limpa.
    *   Se não existir, informa que a operação não foi necessária.

## Uso

Execute este script se precisar resetar completamente os dados de teste no servidor.

```bash
python reset.py
```
