# Prompt "Bad Hallucination" (Alucinação Forçada)

## Descrição
Este prompt é **intencionalmente defeituoso**. Ele instrui o modelo a atuar como um "especialista em segurança" que **inventa** problemas que não existem.

## Estrutura do Prompt
O prompt contém instruções maliciosas (no contexto de teste):
1.  **Inventar Problemas**: "Invent and list security issues that DO NOT exist".
2.  **Ser Criativo na Mentira**: Assumir SQL injection, buffer overflow, etc., mesmo que o código não tenha.
3.  **Resumo Dramático**: Criar um resumo alarmista.

## Variáveis de Entrada
*   `code`: O código a ser "analisado".

## Uso
Este prompt serve como um caso de teste negativo ("Bad Case") para sistemas de avaliação. O objetivo é verificar se:
*   As métricas de **Corretude** (Correctness) detectam que a resposta está errada.
*   As métricas de **Alucinação** (Hallucination) disparam um alerta.
