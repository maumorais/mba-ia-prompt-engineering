# Instruções de Uso - Tipos de Prompts

Este diretório contém uma coleção progressiva de exemplos demonstrando técnicas fundamentais e avançadas de Engenharia de Prompt.

## Visão Geral

Os scripts estão numerados sequencialmente para facilitar o aprendizado, partindo de conceitos básicos até arquiteturas cognitivas complexas.

| Script | Técnica | Descrição |
|--------|---------|-----------|
| `0-Role-prompting.py` | Role Prompting | Atribuição de persona ao modelo (ex: "Você é um especialista..."). Fundamental para definir tom e estilo. |
| `1-zero-shot.py` | Zero-shot | Prompt direto sem exemplos. O modelo confia inteiramente em seu pré-treinamento. |
| `2-one-few-shot.py` | Few-shot Learning | Fornecimento de 1 ou mais exemplos (input/output) no prompt para guiar o formato e a lógica da resposta. |
| `3-CoT.py` | Chain of Thought (CoT) | Solicita que o modelo "pense passo a passo", melhorando drasticamente a performance em raciocínio lógico e matemático. |
| `3.1-CoT-Self-consistency.py` | CoT Self-Consistency | Gera múltiplos caminhos de raciocínio (CoT) e seleciona a resposta mais frequente (votação majoritária) para aumentar a confiabilidade. |
| `4-ToT.py` | Tree of Thoughts (ToT) | Mantém múltiplos "galhos" de raciocínio simultâneos, permitindo exploração e retrocesso (backtracking) para problemas complexos. |
| `5-SoT.py` | Skeleton of Thought | Gera primeiro um esqueleto/outline da resposta e depois preenche os detalhes, otimizando latência e estrutura. |
| `6-ReAct.py` | ReAct | Intercala **Re**asoning (Raciocínio) e **Act**ion (Ação), permitindo uso de ferramentas externas. |
| `7-Prompt-channing.py` | Prompt Chaining | Quebra uma tarefa complexa em uma sequência linear de prompts menores, onde a saída de um é a entrada do próximo. |
| `8-Least-to-most.py` | Least-to-Most | Decompõe um problema complexo em subproblemas mais simples, resolvendo-os sequencialmente usando as respostas anteriores. |

## Configuração do Ambiente

1. **Variáveis de Ambiente**:
   Certifique-se de que o arquivo `.env` existe na raiz do diretório `1-tipos-de-prompts` com sua chave da OpenAI:
   ```env
   OPENAI_API_KEY=sk-...
   ```
   *Nota: Use `.env.example` como base.*

2. **Instalação de Dependências**:
   ```bash
   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Como Executar

Cada script é independente e pode ser executado diretamente. Recomenda-se seguir a ordem numérica para compreender a evolução das técnicas.

Exemplo:
```bash
python 3-CoT.py
```

## Detalhes Técnicos

- **Utils (`utils.py`)**: Contém funções auxiliares para formatação de saída no terminal (usando a biblioteca `rich`), garantindo que as respostas do modelo sejam apresentadas de forma legível.
- **Modelos**: Os scripts são configurados por padrão para usar modelos da OpenAI (ex: `gpt-4o-mini` ou `gpt-3.5-turbo`), mas podem ser adaptados para outros providers compatíveis com LangChain.

## Exercícios Sugeridos

1. **Comparação Zero vs Few-shot**: Execute `1-zero-shot.py` e `2-one-few-shot.py` com a mesma pergunta complexa e observe a diferença na formatação da resposta.
2. **Depuração de Raciocínio**: No script `3-CoT.py`, tente remover a instrução "Let's think step by step" e veja se o modelo erra problemas de lógica.
3. **Criação de Agentes**: Estude o `6-ReAct.py` como base para construir agentes que realmente executam ações (como buscar na web ou consultar banco de dados).
