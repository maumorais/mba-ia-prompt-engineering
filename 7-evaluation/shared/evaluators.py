"""Helper functions for creating prepare_data functions."""


def prepare_prediction_only(run, example):
    """
    Prepare data with only prediction (for evaluators that don't need input/reference).

    Use for:
    - json_validity
    - json_schema

    Args:
        run: LangSmith run object
        example: Dataset example

    Returns:
        {"prediction": str}
    """
    return {"prediction": run.outputs.get("output", "")}


def prepare_with_input(run, example, input_key="code"):
    """
    Prepare data with prediction + input (for evaluators without reference).

    Use for:
    - criteria (binary)
    - score_string (continuous)
    - Custom criteria

    Args:
        run: LangSmith run object
        example: Dataset example
        input_key: Key to extract from inputs (default: "code")

    Returns:
        {"prediction": str, "input": str}
    """
    return {
        "prediction": run.outputs.get("output", ""),
        "input": example.inputs.get(input_key, "")
    }


def prepare_with_reference(run, example, input_key="code"):
    """
    Prepare data with prediction + input + reference (for labeled evaluators).

    Use for:
    - labeled_criteria
    - labeled_score_string

    Args:
        run: LangSmith run object
        example: Dataset example
        input_key: Key to extract from inputs (default: "code")

    Returns:
        {"prediction": str, "input": str, "reference": dict}
    """
    return {
        "prediction": run.outputs.get("output", ""),
        "input": example.inputs.get(input_key, ""),
        "reference": example.outputs
    }


def prepare_for_embedding_distance(run, example):
    """
    Prepare data specifically for embedding distance evaluation.
    Extracts the 'summary' from reference outputs to compare text-to-text.

    Use for:
    - embedding_distance

    Args:
        run: LangSmith run object
        example: Dataset example

    Returns:
        {"prediction": str, "reference": str}
    """
    # Extract just the summary string from the complex output object
    # If summary doesn't exist, dump the whole object to string
    reference_data = example.outputs
    if isinstance(reference_data, dict) and "summary" in reference_data:
        reference_text = reference_data["summary"]
    else:
        import json
        reference_text = json.dumps(reference_data)
        
    return {
        "prediction": run.outputs.get("output", ""),
        "reference": reference_text
    }
