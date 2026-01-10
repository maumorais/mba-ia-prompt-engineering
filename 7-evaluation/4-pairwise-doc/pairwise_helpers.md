# pairwise_helpers.py

Este módulo fornece a lógica para o "Juiz Pairwise" (LLM-as-Judge), capaz de comparar duas gerações de documentação e fornecer um veredicto detalhado e estruturado.

## Funcionalidades Principais

*   **`create_pairwise_judge(judge_prompt_obj, client)`**:
    *   Cria uma função avaliadora que compara `answer_a` vs `answer_b` utilizando uma `reference` (Ground Truth).
    *   Processa a resposta do LLM que retorna um JSON contendo:
        *   Scores individuais para 5 dimensões (Completude, Precisão, Clareza, Alinhamento, Concisão).
        *   Justificativas textuais para cada nota.
        *   Decisão final ("A", "B" ou Empate).
    *   Converte o JSON em um formato compatível com o sistema de avaliação do LangSmith (`ranked_preference`).

*   **`format_reasoning_as_text(decision, reasoning)`**:
    *   Transforma o objeto de raciocínio JSON em um relatório textual legível por humanos.
    *   Exibe o breakdown de pontuação por categoria e a justificativa final, facilitando a análise no dashboard do LangSmith.

## Diferencial

Diferente de avaliadores simples que retornam apenas "A venceu", este helper extrai e formata o *porquê* da decisão, permitindo insights profundos sobre os trade-offs entre os prompts.

## Uso

Importado pelo `run.py` para configurar a comparação direta entre os resultados dos experimentos.
