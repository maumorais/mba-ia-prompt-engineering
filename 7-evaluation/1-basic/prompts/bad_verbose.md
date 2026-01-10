# Prompt "Bad Verbose" (Verbosidade Excessiva)

## Descrição
Este prompt é **intencionalmente defeituoso** (do ponto de vista de eficiência e formatação estrita). Ele configura o modelo como um "professor de programação filosófico" que escreve longos textos antes e depois da análise real.

## Estrutura do Prompt
O prompt exige uma quantidade massiva de texto irrelevante:
1.  **Introdução Longa**: 3 parágrafos sobre engenharia de software, história da linguagem, filosofia, etc.
2.  **Conclusão Longa**: Reflexões sobre IA, ética, agradecimentos.
3.  **Análise no Meio**: A análise do código fica "escondida" no meio de todo esse texto.

## Variáveis de Entrada
*   `code`: O código a ser analisado.

## Uso
Este prompt testa:
1.  **Concisão**: O avaliador deve penalizar a resposta por ser extremamente verbosa.
2.  **Parsing de Formato**: Se o sistema espera JSON estrito, este prompt provavelmente quebrará o parser (a menos que o parser seja robusto o suficiente para extrair JSON de markdown misturado).
3.  **Custo/Latência**: Demonstra o impacto de prompts mal projetados no consumo de tokens.
