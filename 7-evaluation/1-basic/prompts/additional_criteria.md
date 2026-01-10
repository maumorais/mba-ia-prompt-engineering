# Prompt Critérios Adicionais

## Descrição
Este prompt configura o modelo como um **Revisor de Código Rigoroso**. Ele é usado para testar se métricas de avaliação personalizadas (como severidade, clareza, etc.) conseguem capturar nuances além do básico.

## Estrutura do Prompt
O prompt é direto e instrui o modelo a:
1.  **Analisar Qualidade e Segurança**: Identificar problemas de qualidade, segurança e melhores práticas.
2.  **Formato JSON**: Retornar findings e summary em formato JSON estrito.

## Variáveis de Entrada
*   `code`: O código a ser analisado.

## Uso
Utilizado em scripts de avaliação (`5-additional-criteria.py`) para verificar se avaliadores baseados em LLM conseguem pontuar corretamente critérios específicos definidos pelo usuário.
