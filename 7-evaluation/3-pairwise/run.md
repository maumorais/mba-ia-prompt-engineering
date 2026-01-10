# run.py: Avaliação Comparativa (Pairwise)

Este script executa uma **avaliação comparativa** (A/B Test) entre duas versões de prompts (`PairwiseA` e `PairwiseB`) utilizando um "LLM Juiz" para decidir qual resposta é melhor.

## O que este script faz?

1.  **Executa o Prompt A**: Roda o prompt de segurança (`pairwise_comparison_security`) contra o dataset.
2.  **Executa o Prompt B**: Roda o prompt de performance (`pairwise_comparison_performance`) contra o mesmo dataset.
3.  **Comparação (Pairwise)**: Usa um terceiro LLM (o juiz) para olhar as duas respostas lado a lado e decidir qual é a melhor, baseada nos critérios definidos em `pairwise_judge.yaml`.

## Conceitos Chave

1.  **Pairwise Evaluation**: Em vez de dar uma nota absoluta (0 a 10), o avaliador diz "A é melhor que B". Isso é frequentemente mais confiável para humanos e LLMs do que notas absolutas.
2.  **LLM-as-a-Judge**: Usar um LLM poderoso (ex: GPT-4o) para avaliar as saídas de outros modelos. O prompt do juiz deve ser muito claro sobre os critérios de desempate.
3.  **Experimentos Controlados**: O LangSmith permite comparar dois experimentos (`results_a` e `results_b`) e gerar estatísticas de vitória/derrota (win rates).

## Análise do Código

### 1. Definição dos Concorrentes
```python
PROMPT_A_ID = "pairwise_comparison_security"     # Prompt focado em segurança
PROMPT_B_ID = "pairwise_comparison_performance"  # Prompt focado em performance
```
Aqui definimos quais prompts estão batalhando. Normalmente são duas versões do mesmo prompt (v1 vs v2), mas aqui estamos comparando focos diferentes para ver qual o juiz prefere.

### 2. O Juiz
```python
judge_template = load_yaml_prompt("pairwise_judge.yaml")
pairwise_judge = create_pairwise_evaluator(judge_template, client)
```
O juiz recebe `prediction`, `prediction_b` e o `input` original. Ele deve retornar qual venceu.

### 3. Execução e Comparação
```python
pairwise_results = evaluate_comparative(
    [results_a.experiment_name, results_b.experiment_name],
    evaluators=[pairwise_judge],
    ...
)
```
A função `evaluate_comparative` do LangSmith automatiza o cruzamento dos resultados e a chamada do juiz para cada exemplo do dataset.

## Por que usar?

*   **Refinamento de Prompts**: Quando você faz uma alteração no prompt e quer saber se melhorou ou piorou.
*   **Preferência Humana Simulada**: Pairwise é o método padrão para treinar modelos (RLHF), pois reflete melhor a preferência subjetiva do que métricas rígidas.
