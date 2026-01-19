# Prompt Avaliação de Critérios

## Descrição
Este é um prompt minimalista que configura um **Revisor Especializado**. Semelhante ao `correctness_eval`, mas ainda mais conciso em suas instruções.

## Estrutura do Prompt
1.  **Instrução Básica**: "Analyze the following code snippet".
2.  **Formato**: JSON estrito.

## Variáveis de Entrada
*   `code`: O código a ser analisado.

## Uso
Utilizado em scripts como `2-criteria-binary-eval.py` e `3-criteria-score-eval.py`. O objetivo é fornecer uma saída padrão que será então avaliada por um "LLM Judge" (Juiz LLM) com base em critérios binários (Pass/Fail) ou escalas de pontuação (1-5).
