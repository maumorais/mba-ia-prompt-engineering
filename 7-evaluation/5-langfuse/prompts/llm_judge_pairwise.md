# Prompt Juiz para Comparação Pairwise (Versão LangFuse)

## Descrição
Este prompt define um "Juiz LLM" para avaliar documentação técnica, idêntico ao utilizado na pasta `4-pairwise-doc`, mas localizado aqui para suportar os experimentos de integração com o LangFuse.

## Estrutura do Prompt
O prompt instrui o modelo a comparar duas documentações (A e B) contra uma referência (Ground Truth) em 5 dimensões:
1.  Completude Estrutural
2.  Precisão Técnica
3.  Clareza e Utilidade
4.  Alinhamento com a Referência
5.  Concisão vs Detalhe

## Variáveis de Entrada
*   `code`: Código fonte.
*   `reference`: Documentação de referência.
*   `answer_a`: Documentação A.
*   `answer_b`: Documentação B.

## Uso
Utilizado em scripts de avaliação pairwise que reportam resultados para o LangFuse. O juiz determina qual versão do prompt de documentação (`prompt_doc_a` vs `prompt_doc_b`) teve melhor desempenho.
