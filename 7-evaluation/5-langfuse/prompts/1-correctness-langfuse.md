# Prompt Avaliação de Corretude (Integração LangFuse)

## Descrição
Este prompt configura um **Analisador de Qualidade e Segurança para Go**. Ele é semelhante aos prompts de avaliação vistos em outras pastas, mas formatado especificamente para uso em fluxos integrados com o LangFuse.

## Estrutura do Prompt
1.  **Persona**: Analisador de segurança e qualidade Go.
2.  **Escopo**: Identificar vulnerabilidades, erros, problemas de performance e qualidade.
3.  **Formato de Saída**: JSON estrito contendo lista de `findings` com `type` e `severity`.
4.  **Lista de Referência**: Fornece uma lista explícita de tipos de issues (`issue_types`) e níveis de severidade para padronização.

## Variáveis de Entrada
*   `code`: O código Go a ser analisado.

## Uso
Utilizado no script `1-correctness-langfuse.py`. Este prompt serve para gerar as análises que serão posteriormente avaliadas quanto à sua corretude (correctness) dentro da plataforma LangFuse. Ele age como o "sistema sob teste" cujas saídas serão julgadas.
