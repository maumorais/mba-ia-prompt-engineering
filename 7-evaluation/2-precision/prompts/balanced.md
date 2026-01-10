# Prompt Balanceado (Best F1)

## Descrição
Este prompt configura o modelo como um **Revisor de Código Especialista** com uma abordagem sistemática e equilibrada. Ele busca otimizar a pontuação F1 (média harmônica entre precisão e recall), encontrando a maioria dos bugs reais enquanto mantém os falsos positivos sob controle.

## Estrutura do Prompt
O prompt utiliza técnicas avançadas de engenharia de prompt:
1.  **Camadas de Prioridade**: Divide a análise em 3 camadas:
    *   Camada 1: Segurança (Crítico/Alto)
    *   Camada 2: Robustez & Performance (Alto/Médio)
    *   Camada 3: Qualidade de Código (Médio/Baixo)
2.  **Regra de Confiança**: Exige explicitamente **80%+ de confiança** antes de reportar um problema.
3.  **Checklist Sistemático**: Fornece uma ordem lógica de análise para o modelo seguir.
4.  **Exemplos Claros**: Fornece exemplos de código para os problemas mais complexos (como SQL Injection e Ignored Errors) para alinhar o entendimento do modelo.

## Variáveis de Entrada
*   `code`: O código fonte Go a ser analisado.

## Uso
Este prompt é o "ponto ideal" para a maioria dos cenários de CI/CD e assistência ao desenvolvedor, pois fornece feedback valioso sem sobrecarregar o usuário com ruído excessivo.
