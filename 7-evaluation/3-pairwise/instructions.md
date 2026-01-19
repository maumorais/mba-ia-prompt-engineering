# Guia do Desenvolvedor: Módulo 3-pairwise

Este documento fornece uma análise técnica do diretório `3-pairwise`, que demonstra como validar a evolução de um prompt usando testes comparativos automatizados no LangSmith.

## 1. Semântica: O Problema que Ele Resolve

Quando você altera um prompt, como saber se ele ficou melhor?
Métricas absolutas (como "precisão 80%") são difíceis de definir para geração de texto.
Este módulo resolve isso usando **Preferência Relativa**: "O Prompt V2 é melhor que o Prompt V1?".

O cenário de demonstração é clássico:
- **V1**: Um especialista focado apenas em Segurança.
- **V2**: O mesmo especialista, agora treinado para cobrir também Performance.
- **Pergunta**: A versão V2 conseguiu aprender Performance sem piorar em Segurança? (Teste de Regressão + Evolução).

## 2. Padrões de Design Implementados

### Pairwise Comparison (Comparação Lado a Lado)
Em vez de avaliar cada prompt isoladamente, o script executa ambos para o mesmo input e pergunta a um LLM Juiz: "Compare a Resposta A e a Resposta B. Qual é mais completa e correta?".
- **Benefício**: Reduz a subjetividade. É mais fácil para um LLM (e humanos) dizer "A é melhor que B" do que dar uma nota absoluta "A vale 8.5".

### Prompt Versioning (Evolução)
O módulo mostra explicitamente o ciclo de vida de um prompt:
1.  **Criação (V1)**: `create_prompts.py` registra a versão inicial.
2.  **Execução (Baseline)**: `run.py` estabelece a performance base (50% de vitória, pois só cobre metade dos casos).
3.  **Atualização (V2)**: `update_prompt_v2.py` faz o "commit" de uma nova versão do prompt no LangSmith.
4.  **Re-execução (Melhoria)**: `run.py` (ou `run_v2.py` na lógica descrita) roda novamente e mostra o salto para 90% de vitória.

### Dataset Balanceado
O arquivo `dataset.jsonl` é cuidadosamente construído com 50% de casos de segurança e 50% de performance. Isso é crucial para evitar viés na avaliação. Se o dataset fosse 100% segurança, o prompt V1 já teria 100% de vitória e não veríamos a melhoria do V2.

## 3. Detalhes Técnicos

### O Juiz (Pairwise Judge)
O avaliador customizado (`pairwise_evaluator`) recebe duas listas de outputs. A lógica de pontuação é binária para o experimento:
- `[1, 0]`: A ganhou.
- `[0, 1]`: B ganhou.
- `[0.5, 0.5]`: Empate.

Isso gera um gráfico de "Win Rate" no LangSmith, que é a métrica executiva ideal para mostrar progresso.

## 4. Resumo

Desenvolvedores devem usar este padrão quando:
- Estiverem refatorando prompts complexos.
- Precisarem provar que uma mudança no prompt trouxe valor real.
- Quiserem monitorar "Drift" (se o modelo piorou com o tempo).

A grande lição aqui é: **Não confie na sua intuição. Coloque a V1 e a V2 para brigar e deixe um Juiz imparcial decidir.**
