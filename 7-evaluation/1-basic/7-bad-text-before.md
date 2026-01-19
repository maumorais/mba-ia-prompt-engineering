# 7-bad-text-before.py: Teste de Robustez (Falha de Formato)

Este script inicia a série de "Negative Tests" (Testes Negativos). O objetivo aqui não é avaliar o *modelo*, mas sim **testar a eficácia dos seus avaliadores**.

## O que este script faz?

Ele utiliza propositalmente um prompt "ruim" (`bad_text_before.yaml`) que instrui o modelo a ser conversador e adicionar texto introdutório antes de entregar o JSON (ex: "Aqui está a análise que você pediu: {json}"). Isso é um erro comum que quebra parsers.

## Conceitos Chave

1.  **Meta-Avaliação**: Avaliar o avaliador. Se o seu avaliador de formato der nota 10 para esse modelo, seu avaliador está quebrado.
2.  **Robustez de Prompt**: Testar como o sistema reage a instruções que conflitam com as restrições de formato.

## Análise do Código e Expectativa

```python
# Evaluators focused on detecting lack of detail and depth
evaluators = [
    LangChainStringEvaluator("score_string", config={"criteria": "detail"...}),
    # ...
]
```

O script roda o prompt ruim e aplica os avaliadores.
*   **Cenário**: O modelo gera texto tagarela + JSON.
*   **Expectativa**: Esperamos que avaliadores de `format_adherence` (se usados) deem nota baixa. Neste exemplo específico, focamos em métricas de qualidade como `detail` e `depth`. Como o prompt ruim foca em ser "otimista e ignorar problemas", a nota de `depth` (profundidade) deve ser **baixa**.

## Por que usar?

Para garantir que seu pipeline de avaliação não seja um "carimbo de aprovação" cego. Você precisa provar que seu sistema de notas penaliza erros reais.