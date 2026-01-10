# run.py: Avaliação de Documentação (Híbrida)

Este script demonstra uma avaliação sofisticada para tarefas de geração de documentação, combinando **avaliação baseada em critérios** (absoluta) com **avaliação comparativa** (relativa/pairwise).

## O que este script faz?

Ele avalia dois prompts que geram documentação técnica a partir de código.
1.  **Avaliação Individual**: Cada prompt é avaliado quanto à conformidade (se segue o template, se inclui seções obrigatórias) usando `doc_evaluators`.
2.  **Avaliação Comparativa**: As saídas dos dois prompts são comparadas diretamente para ver qual gerou uma explicação mais clara e útil.

## Conceitos Chave

1.  **Avaliação Híbrida**: Nem tudo se resolve com comparação. Às vezes você precisa saber se o formato está certo (critério absoluto) *e* se o texto está bom (comparação relativa).
2.  **Conformance Checking**: Verificar se a documentação gerada adere a um guia de estilo (style guide) ou estrutura rígida.

## Análise do Código

### 1. Avaliadores de Documentação
```python
doc_evaluators = create_evaluators_for_documentation(client)
```
Esta lista de avaliadores (definida em `doc_evaluators.py`) provavelmente verifica critérios específicos como: "Tem seção de Exemplo?", "Descreve os parâmetros?", "Usa tom profissional?". Eles rodam *durante* a execução individual.

### 2. Avaliação Comparativa Final
```python
pairwise_results = evaluate_comparative(
    [results_a.experiment_name, results_b.experiment_name],
    evaluators=[pairwise_judge],
    ...
)
```
Após saber se ambos respeitam o formato, o juiz comparativo decide qual texto ficou melhor escrito.

## Por que usar?

Ideal para tarefas criativas mas estruturadas, como:
*   Geração de READMEs.
*   Docstrings de funções.
*   Resumos de reuniões.

Você garante o *compliance* (formato) e maximiza a *qualidade* (conteúdo).
