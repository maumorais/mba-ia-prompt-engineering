# Prompt Avaliação de Formato

## Descrição
Este prompt foca quase exclusivamente na **conformidade do formato de saída**.

## Estrutura do Prompt
1.  **Instrução Principal**: "You are a code reviewer that always responds in JSON."
2.  **Ênfase**: Repete várias vezes a necessidade de JSON RAW e "NEVER USE MARKDOWN".

## Variáveis de Entrada
*   `code`: O código a ser analisado.

## Uso
Utilizado no script `1-format-eval.py`. O objetivo primordial deste teste é verificar se o modelo obedece às restrições de formatação (retornar um JSON válido parseável) e não se a análise do código em si está correta. É um teste de "instrução de formato" (Format Compliance).
