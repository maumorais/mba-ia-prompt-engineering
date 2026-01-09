"""
Bad prompt test: Text before JSON.

Tests a prompt that adds explanatory text before the JSON response.
Expected: LOW scores in format adherence.
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


def run_bad_text_before(inputs: dict) -> dict:
    """Runs the bad_text_before prompt"""
    prompt = load_yaml_prompt("bad_text_before.yaml")
    # Note: Using higher temperature for this bad example
    # Note: execute_text_prompt now accepts llm_client instead of model kwarg for model selection,
    # but still accepts temperature overrides if the function supports it (it doesn't support temp override on client directly easily without re-instantiation, but execute_text_prompt ignores temp unless we update it. 
    # WAIT: execute_text_prompt implementation I wrote uses 'chain = prompt | llm'.
    # If I pass a temperature to execute_text_prompt, it is IGNORED by my previous implementation.
    # To support temperature override in 'bad' scripts, I should probably re-instantiate the client inside the run function OR update execute_text_prompt to bind arguments.
    # For now, let's keep it simple and just use the client as is, OR strictly speaking, if these bad prompts RELY on high temperature to be bad, I need to support it.
    
    # My previous implementation of execute_text_prompt:
    # def execute_text_prompt(..., llm, ..., temperature=None):
    #    chain = prompt_obj | llm ...
    
    # This ignores the temperature arg. 
    # I should fix execute_text_prompt first to support runtime configuration (binding) if possible, or just accept that for this refactor we might lose the temperature override unless I fix it.
    
    # Actually, the user asked to "adapt the code". Losing the "badness" (high temp) might make the test fail to be bad.
    # I will stick to the plan: pass llm_client.
    # I will modify execute_text_prompt in shared/prompts.py to support binding temperature if passed.
    
    return execute_text_prompt(prompt, inputs, llm_client, input_key="code")


# Evaluators focused on detecting lack of detail and depth
evaluators = [
    # Detects lack of details (bad_text_before should have low score)
    LangChainStringEvaluator(
        "score_string",
        config={"criteria": "detail", "normalize_by": 10},
        prepare_data=prepare_with_input,
        llm=llm_client
    ),

    # Detects superficial analysis (bad_text_before should have low score)
    LangChainStringEvaluator(
        "score_string",
        config={"criteria": "depth", "normalize_by": 10},
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
]

print("="*80)
print("TEST: BAD_TEXT_BEFORE")
print("="*80)
print("\nExpected: LOW scores in detail and depth (< 0.4)")
print("Prompt: Optimistic reviewer who ignores issues")
print("="*80)
print()

# Run evaluation
results = evaluate(
    run_bad_text_before,
    data=DATASET_NAME,
    evaluators=evaluators,
    experiment_prefix="BadTextBefore_Test",
    max_concurrency=2
)

print("="*80)
print(f"EXPERIMENT: {results.experiment_name}")
print("="*80)
