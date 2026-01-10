# create_prompts.py

Este script é responsável por inicializar e registrar os prompts base no LangSmith para o experimento de comparação pairwise (par a par).

## Funcionalidades Principais

1.  **Carregamento de YAML**: Lê arquivos de configuração de prompt em formato YAML (`prompts/security_expert_v1.yaml` e `prompts/performance_expert.yaml`) e os converte em templates de chat compatíveis com LangChain.
2.  **Registro no LangSmith**: Envia (push) os prompts para o registro do LangSmith com identificadores específicos:
    *   `pairwise_comparison_security`: Versão inicial do especialista em segurança.
    *   `pairwise_comparison_performance`: Especialista em performance.

## Uso

Execute este script antes de rodar os experimentos para garantir que os prompts estejam disponíveis no registro.

```bash
python create_prompts.py
```
