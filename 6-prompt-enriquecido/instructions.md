# Instruções de Uso - Prompt Enriquecido

Este diretório explora técnicas avançadas de RAG (Retrieval-Augmented Generation) e expansão de query para melhorar a qualidade das respostas do LLM.

## Visão Geral

Aqui focamos em **como manipular a entrada** antes de enviá-la ao modelo final.

| Arquivo | Técnica | Descrição |
|---------|---------|-----------|
| `0-No-expansion.py` | Baseline | Execução padrão (Pergunta -> LLM -> Resposta) para servir de base de comparação. |
| `1-ITER_RETGEN.py` | ITER-RETGEN | "Generation-Augmented Retrieval". O modelo gera uma resposta preliminar (com lacunas), que é usada para buscar documentos, que por sua vez refinam a resposta, em um loop iterativo. |
| `2-query-enrichment.py` | Query Expansion | O modelo reescreve ou expande a pergunta do usuário (adicionando sinônimos, contexto ou quebrando em sub-perguntas) antes da busca ou execução. |

## Configuração do Ambiente

⚠️ **Atenção**: Este módulo utiliza uma versão **Alpha** do LangChain (`1.0.0a5`). Não misture o ambiente virtual deste diretório com os de outros módulos.

1.  **Criação do Venv**:
    ```bash
    python -m venv venv
    # Ativar: source venv/bin/activate (Linux/Mac) ou .\venv\Scripts\activate (Windows)
    pip install -r requirements.txt
    ```

2.  **Variáveis (.env)**:
    ```env
    OPENAI_API_KEY=sk-...
    ```

## Detalhes Técnicos

### LangChain 1.0 Alpha
Este projeto demonstra o uso da nova API `init_chat_model` que unifica a inicialização de modelos:
```python
# Exemplo da nova sintaxe
from langchain.chat_models import init_chat_model
llm = init_chat_model("openai:gpt-4o-mini", temperature=0)
```

### ITER-RETGEN (Iterative Retrieval-Generator)
O script `1-ITER_RETGEN.py` simula um fluxo onde:
1.  O LLM tenta responder.
2.  Identifica o que não sabe (simulado ou real).
3.  "Busca" informação (aqui simulado com um *mock* ou busca real se configurado).
4.  Refina a resposta.

Isso é crucial para reduzir alucinações em perguntas complexas onde uma única busca (Single-hop RAG) falharia.

## Como Executar

Execute sequencialmente para ver a evolução:

1.  **Sem expansão**:
    ```bash
    python 0-No-expansion.py
    ```
    *Observe a resposta possivelmente genérica ou incompleta.*

2.  **Com Enriquecimento**:
    ```bash
    python 2-query-enrichment.py
    ```
    *Veja como a pergunta é transformada para ser mais específica.*

3.  **Com Recuperação Iterativa**:
    ```bash
    python 1-ITER_RETGEN.py
    ```
    *Acompanhe o loop de refinamento no terminal.*
