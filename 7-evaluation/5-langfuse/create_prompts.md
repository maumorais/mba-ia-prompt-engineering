# create_prompts.py

Script de inicialização responsável por criar e registrar todos os prompts necessários para os experimentos desta pasta no Langfuse.

## Funcionalidades Principais

1.  **Conversão de Formato**: Lê arquivos YAML (formato LangChain/Genérico) e os converte para a estrutura de prompt nativa do Langfuse.
2.  **Gerenciamento de Prompts**:
    *   **Chat Prompts**: Cria `prompt_doc_a`, `prompt_doc_b` e `1-correctness-langfuse`.
    *   **Text Prompt**: Cria `llm_judge_pairwise` (prompt do juiz).
3.  **Etiquetagem**: Adiciona labels como `production`, `documentation` e `evaluation` para facilitar a organização no dashboard.

## Uso

Execute uma vez para popular o registro de prompts do Langfuse antes de rodar os experimentos.

```bash
python create_prompts.py
```
