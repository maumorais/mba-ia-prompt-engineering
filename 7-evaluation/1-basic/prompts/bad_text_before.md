# Prompt "Bad Text Before" (Falsamente Otimista)

## Descrição
Este prompt é **intencionalmente defeituoso**. Ele configura o modelo como um "revisor otimista" que ignora deliberadamente quaisquer falhas ou vulnerabilidades no código.

*Nota: Embora o nome do arquivo seja `bad_text_before.yaml`, o conteúdo deste prompt foca em gerar falsos negativos (ignorar erros), e não necessariamente em gerar texto antes do JSON. O nome pode se referir a uma versão anterior ou a um teste específico de formato que evoluiu.*

## Estrutura do Prompt
O prompt instrui o modelo a:
1.  **Ignorar Problemas**: "Ignore issues and vulnerabilities".
2.  **Focar no Positivo**: Dizer apenas que o código é bem escrito.
3.  **Ser Superficial**: Retornar findings vazios ou genéricos.

## Variáveis de Entrada
*   `code`: O código a ser analisado.

## Uso
Este prompt gera um **Falso Negativo**. É usado para testar se as métricas de avaliação conseguem detectar que o modelo falhou em encontrar bugs óbvios que estavam presentes no código (Recall ruim).
