# Prompt Enriquecido (Enriched Prompting)

Este diretório contém exemplos de técnicas avançadas de **Engenharia de Prompt** focadas em enriquecer o contexto e a qualidade das respostas geradas por LLMs (Large Language Models).

Os scripts demonstram desde a abordagem mais simples (sem enriquecimento) até técnicas iterativas complexas para refinamento de respostas e clarificação de perguntas.

## 📂 Conteúdo

### 1. `0-No-expansion.py` (Baseline)
Exemplo básico de interação com o modelo sem nenhuma técnica de expansão ou enriquecimento. Serve como linha de base para comparação.
- **Técnica:** Zero-shot prompting simples.
- **Objetivo:** Responder a uma pergunta diretamente.

### 2. `1-ITER_RETGEN.py` (Iterative Retrieval-Generation)
Implementação da técnica **ITER-RETGEN** (Geração e Recuperação Iterativa).
- **Técnica:** O modelo gera um rascunho inicial identificando lacunas de conhecimento (marcando com `[MISSING: ...]`). Em seguida, gera queries para preencher essas lacunas e refina a resposta iterativamente até que esteja completa.
- **Destaque:** Demonstra como fazer o modelo "criticar" e melhorar sua própria resposta em múltiplos passos, simulando um processo de pesquisa e redação.

### 3. `2-query-enrichment.py` (Query Enrichment)
Implementação de um sistema interativo de **Enriquecimento de Query**.
- **Técnica:** Transforma uma solicitação vaga do usuário em uma query detalhada e estruturada. O sistema identifica informações faltantes críticas (baseado em uma configuração pré-definida, ex: revisão de PR) e faz perguntas de clarificação ao usuário.
- **Destaque:** Garante que o modelo tenha todo o contexto necessário *antes* de tentar realizar a tarefa, resultando em respostas muito mais precisas e úteis.

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8+
- Uma chave de API da OpenAI (ou outra compatível com LangChain).

### Instalação

1. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure as variáveis de ambiente:**
   Crie um arquivo `.env` na raiz desta pasta (baseado no `.env.example` se existir, ou crie do zero) e adicione sua chave de API:
   ```env
   OPENAI_API_KEY=sk-...
   ```

### Executando os Exemplos

Execute cada script individualmente para ver a técnica em ação:

```bash
# 1. Baseline (Sem expansão)
python 0-No-expansion.py

# 2. Iterative Retrieval-Generation (Refinamento automático)
python 1-ITER_RETGEN.py

# 3. Query Enrichment (Interativo - requer input do usuário)
python 2-query-enrichment.py
```

## 📚 Conceitos Chave

- **Prompt Expansion:** Aumentar o prompt original com mais contexto ou instruções para guiar melhor o modelo.
- **Iterative Refinement:** O processo de melhorar a saída em vários passos, em vez de tentar obter a resposta perfeita em uma única tentativa.
- **Clarification:** A capacidade do agente de pedir mais informações ao usuário quando a solicitação inicial é ambígua ou incompleta.
