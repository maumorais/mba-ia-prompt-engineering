# Guia do Desenvolvedor: Módulo 5-langfuse

Este documento fornece uma análise técnica do diretório `5-langfuse`, que implementa um laboratório prático de **LLMOps** (Operações de LLM), focado especificamente em **Avaliação Comparativa (Pairwise Evaluation)** e gestão de prompts.

## 1. Semântica: O Problema que Ele Resolve

Em vez de avaliar uma resposta de IA subjetivamente, este módulo automatiza um **Teste A/B** robusto.

- **Cenário**: Você tem duas versões de um prompt (ex: `Prompt A` técnico vs `Prompt B` resumido).
- **Objetivo**: Saber qual performa melhor em uma bateria de testes padronizada.
- **Solução**: O sistema executa ambos os prompts, utiliza um terceiro LLM como "Juiz" para decidir o vencedor, e registra todos os passos e metadados em uma plataforma de observabilidade (Langfuse).

## 2. Estrutura Lógica (O Pipeline)

O código é separado em três responsabilidades distintas, simulando um pipeline de produção CI/CD para IA:

### A. Infrastructure as Code (`create_prompts.py`)
Responsável por definir os prompts como código (YAML) e registrá-los na nuvem.

- **Conceito Chave (Prompt Registry)**: O código Python nunca contém strings de prompt *hardcoded* (ex: "Você é um assistente..."). Ele apenas referencia prompts pelo ID (ex: `prompt_doc_a`).
- **Benefício**: Permite versionamento semântico. Se o script for executado novamente com alterações no YAML, o Langfuse cria novas versões (`v2`, `v3`) automaticamente, sem quebrar o código de produção que aponta para a tag/label `production`.

### B. Data Engineering (`upload_dataset.py`)
Responsável por definir o "gabarito" (*Golden Dataset*) para os testes.

- Carrega exemplos de *Input* (código fonte) e *Output Esperado* (documentação ideal) para o Langfuse.
- Isso garante que os testes sejam determinísticos, reprodutíveis e baseados em uma fonte de verdade imutável.

### C. Runtime Engine (`run.py`)
O orquestrador que executa a avaliação. É o componente central do pipeline:

1.  **Fetch**: Baixa os prompts versionados e o dataset do Langfuse.
2.  **Execute**: Roda o Prompt A e o Prompt B para cada item do dataset.
3.  **Judge**: Envia as duas respostas geradas + o gabarito para um LLM Juiz (`gpt-4o-mini`), perguntando: "Qual é melhor e por quê?".
4.  **Score**: Grava o resultado (Vitoria/Derrota/Empate) de volta nos metadados da execução original.

## 3. Padrões de Código para Estudar

Desenvolvedores devem atentar-se aos seguintes padrões implementados em `run.py`:

### Observabilidade Universal
```python
handler_a = CallbackHandler() # SDK do Langfuse
chain.invoke(..., config={"callbacks": [handler_a]})
```
Nenhuma chamada a LLM é feita "no escuro". Todas são instrumentadas para gerar *Traces* (rastros), permitindo debugar latência, custo, tokens e conteúdo exato enviado/recebido.

### Prompt-Chain Decoupling
```python
prompt_a = langfuse.get_prompt("prompt_doc_a", label="production")
```
O código pede explicitamente pela versão rotulada como `production`. Isso permite que engenheiros de prompt trabalhem em versões `staging` ou `dev` na UI do Langfuse sem quebrar a automação principal.

### Feedback Loop (Scoring)
O script não apenas lê dados; ele escreve o resultado da avaliação de volta no trace original:
```python
langfuse.create_score(
    trace_id=trace_id_a,
    name="Pairwise Result",
    value="Won"
)
```
Isso conecta a *execução* com a *qualidade*, permitindo a criação de dashboards analíticos (ex: "Taxa de Vitória do Prompt A nos últimos 30 dias").

## 4. Resumo

Este módulo demonstra engenharia de confiabilidade para sistemas de IA. Ele ensina como montar uma esteira de qualidade onde a alteração de um prompt passa por uma validação sistemática (**Dataset** -> **Execução** -> **Julgamento**) antes de ser considerada pronta para produção.
