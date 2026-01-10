# Prompt de Geração de Documentação A (Detalhado)

## Descrição
Este prompt define um perfil de **Especialista em Documentação de Software** focado em sistemas Python e IA. Seu objetivo é gerar uma documentação técnica abrangente e bem estruturada para um conjunto de arquivos de projeto fornecidos.

## Estrutura do Prompt
O prompt instrui o modelo a:
1.  **Analisar Múltiplos Arquivos**: Recebe um dicionário ou lista de arquivos do projeto.
2.  **Gerar Documentação Completa**: Exige seções específicas:
    *   Visão geral de alto nível.
    *   Descrição dos módulos e relacionamentos.
    *   Fluxo de dados.
    *   Resumo de funções importantes (inputs, outputs, comportamento).
    *   Detalhes de implementação notáveis (frameworks, padrões).
3.  **Formato**: Markdown com títulos claros.

## Variáveis de Entrada
*   `files`: O conteúdo dos arquivos do projeto a serem documentados (geralmente um dicionário `nome_arquivo: conteudo`).

## Uso
Este prompt representa a estratégia de geração **"A"** no experimento de comparação pairwise. Ele é projetado para produzir uma documentação **rica em detalhes técnicos**, ideal para desenvolvedores que precisam entender a fundo o funcionamento interno do sistema. No contexto da avaliação, ele compete contra o `prompt_doc_b` para verificar qual estilo de documentação (mais detalhado ou mais conciso) é preferido pelo juiz ou se alinha melhor à referência.
