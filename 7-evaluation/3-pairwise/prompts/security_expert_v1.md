# Prompt Especialista em Segurança (v1)

## Descrição
Este prompt configura o modelo como um **Especialista em Segurança de Aplicações** focado em identificar vulnerabilidades críticas em código Go. É a primeira versão do especialista de segurança usado nos testes.

## Estrutura do Prompt
O prompt define:
1.  **Persona**: Especialista em segurança focado em vulnerabilidades críticas.
2.  **Foco da Análise**:
    *   SQL Injection.
    *   XSS (Cross-site scripting).
    *   Command Injection.
    *   Validação de input ausente.
    *   Problemas de Autenticação/Autorização.
    *   Credenciais hardcoded.
    *   Gerenciamento de sessão.
3.  **Formato de Saída**: JSON estrito (RAW JSON), contendo lista de `findings` e `summary`.

## Variáveis de Entrada
*   `language`: A linguagem de programação.
*   `code`: O código fonte a ser analisado.

## Uso
Gera a "Resposta A" (focada em segurança) nos experimentos de comparação. Serve como baseline para avaliar a detecção de vulnerabilidades comuns contra outros tipos de revisão (performance ou generalista).
