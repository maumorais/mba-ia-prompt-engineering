# Guia do Desenvolvedor: Módulo 2-precision

Este documento fornece uma análise técnica do diretório `2-precision`, que adapta métricas de classificação clássica (Precision, Recall, F1) para o contexto de LLMs.

## 1. Semântica: O Problema que Ele Resolve

Avaliar LLMs não é apenas sobre "texto bonito". Em tarefas de classificação ou detecção (ex: encontrar bugs em código), precisamos saber se o modelo está:
1.  **Alucinando erros** (Falso Positivo -> Baixa Precisão)
2.  **Deixando passar erros reais** (Falso Negativo -> Baixo Recall)

Este módulo demonstra como ajustar o *Prompt* para mover o modelo ao longo da curva de Precision-Recall.

## 2. Conceitos Chave

### Trade-off Precision vs Recall
- **Script**: `1-conservative-high-precision.py`
  - **Estratégia**: Prompt instrui o modelo a reportar *apenas* se tiver certeza absoluta.
  - **Resultado**: Alta Precisão (poucos alarmes falsos), mas Baixo Recall (perde alguns bugs sutis). Ideal para *Blockers de CI/CD*.

- **Script**: `2-aggressive-high-recall.py`
  - **Estratégia**: Prompt instrui o modelo a ser "paranoico" e reportar qualquer suspeita.
  - **Resultado**: Alto Recall (acha quase tudo), mas Baixa Precisão (muito ruído). Ideal para *Auditoria de Segurança*.

- **Script**: `3-balanced-best-f1.py`
  - **Estratégia**: Prompt equilibrado.
  - **Resultado**: Melhor F1-Score (média harmônica). Ideal para uso geral.

## 3. Implementação Técnica

### Custom Summary Evaluators
O LangSmith não tem avaliadores nativos de Precision/Recall para texto livre. Este módulo implementa **Summary Evaluators Customizados** em `metrics.py`.

A lógica é:
1.  O Dataset contém uma lista de `expected_issue_types` (Gabarito).
2.  O Modelo gera uma lista de `found_issue_types` (Predição).
3.  O avaliador calcula a interseção de conjuntos:
    - `TP` = Interseção (Achou e Era Real)
    - `FP` = Achou - Real (Alucinação)
    - `FN` = Real - Achou (Perdeu)

### Arquitetura de Prompt
Os arquivos YAML em `prompts/` demonstram como palavras-chave alteram o comportamento estatístico do modelo:
- `conservative.yaml`: Usa termos como "ONLY report", "CERTAINTY", "CRITICAL".
- `aggressive.yaml`: Usa termos como "POTENTIAL issues", "SUSPICION", "ALL findings".

## 4. Resumo

Desenvolvedores devem usar este módulo para aprender a **calibrar** seus LLMs.
- Se o usuário reclama de "barulho" (muitos avisos inúteis), adote a estratégia **Conservative**.
- Se o usuário reclama que o modelo "não ajuda" ou "deixa passar coisas", adote a estratégia **Aggressive**.
- Use o **F1-Score** como métrica única para comparar versões de prompts durante o desenvolvimento.
