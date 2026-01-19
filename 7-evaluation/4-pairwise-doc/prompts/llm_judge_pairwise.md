# Prompt de Juiz para Comparação de Documentação

## Descrição
Este prompt define um "juiz LLM" especializado em avaliar e comparar documentação técnica de software. Ele é projetado para receber duas variantes de documentação gerada (A e B), juntamente com o código fonte original e uma documentação de referência (ground truth), e determinar qual das duas variantes é superior com base em critérios objetivos.

## Estrutura do Prompt
O prompt instrui o modelo a atuar como um avaliador especialista e fornece:
1.  **Contexto**: O código analisado, a documentação de referência e as duas documentações candidatas (A e B).
2.  **Métricas de Avaliação**: Cinco dimensões específicas para pontuação (0-10):
    *   Completude Estrutural
    *   Precisão Técnica
    *   Clareza e Utilidade
    *   Alinhamento com a Referência
    *   Concisão vs Detalhe
3.  **Regras de Decisão**: Critérios para determinar o vencedor, incluindo pesos para métricas críticas e regras para empates.
4.  **Formato de Resposta**: Exige estritamente um JSON estruturado contendo a decisão final, pontuações detalhadas por métrica e justificativas específicas.

## Variáveis de Entrada
*   `code`: O código fonte original que foi documentado.
*   `answer_a`: O texto da primeira documentação gerada.
*   `answer_b`: O texto da segunda documentação gerada.
*   `reference`: A documentação considerada padrão-ouro (ground truth).

## Uso
Este prompt é fundamental para a etapa de **avaliação pairwise**. Ele permite automatizar a comparação de diferentes versões de prompts geradores de documentação (`prompt_doc_a` vs `prompt_doc_b`), fornecendo uma análise detalhada e quantitativa sobre qual prompt produz resultados de melhor qualidade segundo os critérios estabelecidos.
