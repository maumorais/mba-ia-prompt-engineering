# Prompt Especialista em Code Review (Segurança + Performance) - v2

## Descrição
Esta é uma versão mais abrangente ("v2") do prompt de especialista. Diferente da v1 que foca apenas em segurança, este prompt configura o modelo como um **Especialista em Code Review Completo**, cobrindo *tanto* segurança *quanto* performance.

## Estrutura do Prompt
O prompt é mais detalhado e instrui o modelo a:
1.  **Análise Completa e Técnica**: Identificar vulnerabilidades de segurança E problemas de performance no mesmo passo.
2.  **Instruções Específicas**:
    *   Citar linhas exatas e contexto.
    *   Ser acionável (explicar como corrigir).
    *   Ser completo (não omitir problemas menores).
3.  **Formato de Saída Expandido**: JSON estrito que inclui:
    *   `findings`: Com campos adicionais como `suggestion` (sugestão de correção).
    *   `summary`: Resumo técnico.
    *   `stats`: Estatísticas contendo contagem total e por severidade (critical, high, medium, low).
4.  **Restrição de Alucinação**: Instrução explícita para identificar apenas problemas REAIS.

## Variáveis de Entrada
*   `language`: A linguagem de programação.
*   `code`: O código fonte a ser analisado.

## Uso
Este prompt representa uma evolução ou uma alternativa "híbrida" no experimento. Ele testa se um único prompt abrangente é mais eficaz (ou preferido pelo juiz) do que prompts especializados isolados, ou se ele consegue manter a qualidade em ambas as frentes sem alucinar.
