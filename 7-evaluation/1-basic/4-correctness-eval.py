"""
Correctness evaluation: Comparing predictions against reference outputs.

Demonstrates labeled evaluators that use reference outputs for comparison.
"""
#Incluindo a pasta superior no caminho do python, para permitir a importação de Shared
import sys
import os
# Adiciona o diretório pai (7-evaluation) ao caminho de busca do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from langsmith import evaluate
from langsmith.evaluation import LangChainStringEvaluator
from pathlib import Path

from shared.clients import get_llm_client
from shared.prompts import load_yaml_prompt, execute_text_prompt
from shared.evaluators import prepare_with_reference

# Configuration
DATASET_NAME = "evaluation_basic_dataset"
BASE_DIR = Path(__file__).parent

# Setup
llm_client = get_llm_client()

prompt = load_yaml_prompt("correctness_eval.yaml")


def run_correctness_evaluation(inputs: dict) -> dict:
    """Target function for evaluate()."""
    return execute_text_prompt(prompt, inputs, llm_client, input_key="code")


# Labeled evaluators with reference outputs
evaluators = [
    LangChainStringEvaluator(
        "labeled_score_string",
        config={"criteria": "correctness", "normalize_by": 10, "llm": llm_client},
        prepare_data=prepare_with_reference
    ),
    LangChainStringEvaluator(
        "labeled_score_string",
        config={"criteria": "relevance", "normalize_by": 10, "llm": llm_client},
        prepare_data=prepare_with_reference
    )
]

# Run evaluation
results = evaluate(
    run_correctness_evaluation,
    data=DATASET_NAME,
    evaluators=evaluators,
    experiment_prefix="CorrectnessEval",
    max_concurrency=2
)

print("="*80)
print(f"EXPERIMENT: {results.experiment_name}")
print("="*80)
