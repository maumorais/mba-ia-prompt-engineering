# Prompt "Bad Not Helpful" (Não Útil)

## Descrição
Este prompt é **intencionalmente defeituoso**. Ele configura o modelo como um "revisor preguiçoso" que se recusa a fornecer detalhes úteis.

## Estrutura do Prompt
O prompt instrui o modelo a:
1.  **Ser Genérico**: Responder apenas "Code analyzed" ou "Looks OK".
2.  **Não Fornecer Detalhes**: "DO NOT provide details, findings...".
3.  **Ser Mínimo**: Resumo de no máximo 3 palavras.

## Variáveis de Entrada
*   `code`: O código a ser analisado.

## Uso
Este prompt serve como caso de teste negativo para métricas de **Utilidade** (Helpfulness). O avaliador deve ser capaz de penalizar severamente essa resposta, pois ela não agrega valor ao usuário.
