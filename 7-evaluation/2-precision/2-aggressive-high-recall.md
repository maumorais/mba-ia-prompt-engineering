# 2-aggressive-high-recall.py: Alto Recall (Aggressive)

Este script demonstra o oposto do script anterior: uma estratégia de **Alto Recall**. O objetivo é encontrar o máximo de problemas possível, aceitando que isso vai gerar muitos alarmes falsos (Falsos Positivos).

## O que este script faz?

Utiliza um prompt "agressivo" (`prompts/aggressive.yaml`) que instrui o modelo a atuar como um auditor paranoico. Qualquer cheiro de código ruim, qualquer potencial vulnerabilidade, mesmo que remota, deve ser reportada.

## Conceitos Chave

1.  **Recall (Revocação)**: De todos os erros que existiam no código, quantos o modelo encontrou?
    *   *Alto Recall* = O modelo não deixa passar nada. É uma rede de pesca fina.
2.  **Falsos Negativos**: O modelo deixar de ver um bug crítico. Esta estratégia visa reduzir isso a zero.
3.  **Aggressive Strategy**: Útil em auditorias de segurança críticas onde o custo de perder uma vulnerabilidade é catastrófico (ex: contrato inteligente, software bancário).

## Análise do Código

### 1. Prompt Agressivo
```python
prompt = load_yaml_prompt("aggressive.yaml")
```
O prompt incentiva o modelo a especular sobre riscos e reportar "warnings" e sugestões de melhoria como se fossem erros, aumentando a cobertura.

### 2. Avaliação de Métricas
O código de avaliação é idêntico ao conservador (`calculate_precision_recall_f1`), o que muda é o **comportamento do modelo** induzido pelo prompt.

Esperamos ver:
*   **Recall**: Muito alto (perto de 1.0)
*   **Precision**: Baixa (muito lixo junto com o ouro)

## Por que usar?

Use esta estratégia quando o **custo do Falso Negativo for inaceitável**.
*   **Exemplo**: Ferramenta de auxílio para um auditor humano sênior. O humano vai filtrar os resultados, então não tem problema ter ruído (falsos positivos), desde que o sistema garanta que nenhuma vulnerabilidade real passou despercebida.
