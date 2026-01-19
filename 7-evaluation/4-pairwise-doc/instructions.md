# Guia do Desenvolvedor: Módulo 4-pairwise-doc

Este documento fornece uma análise técnica do diretório `4-pairwise-doc`, que apresenta uma estratégia de avaliação híbrida combinando **Pairwise Evaluation** com **Métricas Individuais** granulares.

## 1. Semântica: O Problema que Ele Resolve

Pairwise Evaluation tradicional (Módulo 3) responde "Quem ganhou?". Mas para tarefas complexas como **Geração de Documentação**, isso é insuficiente. Precisamos saber *por que* ganhou.
- O Prompt A foi melhor porque foi mais conciso?
- Ou o Prompt B ganhou porque foi mais completo, mesmo sendo verboso?

Este módulo implementa um sistema de "Scorecard Detalhado" onde o Juiz não apenas escolhe um vencedor, mas dá notas (0-10) em 5 dimensões diferentes.

## 2. Arquitetura Híbrida

O fluxo de execução em `run.py` é mais rico que o padrão:

1.  **Avaliação Individual (Unitária)**:
    - O Prompt A é rodado e avaliado isoladamente em 6 métricas: `conciseness`, `coherence`, `detail`, `helpfulness`, `faithfulness`, `completeness`.
    - O Prompt B passa pelo mesmo processo.
    - **Resultado**: Temos um perfil de qualidade independente para cada prompt.

2.  **Avaliação Comparativa (Pairwise)**:
    - O Juiz recebe (Output A, Output B, Gabarito).
    - Em vez de apenas dizer "A venceu", ele preenche um JSON com notas para:
        1.  Completude Estrutural
        2.  Precisão Técnica
        3.  Clareza e Utilidade
        4.  Alinhamento com Referência (Ground Truth)
        5.  Concisão vs Detalhe

## 3. Conceitos Chave

### Ground Truth como "Padrão Ouro"
Diferente do Módulo 3, aqui usamos um `reference` (documentação ideal) no dataset. O Juiz usa isso para pontuar o critério "Alinhamento com Referência". Isso é vital para empresas que têm guias de estilo estritos.

### LLM-as-a-Judge Estruturado
O prompt do juiz (`prompts/llm_judge_pairwise.yaml`) é desenhado para retornar um JSON complexo, não texto livre. Isso permite:
- **Análise Quantitativa**: "O Prompt B é 20% mais alinhado com a referência".
- **Análise Qualitativa**: "O Prompt A perde pontos por alucinar funcionalidades".

## 4. Resumo

Desenvolvedores devem adotar este padrão para **Tarefas de Geração de Texto Longo** (docs, blogs, emails).
- Se a tarefa é classificação (bug/no-bug), use Precision/Recall (Módulo 2).
- Se a tarefa é preferência simples, use Pairwise Simples (Módulo 3).
- Se a tarefa exige nuances de estilo e estrutura, use este módulo (**Pairwise com Scorecard**).
