# reset.py: Limpeza de Ambiente

Este é um script utilitário administrativo projetado para gerenciar o ciclo de vida dos seus dados de teste no LangSmith.

## O que este script faz?

Ele se conecta à API do LangSmith e **deleta permanentemente** o dataset chamado `evaluation_basic_dataset`.

## Conceitos Chave

1.  **Imutabilidade vs. Iteração**: Em data science, datasets tendem a ser imutáveis. Mas durante o *desenvolvimento* dos testes (quando você ainda está decidindo quais exemplos colocar no dataset), é comum querer "começar do zero" para evitar que versões antigas de exemplos se misturem com as novas.
2.  **Limpeza**: Remove o dataset pelo ID, garantindo que o nome `evaluation_basic_dataset` fique livre para ser recriado.

## Análise do Código

```python
dataset = client.read_dataset(dataset_name=DATASET_NAME)
client.delete_dataset(dataset_id=dataset.id)
```
O código tenta encontrar o dataset pelo nome. Se encontrar, pega o ID único dele e manda o comando de deleção. Se não encontrar (bloco `except`), avisa que já estava limpo.

## Por que usar?

Use com cautela. É útil quando você modificou drasticamente a estrutura do seu arquivo `dataset.jsonl` (ex: mudou os nomes das colunas de `input`/`output` para `pergunta`/`resposta`) e quer garantir que o LangSmith não tente mesclar esquemas incompatíveis.