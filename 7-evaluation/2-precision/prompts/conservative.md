# Prompt Conservador (High Precision)

## Descrição
Este prompt configura o modelo como um **Especialista em Segurança** extremamente cauteloso. Seu objetivo é garantir **alta precisão**, reportando apenas problemas sobre os quais tem certeza absoluta, minimizando ao máximo os falsos positivos.

## Estrutura do Prompt
O prompt impõe restrições severas:
1.  **Certeza Absoluta**: Reportar APENAS se tiver **100% de certeza**.
2.  **Escopo Reduzido**: Foca EXCLUSIVAMENTE em vulnerabilidades críticas (SQL Injection, XSS, Command Injection), ignorando problemas de qualidade ou performance.
3.  **Preferência pelo Silêncio**: Instrui explicitamente que é melhor não reportar nada do que gerar um falso positivo.

## Variáveis de Entrada
*   `code`: O código fonte Go a ser analisado.

## Uso
Este prompt é ideal para:
*   **Pipelines de Bloqueio**: Onde um alerta interrompe o deploy. Nesses casos, falsos positivos são inaceitáveis.
*   **Cenários de Alta Confiança**: Quando o usuário tem pouca tolerância a ruído e só quer ser incomodado por problemas graves e óbvios.
*   **Experimentos de Precisão**: Para estabelecer a capacidade do modelo de ser preciso e confiável.

## Trade-off
Espera-se uma taxa mais alta de **Falsos Negativos** (bugs reais que não são reportados porque o modelo não tinha 100% de certeza ou porque não eram críticos).
