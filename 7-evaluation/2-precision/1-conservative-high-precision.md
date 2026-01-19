# 1-conservative-high-precision.py: Alta Precisão (Conservative)

Este script demonstra uma estratégia de avaliação focada em **Alta Precisão**. O objetivo é garantir que, quando o modelo aponta um erro, esse erro realmente existe (minimizar Falsos Positivos), mesmo que para isso ele deixe passar alguns erros reais (sacrificar Recall).

## O que este script faz?

Ele executa uma avaliação em dataset (`evaluation_precision_dataset`) utilizando um prompt "conservador" (`prompts/conservative.yaml`). Este prompt instrui o modelo a apontar apenas erros óbvios e críticos, ignorando suspeitas ou "code smells" menores.

## Conceitos Chave

1.  **Precisão (Precision)**: De tudo que o modelo marcou como erro, quanto realmente era erro?
    *   *Alta Precisão* = O modelo "não chuta". Só fala quando tem certeza.
2.  **Falsos Positivos**: O modelo dizer que há um bug onde não há. Esta estratégia visa reduzir isso a zero.
3.  **Conservative Strategy**: Útil em sistemas de CI/CD bloqueantes (o build falha se houver erro). Você não quer bloquear o deploy por um alarme falso.

## Análise do Código

### 1. Prompt Conservador
```python
prompt = load_yaml_prompt("conservative.yaml")
```
O arquivo YAML associado instrui explicitamente o modelo a ser cético e só reportar vulnerabilidades com evidência concreta.

### 2. Avaliador de Resumo (Summary Evaluator)
Diferente da avaliação linha-a-linha, aqui usamos um `summary_evaluator` que olha para o resultado agregado de todo o dataset para calcular métricas globais (Precision, Recall, F1).

```python
def bug_detection_summary(outputs: list, examples: list) -> list:
    # ...
    return calculate_precision_recall_f1(...)
```
Este avaliador compara o conjunto de tuplas `(tipo, severidade)` preditas pelo modelo contra o gabarito (ground truth).

### 3. Extração Comparável
Para ser justo, a comparação ignora descrições textuais e números de linha (que podem variar), focando apenas na categorização do problema:
```python
# metrics.py (usado pelo script)
finding_tuple = (
    f.get("type", ""),
    f.get("severity", "").lower()
)
```

## Por que usar?

Use esta estratégia quando o **custo do Falso Positivo for alto**.
*   **Exemplo**: Um bot que abre Pull Requests automáticos de correção. Se o bot abrir PRs errados, os desenvolvedores vão perder a confiança e desligá-lo. Melhor ele abrir menos PRs, mas todos serem corretos.
