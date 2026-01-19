# Instruções de Uso - Gerenciamento e Versionamento de Prompts

Este módulo implementa uma arquitetura profissional de **PromptOps** (operações de prompt), tratando prompts como código (Prompt-as-Code) com versionamento semântico, registro centralizado e testes automatizados.

## Visão Geral

O sistema é dividido em duas camadas principais:

1.  **Registro Local (`registry.yaml`)**: Um arquivo central que mapeia IDs de agentes para versões específicas de prompts no sistema de arquivos.
2.  **Testes Automatizados (`pytest`)**: Uma suíte de testes que valida a sintaxe YAML, a integridade dos templates Jinja2/f-string e a presença de variáveis obrigatórias.

## Estrutura de Diretórios

```text
5-gerenciamento.../
├── prompts/
│   ├── registry.yaml           # Fonte da verdade (quem usa qual versão)
│   ├── agent-code-reviewer/    # Prompts do Agente Reviewer
│   │   └── v1/
│   │       ├── prompt.yaml     # Definição do prompt
│   │       └── prompt.tests.yaml # Casos de teste (inputs esperados)
│   └── ...
├── src/
│   ├── prompt_registry.py      # Lógica de carregamento do registro
│   └── agent_code_reviewer.py  # Exemplo de consumo do prompt
└── tests/
    └── test_prompts.py         # Pipeline de validação (CI/CD)
```

## Configuração do Ambiente

1.  **Dependências**:
    ```bash
    python -m venv venv
    # Ative o venv (source venv/bin/activate ou .\venv\Scripts\activate)
    pip install -r requirements.txt
    ```

2.  **Variáveis (.env)**:
    Necessário apenas se for usar a integração com LangSmith ou executar os agentes com a OpenAI.
    ```env
    OPENAI_API_KEY=sk-...
    LANGCHAIN_API_KEY=lsv2-... (Opcional)
    ```

## Fluxo de Trabalho (Workflow)

### 1. Criar/Editar um Prompt
Ao invés de hardcodar strings no Python, você define o prompt em um arquivo YAML:

```yaml
# prompts/meu-agente/v1/prompt.yaml
_type: prompt
input_variables: ["contexto"]
template: |
  Você é um assistente útil.
  Contexto: {contexto}
```

### 2. Registrar a Versão
Atualize o `prompts/registry.yaml` para apontar para a nova versão:

```yaml
meu_agente:
  id: "meu-agente"
  version: "1.0.0"
  path: "prompts/meu-agente/v1/prompt.yaml"
```

### 3. Validar (CI/CD)
Execute os testes para garantir que você não quebrou nada (ex: variáveis faltando no template):

```bash
pytest tests/test_prompts.py -v
```

### 4. Consumir no Código
Use o `PromptRegistry` para carregar o prompt de forma segura:

```python
from src.prompt_registry import PromptRegistry

registry = PromptRegistry()
prompt_info = registry.get_prompt("meu_agente")
# prompt_info.content contém o template carregado
```

## Integração com LangSmith (Opcional)

O script `src/langsmith_push.py` demonstra como subir seus prompts locais para a plataforma LangSmith, permitindo versionamento na nuvem e edição colaborativa.

```bash
python src/langsmith_push.py
```

## Benefícios desta Arquitetura

- **Desacoplamento**: O código Python não muda quando o texto do prompt muda.
- **Segurança**: Testes garantem que todos os placeholders (`{variavel}`) necessários estão presentes.
- **Histórico**: O Git mantém o histórico de evolução de cada prompt.
- **Rollback**: Voltar para uma versão anterior é tão simples quanto mudar uma linha no `registry.yaml`.
