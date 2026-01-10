# reset.py

Este script serve como um utilitário de limpeza para remover os recursos criados durante os experimentos desta pasta no LangSmith. Útil para reiniciar o estado do projeto.

## Funcionalidades Principais

1.  **Remoção de Dataset**: Deleta o dataset `pairwise_initial_comparison` do LangSmith.
2.  **Remoção de Prompts**: Remove os prompts registrados:
    *   `pairwise_comparison_security`
    *   `pairwise_comparison_performance`

## Uso

Execute com cautela, pois isso apagará os dados históricos do experimento no LangSmith.

```bash
python reset.py
```
