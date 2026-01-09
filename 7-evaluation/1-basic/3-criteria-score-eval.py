"""
Continuous criteria evaluation: Score-based evaluation using LLM judges.

Demonstrates continuous evaluators (0.0-1.0) for nuanced quality assessment.
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
from shared.evaluators import prepare_with_input, prepare_with_reference

# Configuration
DATASET_NAME = "evaluation_basic_dataset"
BASE_DIR = Path(__file__).parent

# Setup
llm_client = get_llm_client()

prompt = load_yaml_prompt("criteria_eval.yaml")


def run_score_evaluation(inputs: dict) -> dict:
    """Target function for evaluate()."""
    return execute_text_prompt(prompt, inputs, llm_client, input_key="code")


# CONTINUOUS EVALUATORS: score_string (0.0-1.0)
#
# Difference from example 2:
# - Example 2 uses criteria (binary 0/1)
# - Example 3 uses score_string (continuous 0.0-1.0)
#
# Criteria chosen for CODE REVIEW:
# - conciseness: Also in ex.2 (shows difference binary vs continuous)
# - coherence: Analysis should be coherent and well-structured
# - detail: Code review needs technical details (lines, issue types)
# - depth: Analysis should go beyond obvious, identify non-trivial issues
# - relevance: Should be relevant to analyzed code (with reference)

evaluators = [
    # WITHOUT reference - evaluates subjective quality

    # Conciseness: Also used in ex.2 to show difference binary (0/1) vs continuous (0.0-1.0)
    LangChainStringEvaluator(
        "score_string",
        config={"criteria": "conciseness", "normalize_by": 10},
        prepare_data=prepare_with_input,
        llm=llm_client
    ),

    # Coherence: Is analysis coherent and well-structured?
    LangChainStringEvaluator(
        "score_string",
        config={"criteria": "coherence", "normalize_by": 10},
        prepare_data=prepare_with_input,
        llm=llm_client
    ),

    # Detail: Does analysis detail line, issue type, severity?
    LangChainStringEvaluator(
        "score_string",
        config={"criteria": "detail", "normalize_by": 10},
        prepare_data=prepare_with_input,
        llm=llm_client
    ),

    # Depth: Does analysis go beyond obvious? Identifies non-trivial issues?
    LangChainStringEvaluator(
        "score_string",
        config={"criteria": "depth", "normalize_by": 10},
        prepare_data=prepare_with_input,
        llm=llm_client
    ),

    # WITH reference - compares with expected output

    # Relevance: Is analysis relevant to provided code?
    LangChainStringEvaluator(
        "labeled_score_string",
        config={"criteria": "relevance", "normalize_by": 10},
        prepare_data=prepare_with_reference,
        llm=llm_client
    ),
]

# Run evaluation
results = evaluate(
    run_score_evaluation,
    data=DATASET_NAME,
    evaluators=evaluators,
    experiment_prefix="CriteriaScoreEval",
    max_concurrency=1
)

print("="*80)
print(f"EXPERIMENT: {results.experiment_name}")
print("="*80)
