# 2-criteria-binary-eval.py: Avaliação Binária com LLMs

Este script introduz o conceito de "LLM-as-a-Judge" (LLM como juiz), onde usamos um modelo (geralmente mais forte ou igual ao avaliado) para julgar a qualidade da resposta. Aqui, o foco é em decisões rápidas: **Passa ou Reprova**.

## O que este script faz?

Ele executa o prompt definido em `criteria_eval.yaml` e usa o GPT-4 (via LangSmith) para responder "Sim" (1) ou "Não" (0) para perguntas específicas sobre a qualidade da resposta gerada.

## Conceitos Chave

1.  **Avaliador `criteria`**: É um tipo de avaliador do LangChain que espera uma resposta binária. É útil para métricas que não aceitam meio-termo (ex: "O código é seguro?").
2.  **Reference-Free vs. Reference-Based**:
    *   **Reference-Free (`prepare_with_input`)**: O juiz avalia a resposta apenas olhando para a pergunta (input). Ex: "A resposta é concisa?".
    *   **Reference-Based (`prepare_with_reference`)**: O juiz compara a resposta do modelo com uma resposta ideal (gabarito) que está no dataset. Ex: "A resposta está correta?".

## Análise do Código

### 1. Avaliação de Estilo (Sem Referência)
```python
LangChainStringEvaluator(
    "criteria",
    config={"criteria": "conciseness"},
    prepare_data=prepare_with_input
)
```
O LangSmith usa um prompt interno que pergunta: "A submissão é concisa e direta ao ponto?". Se sim, retorna 1. Se não, 0.

### 2. Avaliação de Corretude (Com Referência)
```python
LangChainStringEvaluator(
    "labeled_criteria",
    config={"criteria": "correctness"},
    prepare_data=prepare_with_reference
)
```
Note o uso de `"labeled_criteria"`. O termo "labeled" indica que o avaliador terá acesso ao rótulo (label/reference) do dataset. O LLM vai comparar o output gerado com o output esperado e decidir se eles batem factualmente.

## Por que usar?

Avaliações binárias são ótimas para criar dashboards executivos (ex: "% de respostas corretas") e para testes de regressão (ex: "Se a concisão cair abaixo de 90% de aprovação, bloqueia o deploy").