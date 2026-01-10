# 0-only-traces.py

Este script demonstra como integrar o **Langfuse** para rastreamento (tracing) automático de execuções do LangChain.

## Funcionalidades Principais

*   **Configuração de Callback**: Utiliza o `CallbackHandler` do Langfuse para interceptar e registrar as interações do LLM.
*   **Prompt de Exemplo**: Define um agente "historiador de linguagens de programação" para gerar narrativas sobre Python, Go e JavaScript.
*   **Execução com Rastreamento**: Ao invocar a chain (`chain.invoke`), passa o handler via `config={"callbacks": [langfuse_handler]}`, o que envia automaticamente os traces (inputs, outputs, latência, consumo de tokens) para o painel do Langfuse.

## Uso

Execute para testar a conexão com o Langfuse e ver os traces aparecerem no dashboard.

```bash
python 0-only-traces.py
```