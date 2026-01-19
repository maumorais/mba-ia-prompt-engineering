# 4-correctness-eval.py: Avaliação de Corretude (Ground Truth)

Este script foca na métrica mais crítica para aplicações de conhecimento: o modelo acertou a resposta? Ele demonstra como comparar a saída gerada com uma "resposta de ouro" (gold standard) armazenada no dataset.

## O que este script faz?

Ele executa uma avaliação focada estritamente na fidelidade da resposta em relação ao esperado. Diferente de avaliar "estilo" (como concisão), aqui avaliamos "fatos".

## Conceitos Chave

1.  **Labeled Evaluators**: Avaliadores que *exigem* uma referência. Eles leem o campo `output` (ou similar) do seu dataset `dataset.jsonl` e o tratam como a verdade absoluta.
2.  **Alinhamento Semântico**: O LLM juiz é capaz de entender que "Use prepared statements" é semanticamente igual a "Utilize consultas parametrizadas", dando nota alta mesmo que as palavras sejam diferentes. Isso é a grande vantagem sobre métricas antigas como BLEU ou ROUGE.

## Análise do Código

```python
LangChainStringEvaluator(
    "labeled_score_string",
    config={"criteria": "correctness", "normalize_by": 10},
    prepare_data=prepare_with_reference
)
```

*   **`labeled_score_string`**: Usa o LLM para dar uma nota baseada na comparação.
*   **`prepare_with_reference`**: Função auxiliar que monta o prompt do juiz contendo:
    1.  O Input do usuário.
    2.  A Resposta do Modelo (Prediction).
    3.  A Resposta de Referência (Reference).

O prompt interno do LangChain pergunta algo como: "Considerando a resposta de referência, quão correta é a resposta do modelo?".

## Por que usar?

Para evitar alucinações críticas. Se você tem um dataset de vulnerabilidades de segurança conhecidas (ex: SQL Injection na linha 10), você precisa garantir que o modelo identifique *exatamente* isso. A métrica de `correctness` mede essa precisão factual.