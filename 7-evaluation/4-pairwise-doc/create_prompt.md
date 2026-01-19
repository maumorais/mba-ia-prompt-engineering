# create_prompt.py

Este script é responsável por criar e registrar as duas variantes de prompts (`prompt_doc_a` e `prompt_doc_b`) no LangSmith, que serão posteriormente comparadas pelo processo de avaliação pairwise.

## Funcionalidades Principais

1.  **Leitura de YAML**: Carrega as configurações dos prompts a partir de arquivos YAML (`prompts/prompt_doc_a.yaml` e `prompts/prompt_doc_b.yaml`).
2.  **Conversão para ChatTemplate**: Transforma as definições YAML em objetos `ChatPromptTemplate` do LangChain.
3.  **Registro (Push) no LangSmith**:
    *   Registra o **Prompt A** com o ID `prompt_doc_a` (focado em documentação técnica estruturada).
    *   Registra o **Prompt B** com o ID `prompt_doc_b` (focado em documentação narrativa).

## Uso

Execute este script na configuração inicial do ambiente ou sempre que fizer alterações nos arquivos YAML dos prompts.

```bash
python create_prompt.py
```
