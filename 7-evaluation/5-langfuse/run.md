# run.py

Script principal de execução da avaliação **Pairwise com Langfuse**. Orquestra todo o fluxo de comparação entre dois prompts de documentação.

## Fluxo de Execução

1.  **Carregamento de Recursos**:
    *   Recupera os prompts versionados do Langfuse (`prompt_doc_a`, `prompt_doc_b`) e o prompt do juiz (`llm_judge_pairwise`).
    *   Carrega o dataset de teste (`code-ds`).

2.  **Conversão para LangChain**:
    *   Transforma os objetos de prompt do Langfuse em Chains executáveis do LangChain.

3.  **Execução dos Experimentos**:
    *   Para cada item do dataset:
        *   **Executa Prompt A**: Gera documentação e registra o trace.
        *   **Executa Prompt B**: Gera documentação e registra o trace.
        *   **Executa Juiz Pairwise**: Compara as saídas de A e B contra a referência (Ground Truth).

4.  **Registro de Scores (Scoring)**:
    *   Interpreta a decisão do juiz (JSON com scores e justificativas).
    *   **Score no Juiz**: Registra quem venceu no trace da execução do juiz.
    *   **Score nos Experimentos**: Adiciona scores categóricos (`Won`, `Lost`, `Tie`) retroativamente aos traces originais de A e B, permitindo análise agregada de taxas de vitória no dashboard.

## Uso

```bash
python run.py
```

Após a execução, os resultados podem ser visualizados na interface do Langfuse, filtrando pelo timestamp exibido no log.
