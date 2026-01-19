# Architectural Analysis Report

## 1. Executive Summary

The **mba-ia-prompt-engineering** project is a comprehensive educational repository designed to demonstrate advanced concepts in Prompt Engineering, LLMOps, and Agentic Workflows. It is structured as a **modular monorepo**, where each top-level directory represents a distinct learning module or functional prototype.

The system evolves from basic prompting techniques (Module 1) to complex agent orchestration (Module 4), prompt management infrastructure (Module 5), RAG enhancement strategies (Module 6), and a robust evaluation framework (Module 7). The technology stack is heavily centered on **Python** and the **LangChain ecosystem**, integrating with observability platforms like **LangSmith** and **Langfuse**.

A key architectural finding is the separation of concerns between "Code-based Agents" (Python scripts using LangChain) and "Prompt-based Agents" (Markdown specifications for CLI-driven workflows), demonstrating two distinct paradigms of AI automation.

## 2. System Overview

The project follows a topic-based directory structure:

```
project-root/
├── 1-tipos-de-prompts/                         # [Module] Basic to Advanced Prompting
│   ├── 0-Role-prompting.py                     # Baseline techniques
│   └── 9-Round-table.md                        # Multi-persona simulation
├── 4-prompts-e-workflow-de-agentes/            # [Module] Markdown-based Agent Architecture
│   ├── agents/                                 # Agent definitions (System Prompts)
│   └── commands/                               # Workflow orchestrators
├── 5-gerenciamento-e-versionamento-de-prompts/ # [Module] PromptOps CLI Tool
│   ├── src/                                    # CLI implementation
│   └── prompts/                                # YAML-based prompt registry
├── 6-prompt-enriquecido/                       # [Module] Advanced RAG Patterns
│   ├── 1-ITER_RETGEN.py                        # Iterative Retrieval-Generation
│   └── 2-query-enrichment.py                   # Query expansion logic
├── 7-evaluation/                               # [Module] LLM Evaluation Framework
│   ├── 1-basic/                                # Simple assertion evals
│   ├── 3-pairwise/                             # A/B testing logic
│   ├── 5-langfuse/                             # Langfuse integration
│   └── shared/                                 # Shared utilities (clients, parsers)
└── docs/                                       # Project documentation & Agent outputs
```

## 3. Critical Components Analysis

| Component | Type | Location | Afferent Coupling | Efferent Coupling | Architectural Role |
|-----------|------|----------|-------------------|-------------------|-------------------|
| **Shared Evaluator Lib** | Library | `7-evaluation/shared/` | High (Modules 7.1-7.5) | Low | Core logic for evaluation metrics and clients |
| **Prompt Registry CLI** | Application | `5-gerenciamento.../src/` | Low | High (LangSmith, YAML) | Automation for prompt versioning and PR creation |
| **Agent Manifest** | Specification | `4-prompts.../agents/` | Low | None | Definition of agent behaviors (Markdown-as-Code) |
| **Langfuse Integration** | Adapter | `7-evaluation/5-langfuse/` | Low | High (Langfuse SDK) | Bridge for observability and pairwise evaluation |
| **RAG Iterators** | Script | `6-prompt-enriquecido/` | Low | Medium (LangChain) | Implementation of complex RAG loops (ITER-RETGEN) |

## 4. Dependency Mapping

```
High-Level Dependencies:

[Evaluation Scripts] --> [Shared Lib (7-evaluation/shared)] --> [LLM Clients (OpenAI/Google)]
                                                            --> [LangSmith SDK]

[Prompt CLI] --> [LangSmith Client]
             --> [GitHub API (simulated/implied)]
             --> [YAML Registry]

[Langfuse Module] --> [Langfuse SDK]
                  --> [Shared Lib]
```

## 5. Integration Points

| Integration | Type | Location | Purpose | Risk Level |
|-------------|------|----------|---------|------------|
| **OpenAI API** | External API | `shared/clients.py` | Main LLM inference provider | High (Cost/Rate Limits) |
| **Google Gemini API** | External API | `shared/clients.py` | Alternative/Fallback LLM provider | Medium |
| **LangSmith** | Platform | `5-gerenciamento.../langsmith_client.py` | Observability & Prompt Registry | Medium |
| **Langfuse** | Platform | `7-evaluation/5-langfuse/` | Evaluation datasets & scoring | Medium |

## 6. Architectural Risks & Single Points of Failure

| Risk Level | Component | Issue | Impact | Details |
|------------|-----------|--------|--------|---------|
| **High** | **API Keys (.env)** | Configuration Management | System-wide | Reliance on local `.env` files makes deployment/sharing fragile without a secrets manager. |
| **Medium** | **Shared Code Duplication** | DRY Violation | Maintainability | Some utility logic might be duplicated between Module 5 and Module 7 (e.g., client initialization). |
| **Low** | **Hardcoded Models** | Flexibility | Future-proofing | Scripts often hardcode "gpt-4o-mini", requiring manual updates for model migration. |

## 7. Technology Stack Assessment

*   **Language**: Python 3.10+
*   **Orchestration**: LangChain (Core, Community, OpenAI), LangGraph (in Module 5)
*   **Observability**: LangSmith, Langfuse
*   **Testing**: Pytest (Module 5 & 7)
*   **Data Serialization**: YAML (Prompts), JSONL (Datasets)
*   **CLI**: Rich (for pretty printing in Module 5)

## 8. Security Architecture and Risks

*   **Secrets Management**: API keys are handled via `python-dotenv`. Ensure `.env` is strictly `gitignored` (confirmed in file structure).
*   **Input Injection**: Prompt injection risks are inherent in the RAG modules (Module 6), though this is an educational repo, in production sanitization would be required.
*   **Dependency Supply Chain**: Multiple `requirements.txt` files increase the surface area for vulnerable packages. A unified dependency lockfile is missing.

## 9. Infrastructure Analysis

*   **Local Execution**: The project is designed primarily for local execution via virtual environments (`venv`).
*   **Docker**: Alluded to in `7-evaluation/5-langfuse/README.md` for running Langfuse locally, but no root `docker-compose.yml` orchestrates the entire repo.