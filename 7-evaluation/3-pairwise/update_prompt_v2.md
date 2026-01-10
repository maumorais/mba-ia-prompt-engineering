# update_prompt_v2.py

Este script simula o ciclo de vida de engenharia de prompt, atualizando uma versão existente de um prompt no LangSmith com melhorias.

## Funcionalidades Principais

1.  **Carregamento da Versão V2**: Lê o arquivo `prompts/security_expert_v2.yaml`.
2.  **Atualização de Prompt**: Faz o *push* desta nova versão para o identificador existente `pairwise_comparison_security`.
    *   Isso cria um novo *commit* no histórico do prompt no LangSmith, permitindo comparar a performance da V1 (criada por `create_prompts.py`) contra a V2.

## Uso

Execute este script após ter rodado o experimento inicial e desejar testar uma versão aprimorada do prompt.

```bash
python update_prompt_v2.py
```
