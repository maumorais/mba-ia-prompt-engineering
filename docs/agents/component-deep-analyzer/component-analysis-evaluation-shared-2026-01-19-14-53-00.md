# Component Deep Analysis Report: Evaluation Shared Lib

## 1. Executive Summary

The **Evaluation Shared Lib** (`7-evaluation/shared/`) acts as the foundational utility layer for the entire evaluation framework (Module 7). Its primary responsibility is to provide unified, provider-agnostic access to LLM services (OpenAI vs Google), consistent observability instrumentation (LangSmith, Langfuse), and standardized data processing utilities for evaluation metrics.

Key finding: The component implements a strict **provider priority logic** (Google > OpenAI), allowing cost optimization or vendor fallback without changing consuming code. It also centralizes the complexity of cleaning "dirty" JSON often returned by LLMs.

## 2. Data Flow Analysis

Typical flow for an evaluation run using this lib:

```
1. Script calls get_llm_client() (clients.py)
   └── Logic checks env vars: if GOOGLE_API_KEY ? GoogleGemini : OpenAI
2. Script executes LLM chain
3. Raw text response is passed to parse_json_response() (parsers.py)
   └── Strips markdown "```json" wrappers
   └── Returns clean Dict
4. Evaluation loop calls prepare_*() functions (evaluators.py)
   └── Extracts 'prediction' from Run object
   └── Extracts 'reference' from Dataset Example
   └── Formats payload for the Judge/Metric
```

## 3. Business Rules & Logic

## Overview of the business rules:

| Rule Type | Rule Description | Location |
|-----------|------------------|----------|
| **Provider Priority** | Prefer Google Gemini over OpenAI if key is present | `clients.py:get_llm_client` |
| **Parsing Robustness** | Aggressively strip Markdown formatting from JSON | `parsers.py:parse_json_response` |
| **Embedding Consistency** | Enforce string typing for Embedding inputs | `evaluators.py:prepare_for_embedding_distance` |

## Detailed breakdown:

### Business Rule: Provider Priority Strategy

**Overview**:
The system is designed to be agnostic but opinionated about costs/providers.

**Detailed description**:
The factory functions `get_llm_client` and `get_embeddings_client` do not just instantiate a client; they check the environment. If `GOOGLE_API_KEY` is detected, the system forces the use of `ChatGoogleGenerativeAI` (`gemini-2.5-flash`). Only if that key is missing does it fall back to `ChatOpenAI` (`gpt-4o-mini`). This allows developers to switch underlying engines globally by simply toggling environment variables.

### Business Rule: JSON Markdown Cleaning

**Overview**:
LLMs frequently disobey "return raw JSON" instructions and wrap output in markdown code blocks.

**Detailed description**:
The `parse_json_response` function implements a heuristic scanner. It searches for the first `{` or `[` and the last `}` or `]`, ignoring everything outside these bounds (like "Here is your JSON:" prefixes or "```" suffixes). This ensures that evaluation pipelines don't crash due to formatting noise.

## 4. Component Structure

```
7-evaluation/shared/
├── clients.py          # Factory patterns for LLMs & Observability
├── evaluators.py       # Data transformers for LangSmith evaluators
├── parsers.py          # Text processing & JSON sanitization
└── prompts.py          # (Empty/Placeholder in analyzed version)
```

## 5. Dependency Analysis

**Internal Dependencies**:
- None (Modules are largely independent utility buckets)

**External Dependencies**:
- `langchain-openai`, `langchain-google-genai`: For model wrappers.
- `langsmith`, `langfuse`: For observability client instantiation.
- `python-dotenv`: For loading configuration.
- `openai`: Direct client usage (legacy support).

## 6. Afferent and Efferent Coupling

| Component | Afferent Coupling | Efferent Coupling | Critical |
|-----------|-------------------|-------------------|-------------------|
| `clients.py` | High (Used by all scripts in 7-evaluation) | High (LangChain, OpenAI, Google SDKs) | **Critical** |
| `parsers.py` | Medium (Used by structured output tests) | Low (json stdlib) | Low |
| `evaluators.py` | Medium (Used by run.py scripts) | Low (LangSmith objects) | Medium |

## 7. Integration Points

| Integration | Type | Purpose | Protocol | Data Format |
|-------------|------|---------|----------|-------------|
| **Google Gemini API** | External Service | Inference & Embeddings | HTTPS/REST | JSON |
| **OpenAI API** | External Service | Inference & Embeddings | HTTPS/REST | JSON |
| **LangSmith API** | Observability | Tracing & Evaluation | HTTPS | JSON |

## 9. Design Patterns & Architecture

| Pattern | Implementation | Location | Purpose |
|---------|----------------|----------|---------|
| **Factory Method** | `get_llm_client` | `clients.py` | Decouple client creation from implementation (OpenAI vs Google) |
| **Adapter** | `prepare_with_reference` | `evaluators.py` | Adapt internal Run/Example objects to Evaluator interface |
| **Strategy** | `parse_json_response` | `parsers.py` | Robust parsing strategy handling multiple format variations |

## 10. Technical Debt & Risks

| Risk Level | Component Area | Issue | Impact |
|------------|----------------|-------|--------|
| **Medium** | `clients.py` | Hardcoded Model Names | Changing `gpt-4o-mini` requires code edits; should be env var fully. |
| **Low** | `evaluators.py` | Type Safety | `prepare_for_embedding_distance` has aggressive `try/except` blocks for JSON dumping, masking potential serialization errors. |

## 11. Test Coverage Analysis

| Component | Unit Tests | Integration Tests | Coverage | Test Quality |
|-----------|------------|-------------------|----------|--------------|
| `parsers.py` | `tests/test_parsers.py` | N/A | High | Covers standard JSON, Markdown-wrapped, and invalid inputs. |
| `clients.py` | `tests/test_clients.py` | N/A | High | Mocks environment variables to verify priority logic without real API calls. |