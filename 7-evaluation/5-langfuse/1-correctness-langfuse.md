# 1-correctness-langfuse.py

Exemplo de avaliação de **corretude** utilizando o Langfuse para registrar scores (pontuações) associados a traces específicos.

## Funcionalidades Principais

1.  **Carregamento de Prompt e Dados**: Lê um prompt YAML e um dataset (`go-ds`) do Langfuse.
2.  **Execução Avaliada**: Para cada item do dataset, executa a chain de análise de código Go.
3.  **Cálculo de Score**: Compara os problemas encontrados pelo modelo (`predicted_findings`) com o gabarito (`expected_findings`) usando uma função de similaridade de conjuntos.
4.  **Registro de Scores**: Utiliza `langfuse.create_score` para anexar a métrica calculada ("Code findings") diretamente ao trace da execução no Langfuse.

## Diferencial

Mostra como vincular métricas de qualidade (scores numéricos) a execuções individuais, permitindo monitoramento de performance ao longo do tempo.

## Uso

```bash
python 1-correctness-langfuse.py
```