"""
Bad prompt test: Hallucinated issues.

Tests a prompt that invents issues not present in the code.
Expected: LOW scores in faithfulness.
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
from shared.evaluators import prepare_with_input

# Configuration
DATASET_NAME = "evaluation_basic_dataset"
BASE_DIR = Path(__file__).parent

# Setup
llm_client = get_llm_client()


def run_bad_hallucination(inputs: dict) -> dict:
    """Runs the bad_hallucination prompt"""
    prompt = load_yaml_prompt("bad_hallucination.yaml")
    # Note: Using higher temperature for this bad example
    return execute_text_prompt(prompt, inputs, llm_client, input_key="code", temperature=1.2)


# Evaluators focused on detecting hallucination
evaluators = [
    # Detects hallucination (bad_hallucination should have low score)
    LangChainStringEvaluator(
        "score_string",
        config={
            "criteria": {
                "faithfulness": "Is the response grounded ONLY in the provided code? Doesn't invent problems or context that doesn't exist in the code?"
            },
            "normalize_by": 10
        },
        prepare_data=prepare_with_input,
        llm=llm_client
    ),

    # Additional metrics for context
    LangChainStringEvaluator(
        "score_string",
        config={"criteria": "helpfulness", "normalize_by": 10},
        prepare_data=prepare_with_input,
        llm=llm_client
    ),

    LangChainStringEvaluator(
        "score_string",
        config={"criteria": "coherence", "normalize_by": 10},
        prepare_data=prepare_with_input,
        llm=llm_client
    ),

    LangChainStringEvaluator(
        "score_string",
        config={"criteria": "detail", "normalize_by": 10},
        prepare_data=prepare_with_input,
        llm=llm_client
    ),
]

print("="*80)
print("TEST: BAD_HALLUCINATION")
print("="*80)
print("\nExpected: LOW score in faithfulness (< 0.4)")
print("Prompt: Expert who invents fictional problems")
print("="*80)
print()

# Run evaluation
results = evaluate(
    run_bad_hallucination,
    data=DATASET_NAME,
    evaluators=evaluators,
    experiment_prefix="BadHallucination_Test",
    max_concurrency=2
)

print("="*80)
print(f"EXPERIMENT: {results.experiment_name}")
print("="*80)
