"""Langfuse-specific helper functions."""
import json
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage


def run_with_chat_prompt(prompt_obj, inputs, client):
    """
    Execute a chat prompt with Langfuse prompt object.

    Args:
        prompt_obj: Langfuse prompt object
        inputs: Input dictionary
        client: LangChain chat client

    Returns:
        String response from model
    """
    # Compile prompt (Langfuse SDK handles message formatting)
    compiled_prompt = prompt_obj.compile(**inputs)
    
    # Convert list of dicts to LangChain messages
    messages = []
    for msg in compiled_prompt:
        role = msg.get('role')
        content = msg.get('content')
        if role == 'system':
            messages.append(SystemMessage(content=content))
        elif role == 'user':
            messages.append(HumanMessage(content=content))
        elif role == 'assistant':
            messages.append(AIMessage(content=content))
        else:
            # Fallback for other roles
            messages.append(HumanMessage(content=content))

    # Execute using LangChain client
    response = client.invoke(messages)

    return response.content


def run_with_text_prompt(prompt_obj, client, **kwargs):
    """
    Execute a text prompt with Langfuse prompt object.

    Args:
        prompt_obj: Langfuse text prompt object
        client: LangChain chat client
        **kwargs: Variables to compile into prompt

    Returns:
        String response from model
    """
    # Compile text prompt with variables
    compiled_prompt = prompt_obj.compile(**kwargs)

    # Execute using LangChain client
    response = client.invoke([HumanMessage(content=compiled_prompt)])

    return response.content


def parse_judge_response(response_text: str):
    """
    Parse JSON response from judge, handling markdown blocks.

    Args:
        response_text: Raw judge response

    Returns:
        Tuple of (decision, reasoning)
        decision: "A", "B", or "TIE"
        reasoning: Dictionary of reasoning details
    """
    from shared.parsers import parse_json_response

    result = parse_json_response(response_text)

    if result:
        return result.get("decision", "TIE"), result.get("reasoning", {})
    else:
        return "TIE", {"error": "Failed to parse JSON"}


def format_reasoning_summary(reasoning: dict) -> str:
    """
    Format reasoning dictionary into readable string.

    Args:
        reasoning: Reasoning dictionary from judge

    Returns:
        Formatted multi-line string
    """
    lines = []

    # Total scores
    if "score_total_a" in reasoning and "score_total_b" in reasoning:
        lines.append(
            f"Total Scores - A: {reasoning['score_total_a']}/50, "
            f"B: {reasoning['score_total_b']}/50"
        )

    # Final decision
    if "final_decision" in reasoning:
        lines.append(f"\nDecision: {reasoning['final_decision']}")

    # Detailed breakdown of each dimension
    dimensions = [
        ("structural_completeness", "Structural Completeness"),
        ("technical_precision", "Technical Precision"),
        ("clarity_and_utility", "Clarity and Utility"),
        ("reference_alignment", "Reference Alignment"),
        ("conciseness_vs_detail", "Conciseness vs Detail")
    ]

    for key, label in dimensions:
        if key in reasoning:
            dim = reasoning[key]
            score_a = dim.get("score_a", "?")
            score_b = dim.get("score_b", "?")
            justification = dim.get("justification", "")

            lines.append(f"\n{label}: A={score_a}/10, B={score_b}/10")
            if justification:
                lines.append(f"  -> {justification}")

    return "\n".join(lines) if lines else "No reasoning provided"