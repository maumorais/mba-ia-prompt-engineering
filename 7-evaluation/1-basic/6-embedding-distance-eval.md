# 6-embedding-distance-eval.py: Avaliação via Distância de Embeddings

Este script demonstra uma abordagem alternativa à avaliação com LLMs: usar representações vetoriais (embeddings) para medir a similaridade semântica. É uma técnica "híbrida" entre a rigidez das métricas exatas e a flexibilidade dos LLMs.

## O que este script faz?

Ele converte tanto a resposta do modelo quanto a resposta de referência em vetores numéricos de alta dimensão (usando modelos como `text-embedding-3-small` da OpenAI) e calcula a proximidade geométrica entre eles (distância cosseno ou euclidiana).

## Conceitos Chave

1.  **Embeddings**: São listas de números que representam o significado do texto. Frases com significados parecidos têm vetores parecidos (próximos no espaço matemático).
2.  **Distância vs. Similaridade**:
    *   Geralmente medimos a *distância*. Quanto **menor** o valor, **mais parecidos** são os textos.
    *   Zero (0.0) significaria identidade semântica perfeita.

## Análise do Código

```python
LangChainStringEvaluator(
    "embedding_distance",
    prepare_data=prepare_with_reference
)
```
Este avaliador, por baixo dos panos:
1.  Chama a API de embeddings para o `prediction` (resposta do modelo).
2.  Chama a API de embeddings para o `reference` (gabarito).
3.  Calcula a distância.

## Vantagens e Desvantagens

*   **Vantagem (Custo/Velocidade)**: É muito mais barato e rápido do que chamar um GPT-4 para avaliar cada resposta.
*   **Desvantagem (Cegueira de Detalhe)**: Embeddings capturam o "tema geral", mas podem falhar em detalhes precisos. Por exemplo, "O código tem um bug na linha 10" e "O código não tem bugs na linha 10" são frases semanticamente muito próximas (compartilham quase todas as palavras e o tema), mas significam o oposto. Embeddings podem achar que são similares (distância baixa), o que seria um erro de avaliação.

## Por que usar?

É excelente para triagem inicial em grandes volumes de dados (milhares de exemplos) onde usar LLMs seria proibitivo, ou para tarefas de RAG (Retrieval Augmented Generation) para verificar se o trecho recuperado é relevante para a pergunta.