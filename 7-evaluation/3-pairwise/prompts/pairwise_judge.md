# Prompt de Juiz para Comparação Pairwise (Segurança vs Performance)

## Descrição
Este prompt define um juiz técnico **imparcial** encarregado de avaliar duas revisões de código distintas para o mesmo trecho de código. Ele compara especificamente uma revisão focada em segurança (Resposta A) contra uma revisão focada em performance (Resposta B) - ou variações destas.

## Estrutura do Prompt
O prompt instrui o modelo a:
1.  **Analisar o Código e as Respostas**: Recebe o código original e duas análises (A e B).
2.  **Avaliar Objetivamente**: Baseado em três critérios principais:
    *   **Existência Real**: Os problemas apontados realmente existem no código?
    *   **Impacto**: Qual conjunto de problemas afeta mais a qualidade (Vulnerabilidade Crítica vs Performance Ruim)?
    *   **Acionabilidade**: Qual feedback é mais claro e fácil de corrigir?
3.  **Regras de Decisão**:
    *   Não favorecer "segurança" automaticamente.
    *   Priorizar problemas reais e críticos, seja de segurança ou performance.
    *   Considerar código lento e código vulnerável como igualmente problemáticos dependendo da severidade.
4.  **Formato de Saída**: Apenas "A", "B" ou "TIE".

## Variáveis de Entrada
*   `code`: O trecho de código sendo analisado.
*   `answer_a`: A saída do primeiro especialista (geralmente o Security Expert).
*   `answer_b`: A saída do segundo especialista (geralmente o Performance Expert).

## Uso
Utilizado em experimentos de avaliação pairwise para determinar qual prompt de especialista gera mais valor em cenários onde diferentes tipos de problemas podem estar presentes. Ajuda a calibrar a utilidade relativa de focos diferentes de revisão (segurança vs performance).
