# 10-bad-not-helpful.py: Teste de Robustez (Respostas Vagas)

Este script simula o comportamento de "quiet quitting" ou preguiça do modelo: dar uma resposta tecnicamente correta, mas inútil.

## O que este script faz?

Usa o prompt `bad_not_helpful.yaml` que instrui o modelo a ser genérico (ex: "O código parece bom, continue assim"). Não aponta erros específicos, não sugere melhorias concretas.

## Conceitos Chave

1.  **Helpfulness (Utilidade)**: Uma métrica subjetiva, mas crucial. Uma resposta pode ser educada, gramaticalmente correta e formatada em JSON, mas ter utilidade zero.
2.  **Profundidade de Análise**: A capacidade de ir além do óbvio.

## Análise do Código e Expectativa

```python
evaluators = [
    LangChainStringEvaluator("score_string", config={"criteria": "helpfulness"...}),
    LangChainStringEvaluator("score_string", config={"criteria": "detail"...}),
]
```

*   **Helpfulness**: Deve ser baixa.
*   **Detail**: Deve ser muito baixa, pois a resposta é vaga.

## Por que usar?

Para garantir que você está pagando por inteligência, não por polidez. Seus avaliadores devem distinguir entre um relatório vazio e educado e uma análise técnica rigorosa. Isso ajuda a tunar seus prompts principais para exigirem *actionable insights* (insights acionáveis).