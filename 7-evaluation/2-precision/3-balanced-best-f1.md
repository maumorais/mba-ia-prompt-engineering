# 3-balanced-best-f1.py: Melhor Equilíbrio (Balanced F1)

Este script busca o "caminho do meio": maximizar o **F1 Score**, que é a média harmônica entre Precisão e Recall. É a estratégia ideal para uso geral, onde queremos detectar bugs reais sem inundar o usuário com falsos alertas.

## O que este script faz?

Utiliza o prompt `prompts/balanced.yaml`. Este prompt foi calibrado para ser assertivo mas justo, instruindo o modelo a verificar evidências antes de acusar, mas sem ser excessivamente tímido.

## Conceitos Chave

1.  **F1 Score**: Uma métrica única que resume a qualidade do modelo.
    *   F1 só é alto se *ambos* (Precisão e Recall) forem razoáveis. Se um deles for zero, o F1 despenca.
2.  **Trade-off**: Em IA, quase sempre ganhar Recall custa Precisão e vice-versa. O prompt balanceado tenta otimizar a fronteira desse trade-off.

## Análise do Código

### 1. Prompt Balanceado
```python
prompt = load_yaml_prompt("balanced.yaml")
```
Este prompt geralmente contém definições claras do que constitui um bug ("Definição de Pronto"), ajudando o modelo a classificar corretamente casos de borda.

### 2. Comparação de Resultados
Ao rodar os três scripts (Conservative, Aggressive, Balanced) e comparar os outputs, você verá:
*   **Conservative**: Poucos findings, quase todos corretos.
*   **Aggressive**: Muitos findings, muitos incorretos.
*   **Balanced**: Quantidade média de findings, mantendo a maioria dos bugs reais e filtrando o ruído óbvio.

## Por que usar?

Esta é a estratégia padrão para **Assistentes de Código** (como o GitHub Copilot ou ferramentas de análise estática em IDEs). O usuário quer ajuda útil no dia-a-dia.
*   Se for muito conservador, o usuário acha a ferramenta "burra" (não vê nada).
*   Se for muito agressivo, o usuário acha a ferramenta "chata" (reclama de tudo) e a desativa.
*   O equilíbrio (Balanced) é onde reside a utilidade máxima para o desenvolvedor médio.
