# 3-criteria-score-eval.py: Avaliação Contínua (Pontuação)

Enquanto a avaliação binária é "preto no branco", a avaliação contínua permite nuances. Este script mostra como obter notas (scores) que variam de 0.0 a 1.0, permitindo medir melhorias ou degradações sutis no modelo.

## O que este script faz?

Utiliza o avaliador `score_string` (ou `labeled_score_string`) para atribuir uma nota à resposta. O LangChain solicita ao LLM juiz que dê uma nota de 1 a 10, e depois normaliza isso para 0.0 a 1.0.

## Conceitos Chave

1.  **Granularidade**: Permite diferenciar uma resposta "ruim" (0.2) de uma resposta "medíocre" (0.5) e de uma "excelente" (0.9).
2.  **Múltiplos Critérios**: O script avalia várias dimensões simultaneamente: coerência, detalhe, profundidade e relevância.

## Análise do Código

### 1. Configuração de Pontuação
```python
LangChainStringEvaluator(
    "score_string",
    config={"criteria": "coherence", "normalize_by": 10},
    prepare_data=prepare_with_input
)
```
*   **`score_string`**: Instrui o LLM a pensar passo-a-passo e atribuir uma nota numérica.
*   **`normalize_by: 10`**: O LLM dá uma nota de 1 a 10, e o sistema divide por 10 para o reporte final.

### 2. Critérios Selecionados
*   **Coherence**: A estrutura lógica faz sentido?
*   **Detail**: O modelo citou linhas específicas ou foi vago?
*   **Depth**: A análise foi superficial ou encontrou a raiz do problema?
*   **Relevance** (com referência): O modelo respondeu o que foi pedido no gabarito?

## Por que usar?

Em **Code Review** (o tema deste projeto), um código pode estar "correto" mas ser "mal explicado". A avaliação binária aprovaria. A avaliação por score revelaria que a "Profundidade" caiu de 0.8 para 0.4, indicando que o modelo ficou preguiçoso, mesmo que tecnicamente correto. Isso é crucial para manter a qualidade da experiência do usuário (UX).