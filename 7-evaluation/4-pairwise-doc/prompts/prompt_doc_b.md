# Prompt de Geração de Documentação B (Alto Nível)

## Descrição
Este prompt define um perfil de **Engenheiro de IA** focado em escrever documentação para desenvolvedores, mas com uma abordagem distinta: prioriza a visão geral e a explicação funcional, evitando explicitamente detalhes técnicos profundos.

## Estrutura do Prompt
O prompt instrui o modelo a:
1.  **Explicar o Propósito**: Focar no que o projeto faz.
2.  **Ser Factual e Conciso**: Manter o texto direto.
3.  **Evitar Detalhes Técnicos Específicos**: Explicitamente instrui a **NÃO** incluir:
    *   Exemplos de código.
    *   Detalhes de implementação.
    *   Detalhes de frameworks.
4.  **Formato**: Markdown útil para desenvolvedores (mas em nível mais alto).

## Variáveis de Entrada
*   `files`: O conteúdo dos arquivos do projeto a serem documentados.

## Uso
Este prompt representa a estratégia de geração **"B"** no experimento de comparação pairwise. Ele serve como um contraponto ao `prompt_doc_a`. Enquanto o "A" busca profundidade técnica, o "B" testa se uma documentação mais **limpa, conceitual e menos verbosa** é avaliada como superior ou inferior pelo juiz, dependendo dos critérios de qualidade definidos (como clareza e concisão).
