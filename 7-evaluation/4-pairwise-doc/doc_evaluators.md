# doc_evaluators.py

Este módulo define um conjunto robusto de avaliadores (evaluators) personalizados para analisar a qualidade da documentação gerada de forma individual, antes da comparação pairwise.

## Funcionalidades Principais

A função `create_evaluators_for_documentation(client)` retorna uma lista de 7 avaliadores baseados em LLM que medem:

1.  **Alinhamento de Concisão**: Verifica se a verbosidade corresponde à referência (Ground Truth).
2.  **Nível de Detalhe**: Compara a profundidade técnica (tipos, parâmetros) com a referência.
3.  **Tom e Estilo**: Avalia formalidade e complexidade da linguagem.
4.  **Alinhamento Estrutural**: Verifica se segue as mesmas seções e hierarquia da referência.
5.  **Cobertura de Conteúdo**: Confirma se os tópicos essenciais foram abordados.
6.  **Consistência Terminológica**: Checa o uso correto de termos técnicos e convenções de nomenclatura.
7.  **Fidelidade (Faithfulness)**: Garante que a documentação não inventa funcionalidades inexistentes no código (alucinação).

Cada avaliador normaliza a pontuação em uma escala de 0 a 10 (via `normalize_by=10`) ou 0 a 1.

## Uso

Este módulo é importado e utilizado pelo script principal (`run.py`) para configurar a fase de avaliação individual dos experimentos.

```python
from doc_evaluators import create_evaluators_for_documentation
# ...
evaluators = create_evaluators_for_documentation(client)
```
