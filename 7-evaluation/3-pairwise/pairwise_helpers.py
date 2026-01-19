"""Helpers for pairwise evaluation."""


def create_pairwise_evaluator(judge_prompt_obj, client):
    """
    Create pairwise evaluator function for evaluate_comparative.

    Args:
        judge_prompt_obj: Judge prompt template (PromptTemplate)
        client: LangChain Chat Model (configured with temperature/model)

    Returns:
        Evaluator function with signature:
        (inputs: dict, outputs: list, reference_outputs: dict) -> list[float]

    The evaluator returns:
    - [1.0, 0.0] if A is better
    - [0.0, 1.0] if B is better
    - [0.5, 0.5] if tie

    Example:
        >>> from shared.prompts import load_yaml_prompt
        >>> from shared.clients import get_llm_client
        >>>
        >>> judge = load_yaml_prompt("pairwise_judge.yaml")
        >>> client = get_llm_client()
        >>> evaluator = create_pairwise_evaluator(judge, client)
        >>>
        >>> # Use in evaluate_comparative
        >>> results = evaluate_comparative(
        ...     [exp_a, exp_b],
        ...     evaluators=[evaluator]
        ... )
    """
    from langchain_core.messages import HumanMessage

    def evaluate_pairwise(inputs: dict, outputs: list, reference_outputs: dict = None):
        """Pairwise comparison evaluator."""
        code = inputs.get("code", "")
        answer_a = outputs[0].get("output", "")
        answer_b = outputs[1].get("output", "")

        # Format judge prompt
        judge_prompt = judge_prompt_obj.format(
            code=code,
            answer_a=answer_a,
            answer_b=answer_b
        )

        # Get judge decision using LangChain invoke
        # client is already configured with model and temperature
        response = client.invoke([HumanMessage(content=judge_prompt)])
        decision = response.content.strip().upper()

        # Parse decision
        if "A" in decision and "B" not in decision:
            return [1.0, 0.0]  # A wins
        elif "B" in decision and "A" not in decision:
            return [0.0, 1.0]  # B wins
        else:
            return [0.5, 0.5]  # Tie

    return evaluate_pairwise