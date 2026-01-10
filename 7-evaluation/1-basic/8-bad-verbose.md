# 8-bad-verbose.py: Teste de Robustez (Verbosidade)

Este script testa como os avaliadores lidam com respostas excessivamente longas e confusas.

## O que este script faz?

Usa o prompt `bad_verbose.yaml`, que instrui o modelo a "explicar cada pensamento", "ser extremamente detalhado" e até "contradizer-se se necessário". O resultado é um texto enorme ("muro de texto") difícil de ler.

## Conceitos Chave

1.  **Sinal vs. Ruído**: Uma resposta longa não é necessariamente boa. Pode conter a informação correta (sinal) soterrada em divagações (ruído).
2.  **Penalização por Coerência**: Avaliadores de coerência devem identificar que o texto divaga e perde o foco.

## Análise do Código e Expectativa

```python
evaluators = [
    # Detects verbosity
    LangChainStringEvaluator("score_string", config={"criteria": "conciseness"...}),
    # Detects incoherence
    LangChainStringEvaluator("score_string", config={"criteria": "coherence"...}),
]
```

*   **Conciseness (Concisão)**: Deve vir **muito baixa**. O modelo falhou em ser direto.
*   **Coherence (Coerência)**: Deve vir **baixa**, pois o prompt força contradições.

## Por que usar?

Muitos desenvolvedores assumem erroneamente que "respostas maiores são melhores/mais inteligentes". Este teste serve para calibrar seus avaliadores para valorizarem a clareza e síntese, punindo a "enrolação" (fluff).