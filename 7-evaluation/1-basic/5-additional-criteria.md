# 5-additional-criteria.py: Critérios Personalizados

Os critérios padrão (concisão, utilidade) nem sempre cobrem as regras de negócio específicas. Este script ensina a criar seus próprios critérios de avaliação injetando definições customizadas no prompt do juiz.

## O que este script faz?

Ele define critérios que não existem nativamente no LangChain, como "Faithfulness" (Fidelidade ao contexto) e "Code Specificity" (Especificidade Técnica), passando descrições textuais detalhadas do que constitui uma boa ou má resposta nesses aspectos.

## Conceitos Chave

1.  **Prompt Engineering para Avaliadores**: Você está, essencialmente, programando o LLM juiz com linguagem natural. A qualidade da sua definição do critério determina a qualidade da avaliação.
2.  **Domain-Specific Metrics**: Criar métricas que só fazem sentido para o seu domínio (no caso, revisão de código).

## Análise do Código

### Exemplo: Code Specificity
```python
config={
    "criteria": {
        "code_specificity": "Does the analysis mention specific line numbers? Uses precise technical terminology (e.g., sql_injection, n_plus_1_query)? Provides actionable details instead of generic ones?"
    },
    "normalize_by": 10
}
```
Aqui, em vez de passar uma string simples como `"conciseness"`, passamos um dicionário. A chave é o nome do critério e o valor é a instrução para o LLM.

O LLM lerá: *"Avalie a resposta baseado no critério 'code_specificity': A análise menciona números de linha específicos? Usa terminologia técnica precisa?..."*

### Exemplo: Format Adherence
```python
"format_adherence": "Did the response follow EXACTLY the format instructions? Returned ONLY valid JSON...?"
```
Isso ajuda a detectar quando o modelo "quase" acerta o formato mas adiciona texto extra ("Aqui está seu JSON: ..."), o que quebraria um parser.

## Por que usar?

Esta é a técnica mais poderosa para refinar o comportamento do modelo. Se você percebe que seu modelo está sendo muito "amigável" mas pouco "técnico", você cria um critério de "Rigor Técnico" e começa a medir e otimizar para isso.