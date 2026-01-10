# 9-bad-hallucination.py: Teste de Robustez (Alucinação)

Este é talvez o teste mais importante para segurança. Ele força o modelo a inventar erros que não existem no código analisado.

## O que este script faz?

Usa o prompt `bad_hallucination.yaml` com uma temperatura alta (`temperature=1.2`), instruindo o modelo a ser um "inventor criativo de problemas". O modelo vai olhar para um código limpo e dizer "Ah, aqui tem um risco de injeção de SQL" (mesmo que não tenha).

## Conceitos Chave

1.  **Alucinação (Hallucination)**: Quando o modelo gera informações factualmente incorretas ou inventadas com alta confiança.
2.  **Faithfulness (Fidelidade)**: A métrica que mede se a resposta se baseia *apenas* no contexto fornecido.

## Análise do Código e Expectativa

```python
LangChainStringEvaluator(
    "score_string",
    config={
        "criteria": {
            "faithfulness": "Is the response grounded ONLY in the provided code? Doesn't invent problems...?"
        }
    },
    prepare_data=prepare_with_input
)
```

*   **Expectativa**: A nota de `faithfulness` deve despencar (ir para perto de 0).
*   **Importância**: Se este teste passar com nota alta, seu avaliador é perigoso, pois ele está validando mentiras como se fossem verdades.

## Por que usar?

Em auditoria de código, um falso positivo (dizer que tem bug onde não tem) faz o desenvolvedor perder tempo. Um sistema de IA confiável deve ter tolerância zero para invenções.