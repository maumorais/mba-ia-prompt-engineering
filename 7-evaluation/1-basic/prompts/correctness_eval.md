# Prompt Avaliação de Corretude

## Descrição
Este é um prompt padrão ("bom") que configura um **Revisor Técnico**. Ele busca identificar problemas de forma direta e correta.

## Estrutura do Prompt
Simples e direto:
1.  **Persona**: Revisor especializado em análise técnica.
2.  **Tarefa**: Analisar código e identificar problemas.
3.  **Formato**: JSON estrito.

## Variáveis de Entrada
*   `code`: O código a ser analisado.

## Uso
Serve como **Baseline (Linha de Base)** para os experimentos de avaliação de corretude. É o "controle positivo" contra o qual os prompts "ruins" (`bad_hallucination`, `bad_text_before`, etc.) são comparados para verificar se o avaliador consegue distinguir entre uma análise útil e uma falha.
