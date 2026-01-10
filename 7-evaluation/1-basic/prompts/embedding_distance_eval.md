# Prompt Avaliação por Distância de Embedding

## Descrição
Este prompt configura um **Revisor de Código Go** altamente detalhado e estruturado. Ele é projetado para produzir respostas consistentes e ricas em terminologia técnica específica.

## Estrutura do Prompt
Diferente dos prompts minimalistas, este fornece instruções detalhadas:
1.  **Foco Específico**: Segurança, performance e qualidade.
2.  **Instruções de Saída**: Pede explicitamente para identificar o tipo (ex: `sql_injection`), linha, descrição técnica e severidade.
3.  **Lista de Tipos Aceitos**: Fornece exemplos de issue types (`missing_timeout`, `n_plus_1_query`, etc.) para padronizar o vocabulário.

## Variáveis de Entrada
*   `code`: O código Go a ser analisado.

## Uso
Utilizado no script `6-embedding-distance-eval.py`. A ideia é gerar uma resposta "padrão ouro" (ou próxima disso) e usar **Embeddings** (vetores semânticos) para medir a distância cosseno entre a resposta gerada por este prompt e uma resposta de referência ideal. Isso permite avaliar a qualidade sem necessariamente usar outro LLM como juiz, baseando-se na similaridade semântica.
