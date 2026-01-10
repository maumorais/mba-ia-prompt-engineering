# pairwise_helpers.py

Este módulo contém funções auxiliares para facilitar a avaliação comparativa (pairwise) entre dois modelos ou prompts.

## Funcionalidades Principais

*   **`create_pairwise_evaluator(judge_prompt_obj, client)`**:
    *   Cria uma função avaliadora personalizada que aceita duas saídas (`answer_a` e `answer_b`) e utiliza um "LLM Juiz" para determinar qual é a melhor.
    *   **Lógica de Pontuação**:
        *   Retorna `[1.0, 0.0]` se A for melhor.
        *   Retorna `[0.0, 1.0]` se B for melhor.
        *   Retorna `[0.5, 0.5]` em caso de empate.
    *   Utiliza o prompt do juiz (configurado via YAML) para estruturar a decisão.

## Exemplo de Uso

```python
from pairwise_helpers import create_pairwise_evaluator

# ... carregar prompt do juiz e cliente LLM ...
evaluator = create_pairwise_evaluator(judge_prompt, client)

# Usado internamente pelo evaluate_comparative do LangSmith
```
