# langfuse_helpers.py

Módulo utilitário contendo funções para facilitar a interação entre objetos do Langfuse e a execução via LangChain.

## Funcionalidades Principais

*   **`run_with_chat_prompt(prompt_obj, inputs, client)`**:
    *   Compila um objeto de prompt do Langfuse com as variáveis de entrada.
    *   Converte a lista de mensagens resultante para o formato `SystemMessage`, `HumanMessage`, etc., do LangChain.
    *   Executa o modelo e retorna o conteúdo.

*   **`run_with_text_prompt(prompt_obj, client, **kwargs)`**:
    *   Similar ao anterior, mas para prompts de texto simples (não-chat).

*   **`parse_judge_response` e `format_reasoning_summary`**:
    *   Funções auxiliares para processar a saída JSON do "LLM Juiz" e formatá-la para exibição legível (logs ou comentários no Langfuse).

## Uso

Importado pelo script principal `run.py` para abstrair a complexidade de conversão de mensagens entre Langfuse SDK e LangChain.
