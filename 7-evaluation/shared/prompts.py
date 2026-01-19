"""Utilities for loading and executing prompts."""
from langchain.prompts import load_prompt
from pathlib import Path
from typing import Optional


def load_yaml_prompt(filename: str, prompts_dir: Optional[Path] = None):
    """
    Load YAML prompt from file.

    Args:
        filename: Prompt filename (e.g., "format_eval.yaml")
        prompts_dir: Directory containing prompts (default: ./prompts from caller)

    Returns:
        Loaded prompt object (PromptTemplate or ChatPromptTemplate)

    Example:
        >>> prompt = load_yaml_prompt("format_eval.yaml")
        >>> # Auto-detects prompts/ directory in caller's location
    """
    if prompts_dir is None:
        import inspect
        caller_file = Path(inspect.stack()[1].filename)
        prompts_dir = caller_file.parent / "prompts"

    return load_prompt(prompts_dir / filename)


def execute_text_prompt(prompt_obj, inputs: dict, llm,
                        input_key: str = "code", model: str = None,
                        temperature: float = None):
    """
    Execute simple text prompt (PromptTemplate) using LangChain.

    Args:
        prompt_obj: Loaded prompt object
        inputs: Input dictionary from dataset
        llm: LangChain Chat Model (OpenAI or Google)
        input_key: Key to extract from inputs (default: "code")
        model: Ignored (handled by llm object)
        temperature: Optional temperature override
    """
    # Configure LLM with specific temperature if requested
    configured_llm = llm
    if temperature is not None:
        configured_llm = llm.bind(temperature=temperature)
    
    chain = prompt_obj | configured_llm
    response = chain.invoke(inputs)

    return {"output": response.content}


def convert_langchain_to_openai_messages(messages):
    """
    Convert LangChain messages to OpenAI format.

    Args:
        messages: List of LangChain message objects

    Returns:
        List of dicts in OpenAI format: [{"role": "user", "content": "..."}]

    Example:
        >>> lc_messages = prompt.format_messages(code="...")
        >>> openai_msgs = convert_langchain_to_openai_messages(lc_messages)
    """
    openai_messages = []
    for m in messages:
        role = "user" if m.type == "human" else m.type
        openai_messages.append({"role": role, "content": m.content})
    return openai_messages


def execute_chat_prompt(prompt_obj, inputs: dict, llm,
                       model: str = None, temperature: float = None,
                       **format_kwargs):
    """
    Execute chat prompt (ChatPromptTemplate) using LangChain.

    Args:
        prompt_obj: ChatPromptTemplate object
        inputs: Input dictionary from dataset
        llm: LangChain Chat Model
        model: Ignored
        temperature: Ignored
        **format_kwargs: Arguments for format_messages()

    Returns:
        {"output": str} - Model response
    """
    messages = prompt_obj.format_messages(**format_kwargs)
    
    response = llm.invoke(messages)

    return {"output": response.content}
