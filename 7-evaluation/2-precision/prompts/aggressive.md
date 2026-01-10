# Prompt Agressivo (High Recall)

## Descrição
Este prompt configura o modelo como um **Especialista em Segurança** com uma mentalidade de "tolerância zero" para riscos. Seu objetivo é identificar **todas** as possíveis falhas, priorizando o recall (encontrar o máximo de bugs) em detrimento da precisão (aceitando mais falsos positivos).

## Estrutura do Prompt
O prompt instrui explicitamente o modelo a:
1.  **Reportar TUDO**: Incluir até mesmo possibilidades remotas.
2.  **Ser Rigoroso**: Suspeitar de tudo; melhor reportar em excesso do que perder um bug.
3.  **Escopo Amplo**: Procura por uma vasta lista de tipos de problemas, desde injeção de SQL até má nomeação de variáveis e loops verbosos.

## Variáveis de Entrada
*   `code`: O código fonte Go a ser analisado.

## Uso
Este prompt é ideal para:
*   **Auditorias de Segurança Críticas**: Onde perder uma vulnerabilidade é inaceitável.
*   **Triagem Inicial**: Para gerar uma lista ampla de candidatos a bugs que serão filtrados posteriormente por humanos ou outros sistemas.
*   **Experimentos de Recall**: Para estabelecer o limite superior de detecção do modelo.

## Trade-off
Espera-se uma taxa mais alta de **Falsos Positivos** (alertas que não são bugs reais), exigindo maior esforço de revisão humana subsequente.
