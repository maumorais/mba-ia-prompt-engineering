# Architectural Analysis Report

**Generated on:** 2026-01-19-14-51-00
**Project:** mba-ia-prompt-engineering

## 1. Executive Summary

The `mba-ia-prompt-engineering` repository is an educational and practical monorepo designed to demonstrate advanced Prompt Engineering techniques, LLMOps, and Agentic Workflows. The architecture is modular, segregated by learning topics, ranging from basic scripts to complex evaluation frameworks and agent specifications.

**Key Findings:**
*   **Polyglot Architecture (Python + Markdown):** The project uses Python for execution logic and Markdown for agent behavior definition.
*   **Modular Design:** Distinct modules (`1-tipos...`, `5-gerenciamento...`, `7-evaluation`) operate almost independently, sharing only external dependencies or utility modules within their scope.
*   **Observability First:** Strong architectural emphasis on observability using LangSmith and Langfuse, abstracted via a shared layer.
*   **Agentic Evolution:** Demonstrates a clear evolution from simple scripts to complex, multi-agent systems defined by prompts.

## 2. System Overview

The project is structured as a collection of independent modules, each representing a specific domain of prompt engineering.

```
project-root/
├── 1-tipos-de-prompts/                        # Scripts: Basic prompting techniques (Zero-shot, CoT, etc.)
├── 4-prompts-e-workflow-de-agentes/           # Specs: Markdown-based Multi-Agent System definitions
├── 5-gerenciamento-e-versionamento-de-prompts/# Application: CLI for Prompt Registry & Code Review
│   └── src/                                   # Core logic for the review agent
├── 6-prompt-enriquecido/                      # Scripts: RAG and Query Expansion techniques
├── 7-evaluation/                              # Framework: Comprehensive LLM Evaluation System
│   ├── shared/                                # Library: Common utilities (clients, datasets, evaluators)
│   ├── 5-langfuse/                            # Module: Langfuse integration examples
│   └── ...                                    # Other evaluation strategies (basic, pairwise)
└── docs/                                      # Documentation and Agent Outputs
```

**Architectural Patterns:**
*   **Script-based Execution:** Used in folders 1 and 6 for direct demonstration.
*   **Service-Oriented (CLI):** Folder 5 implements a Registry pattern and Service layer for code review.
*   **Shared Library / Framework:** Folder 7 implements a robust evaluation framework with a central `shared` module used by satellite scripts.
*   **Prompt-as-Code (PaC):** Folder 4 treats Markdown prompts as executable specifications.

## 3. Critical Components Analysis

| Component | Type | Location | Afferent Coupling | Efferent Coupling | Architectural Role |
|-----------|------|----------|-------------------|-------------------|-------------------|
| Shared Lib (`7-eval`) | Library | `7-evaluation/shared` | High (Used by all eval scripts) | Low (External libs only) | Central utility for evaluation logic & clients |
| LangSmith Client | Adapter | `5-gerenciamento.../src/langsmith_client.py` | Medium | Low | Abstraction for observability platform |
| Prompt Registry | Service | `5-gerenciamento.../src/prompt_registry.py` | Medium | Low | Manages prompt versions and retrieval |
| Agent Orchestrator | Spec | `4-prompts.../agents/orchestrator.md` | High (Conceptually) | High | Coordinates the multi-agent workflow |
| Reviewer Agent | Application | `5-gerenciamento.../src/agent_code_reviewer.py` | Low | High (Uses registry, clients) | Main business logic for code review |

**Coupling Definitions:**
*   **Afferent Coupling (Ca):** The number of other components that depend on this component. High Ca indicates stability and responsibility.
*   **Efferent Coupling (Ce):** The number of other components that this component depends on. High Ce indicates instability and sensitivity to change.

## 4. Dependency Mapping

```
High-Level Dependencies:

[7-evaluation Framework]
Eval Scripts (1-basic, 5-langfuse, etc.)
    │
    ▼
7-evaluation/shared (Clients, Evaluators, Datasets)
    │
    ▼
External APIs (OpenAI, Google, LangSmith, Langfuse)

[5-gerenciamento App]
Agent Code Reviewer
    │
    ├──> Prompt Registry (YAML)
    ├──> LangSmith Client
    └──> OpenAI Client
```

## 5. Integration Points

| Integration | Type | Location | Purpose | Risk Level |
|-------------|------|----------|---------|------------|
| OpenAI API | External API | `shared/clients.py` | LLM Inference | High (Cost/Availability) |
| Google Gemini API | External API | `shared/clients.py` | LLM Inference (Alternative) | Medium |
| LangSmith | SaaS Platform | `shared/clients.py` | Tracing & Evaluation | Medium |
| Langfuse | SaaS Platform | `5-langfuse` | Tracing & Prompt Management | Medium |
| Local File System | I/O | Throughout | Datasets, Journals, Reports | Low |

## 6. Architectural Risks & Single Points of Failure

| Risk Level | Component | Issue | Impact | Details |
|------------|-----------|--------|--------|---------|
| High | API Keys (`.env`) | Configuration | System-wide | Missing keys break all scripts. No fallback logic for offline mode. |
| Medium | `7-evaluation/shared` | Coupling | Framework Stability | Changes in `shared` interfaces break all evaluation scripts. |
| Low | Agent Specs (`4-prompts`) | Execution Environment | Usability | Requires specific CLI agent (Claude Code or similar) to interpret correctly. |

## 7. Technology Stack Assessment

*   **Languages:** Python 3.10+, Markdown.
*   **LLM Frameworks:** LangChain (Core), LangSmith (Obs), Langfuse (Obs/Mgmt).
*   **APIs:** OpenAI (GPT-4o), Google (Gemini 1.5/2.5).
*   **Testing:** Pytest (in folder 5).
*   **Format:** JSONL (Datasets), YAML (Prompts).

## 8. Security Architecture and Risks

*   **Secrets Management:** Relies entirely on `.env` files. Ensure these are strictly `.gitignore`d (verified in root `.gitignore`).
*   **Input Handling:** Evaluation scripts process arbitrary code inputs from `dataset.jsonl`. Potential for Prompt Injection if running against untrusted models/inputs.
*   **Agent Autonomy:** The agents in folder 4 are designed to write files. Strict path validation ("must use absolute paths", "never write outside folder") is specified in Markdown but relies on the executor's enforcement.

## 9. Infrastructure Analysis

*   **Local Execution:** Primarily designed for local CLI execution.
*   **Docker:** Mentioned in `5-langfuse/README.md` for running Langfuse server locally.
*   **Virtual Environments:** Multiple `venv` directories indicate isolated environments per module, a good practice for dependency management in monorepos.

