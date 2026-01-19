# Instruções de Uso - Workflow de Agentes

Este diretório define uma arquitetura de múltiplos agentes baseada puramente em prompts (Markdown), sem código Python executável. Ele serve como um "Livro de Regras" ou "Sistema Operacional" para agentes de IA (como o próprio Claude/Gemini CLI) realizarem tarefas complexas de análise de engenharia.

## Visão Geral

O objetivo deste módulo é demonstrar como coordenar múltiplos "especialistas" (personas) para gerar um relatório completo de estado do projeto.

| Arquivo | Função | Descrição |
|---------|--------|-----------|
| `agents/orchestrator.md` | Gerente de Projeto | Mantém o `MANIFEST.md`, valida caminhos e garante que todos os componentes sejam analisados. |
| `agents/architectural-analyzer.md` | Arquiteto de Software | Analisa a estrutura de alto nível, stack tecnológico e padrões de design. |
| `agents/component-deep-analyzer.md` | Especialista em Código | Realiza "mergulho profundo" em arquivos específicos para extrair regras de negócio e dívida técnica. |
| `agents/dependency-auditor.md` | Auditor de Segurança | Verifica `package.json`, `requirements.txt`, etc., buscando vulnerabilidades e licenças. |
| `commands/run-project-state-full-report.md` | Workflow (Script) | O "código fonte" do processo em linguagem natural, definindo a ordem de execução e paralelismo. |

## Como Utilizar

Como este módulo não possui scripts Python (`.py`), a "execução" é feita simulando os agentes ou instruindo seu assistente de IA a assumir as personas definidas.

### Simulação Manual (Role-Playing)

1. **Carregar o Contexto**: Forneça o conteúdo de `agents/architectural-analyzer.md` para a IA.
2. **Executar a Tarefa**: Peça para ela analisar o diretório atual seguindo estritamente aquelas regras.
3. **Salvar o Resultado**: Salve a saída no caminho especificado (ex: `docs/agents/architectural-analyzer/...`).

### Automação via CLI (Conceitual)

Se você estiver usando uma ferramenta de CLI com suporte a ferramentas (como este Gemini CLI), você pode instruir o agente:

> "Atue como o `Architectural Analyzer` definido em `4-prompts-e-workflow-de-agentes/agents/architectural-analyzer.md` e gere um relatório sobre a pasta `7-evaluation`."

## Estrutura de Saída

Os agentes são programados para gerar artefatos na pasta `docs/agents/` (na raiz do projeto), seguindo esta hierarquia:

```text
docs/
└── agents/
    ├── orchestrator/
    │   └── MANIFEST.md              # Índice central de todos os relatórios
    ├── architectural-analyzer/
    │   └── report-YYYY-MM-DD.md     # Visão macro
    ├── component-deep-analyzer/
    │   ├── auth-module-report.md    # Análise específica A
    │   └── db-module-report.md      # Análise específica B
    └── dependency-auditor/
        └── security-audit.md        # Análise de libs
```

## Conceitos Chave

1. **Manifesto como Fonte da Verdade**: O Orchestrator não "adivinha" o estado; ele lê e escreve no `MANIFEST.md` para manter o controle do que já foi feito.
2. **Separação de Responsabilidades**: Cada agente tem um prompt negativo forte ("NEVER do X") para evitar alucinações ou desvio de função.
3. **Prompt-as-Code**: A lógica de controle, loops e condicionais está escrita em inglês dentro dos arquivos markdown, demonstrando que instruções naturais podem substituir scripts de orquestração tradicionais.
