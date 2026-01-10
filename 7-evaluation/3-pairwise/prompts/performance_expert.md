# Prompt Especialista em Performance

## Descrição
Este prompt configura o modelo como um **Especialista em Otimização de Performance** para aplicações Go. Seu objetivo é identificar gargalos, ineficiências e problemas de uso de recursos.

## Estrutura do Prompt
O prompt define:
1.  **Persona**: Especialista em Go focado em eficiência.
2.  **Foco da Análise**:
    *   Problemas de query N+1.
    *   Vazamentos de memória (Memory leaks).
    *   Operações bloqueantes e falta de concorrência.
    *   Timeouts ausentes.
    *   Bloqueios ineficientes (Locking).
    *   Processamento sequencial que poderia ser paralelo.
3.  **Formato de Saída**: JSON estrito (RAW JSON), contendo uma lista de `findings` (com tipo, linha, descrição e severidade) e um `summary`.

## Variáveis de Entrada
*   `language`: A linguagem de programação do código (geralmente "Go" neste contexto).
*   `code`: O código fonte a ser analisado.

## Uso
Este prompt é usado para gerar a "Resposta B" (ou uma das variantes) no experimento de comparação. Ele isola a capacidade do modelo de detectar falhas de desempenho, permitindo avaliar se um prompt especializado em performance é mais valioso do que um focado em segurança ou um generalista para determinados tipos de código.
