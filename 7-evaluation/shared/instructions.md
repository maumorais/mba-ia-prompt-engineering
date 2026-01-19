# Guia do Desenvolvedor: Módulo shared

Este documento fornece uma análise técnica do diretório `shared`, que atua como uma biblioteca de utilitários comum para todos os módulos de avaliação.

## 1. Semântica: O Problema que Ele Resolve

Evita a duplicação de código (DRY) ao centralizar:
1.  **Inicialização de Clientes**: Lógica complexa para decidir qual provedor usar (Google vs OpenAI).
2.  **Parsing de Dados**: Lógica robusta para limpar JSON "sujo" gerado por LLMs.
3.  **Adaptação de Dados**: Funções helper para transformar objetos de execução (`Run`) em dicionários que o LangSmith entende.

## 2. Componentes Principais

### `clients.py` (Factory Pattern)
Responsável por instanciar os modelos.
- **Regra de Negócio**: Prioridade para Google Gemini (`GOOGLE_API_KEY`) sobre OpenAI (`OPENAI_API_KEY`).
- **Uso**:
  ```python
  from shared.clients import get_llm_client
  llm = get_llm_client() # Retorna ChatGoogleGenerativeAI ou ChatOpenAI automaticamente
  ```

### `parsers.py` (Robustez)
Responsável por sanitizar saídas.
- **Problema**: LLMs frequentemente retornam JSON embrulhado em blocos de código markdown (ex: ` ```json {...} ``` `).
- **Solução**: `parse_json_response` detecta e remove esses wrappers antes de tentar o `json.loads`.

### `evaluators.py` (Adapter Pattern)
Responsável por conectar a saída do seu script ao formato esperado pelos avaliadores do LangSmith.
- **Funções**:
  - `prepare_prediction_only`: Para avaliadores simples (ex: validação de formato).
  - `prepare_with_input`: Para avaliadores que precisam ver a pergunta original.
  - `prepare_with_reference`: Para avaliadores que comparam com um gabarito.

## 3. Resumo

Ao criar um novo script de avaliação:
1.  **Sempre** importe `get_llm_client` de `shared.clients` em vez de instanciar `ChatOpenAI` diretamente. Isso garante portabilidade.
2.  **Sempre** use `parse_json_response` se seu prompt pede JSON.
3.  Estude `evaluators.py` se seu avaliador no LangSmith reclamar de "missing keys".
