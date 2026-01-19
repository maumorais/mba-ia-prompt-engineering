# Guia do Desenvolvedor: Módulo 1-basic

Este documento fornece uma análise técnica do diretório `1-basic`, que serve como o ponto de entrada para entender a suite de avaliação do LangSmith.

## 1. Semântica: O Problema que Ele Resolve

Este módulo ensina, de forma progressiva, como sair da avaliação manual ("olhômetro") para avaliações sistemáticas usando diferentes técnicas, desde checagens simples de formato até julgamentos complexos por LLM.

- **Cenário**: Você precisa garantir que a saída do seu LLM é válida (JSON), concisa, útil ou correta em relação a um gabarito.
- **Solução**: Utilizar a biblioteca de avaliadores (`evaluators`) do LangChain/LangSmith para automatizar essas verificações.

## 2. Progressão Lógica (O Caminho de Aprendizado)

O módulo é estruturado em níveis de complexidade:

### Nível 1: Determinístico (Sem LLM)
- **Script**: `1-format-eval.py`
- **Técnica**: `JsonValidityEvaluator`.
- **Uso**: Verifica se a string de saída é um JSON válido. É rápido, barato e binário (0 ou 1). Ideal para pipelines onde o formato estruturado é crítico.

### Nível 2: Avaliação Binária com LLM
- **Script**: `2-criteria-binary-eval.py`
- **Técnica**: `CriteriaEvaluator` (labeled "criteria").
- **Uso**: Usa um LLM para responder perguntas de Sim/Não sobre a saída. Ex: "A resposta é concisa?". Retorna 0 ou 1.

### Nível 3: Avaliação Contínua (Score)
- **Script**: `3-criteria-score-eval.py`
- **Técnica**: `ScoreStringEvaluator` (labeled "score_string").
- **Uso**: Similar ao binário, mas retorna uma nota de 0.0 a 1.0 (ex: 0.8). Permite medir melhorias sutis de qualidade (ex: "Quão útil é a resposta?").

### Nível 4: Comparação com Referência (Correctness)
- **Script**: `4-correctness-eval.py`
- **Técnica**: `LabeledScoreStringEvaluator` (labeled "labeled_score_string").
- **Diferença Chave**: Introduz o conceito de **Ground Truth**. O avaliador recebe a saída do LLM **E** a resposta correta esperada (do dataset), comparando as duas para dar uma nota de correção.

### Nível 5: Critérios Customizados
- **Script**: `5-additional-criteria.py`
- **Técnica**: Definição de prompts de avaliação personalizados.
- **Uso**: Quando os critérios padrão (concisão, relevância) não bastam. Você define o que é "Fidelidade ao Código" e o avaliador segue sua regra.

### Nível 6: Similaridade Semântica
- **Script**: `6-embedding-distance-eval.py`
- **Técnica**: Distância de vetores (Embeddings).
- **Uso**: Calcula matematicamente quão próximo o significado do texto gerado está da referência, sem usar um LLM caro para julgar. Ótimo para verificar consistência semântica em escala.

## 3. Padrões de Código Importantes

### O Padrão `evaluate()`
Todos os scripts seguem o mesmo padrão de execução do LangSmith:
```python
evaluate(
    target_function, # A função que gera a resposta (sua chain/LLM)
    data=dataset_name, # O nome do dataset no LangSmith
    evaluators=[evaluator_config], # Lista de critérios a aplicar
    experiment_prefix="nome-do-experimento"
)
```

### Preparação de Dados (`prepare_data`)
O LangSmith espera chaves específicas (`prediction`, `input`, `reference`). Funções auxiliares (frequentemente importadas de `shared` ou definidas localmente) adaptam a saída do seu modelo para esse formato:
```python
def prepare_data(run, example):
    return {
        "prediction": run.outputs["output"],
        "input": example.inputs["code"],
        "reference": example.outputs["reference"] # Apenas para avaliadores 'labeled'
    }
```

## 4. Resumo

Este módulo é a fundação. Desenvolvedores devem dominar estes conceitos antes de tentar arquiteturas complexas como Pairwise ou RAG Evaluation.
- Comece com **format-eval** para garantir que seu sistema não quebra.
- Use **correctness-eval** quando tiver um gabarito confiável.
- Use **embedding-eval** para testes de regressão baratos em larga escala.
