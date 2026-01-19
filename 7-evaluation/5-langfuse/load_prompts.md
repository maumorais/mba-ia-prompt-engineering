# load_prompts.py

Script utilitário leve para carregar ou atualizar especificamente o prompt de análise de código (`1-correctness-langfuse`) no Langfuse.

## Funcionalidades Principais

*   Carrega a definição do prompt do arquivo `prompts/1-correctness-langfuse.yaml`.
*   Cria/Atualiza o prompt no Langfuse com o tipo `chat` e labels apropriados (`production`, `code-analysis`).

## Uso

Útil para atualizações rápidas neste prompt específico sem precisar rodar o script de criação completo.

```bash
python load_prompts.py
```
