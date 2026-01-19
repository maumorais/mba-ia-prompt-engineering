"""LLM and observability platform clients."""
import os
from langsmith.wrappers import wrap_openai
from langsmith import Client as LangSmithClient
from openai import OpenAI
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langfuse import Langfuse
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def get_llm_client(model: str = None, temperature: float = None):
    """
    Returns a configured LangChain Chat Model (OpenAI or Google).
    
    Priority:
    1. Google (if GOOGLE_API_KEY is present) -> gemini-2.5-flash-lite
    2. OpenAI (if OPENAI_API_KEY is present) -> gpt-4o-mini (default)
    
    Args:
        model: Override default model name
        temperature: Override default temperature (0)
        
    Returns:
        BaseChatModel: Configured LangChain chat model
    """
    if temperature is None:
        temperature = get_temperature()

    if os.getenv("GOOGLE_API_KEY"):
        # Default to Gemini if not specified
        model_name = model or "gemini-2.5-flash"
        print(f"Using Google Model: {model_name}")
        return ChatGoogleGenerativeAI(
            model=model_name,
            temperature=temperature,
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )
    
    elif os.getenv("OPENAI_API_KEY"):
        # Default to GPT-4o-mini if not specified
        model_name = model or get_model_name()
        print(f"Using OpenAI Model: {model_name}")
        return ChatOpenAI(
            model=model_name,
            temperature=temperature
        )
    
    else:
        raise ValueError("No API keys found. Please set GOOGLE_API_KEY or OPENAI_API_KEY in .env")


def get_embeddings_client():
    """
    Returns a configured LangChain Embeddings model (OpenAI or Google).
    
    Priority:
    1. Google (if GOOGLE_API_KEY is present) -> models/text-embedding-004
    2. OpenAI (if OPENAI_API_KEY is present) -> text-embedding-3-small
    
    Returns:
        Embeddings: Configured LangChain embeddings model
    """
    if os.getenv("GOOGLE_API_KEY"):
        print("Using Google Embeddings: models/text-embedding-004")
        return GoogleGenerativeAIEmbeddings(
            model="models/text-embedding-004",
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )
    
    elif os.getenv("OPENAI_API_KEY"):
        print("Using OpenAI Embeddings: text-embedding-3-small")
        return OpenAIEmbeddings(model="text-embedding-3-small")
    
    else:
        raise ValueError("No API keys found. Please set GOOGLE_API_KEY or OPENAI_API_KEY in .env")


def get_openai_client():
    """
    DEPRECATED: Use get_llm_client() instead.
    Maintains backward compatibility but returns a LangChain model now.
    """
    return get_llm_client()


def get_model_name() -> str:
    """
    Get configured model name from environment.

    Returns:
        Model name (default: gpt-4o-mini)
    """
    return os.getenv("LLM_MODEL", "gpt-4o-mini")


def get_temperature() -> float:
    """
    Get configured temperature from environment.

    Returns:
        Temperature value (default: 0)
    """
    return float(os.getenv("LLM_TEMPERATURE", "0"))


def get_langsmith_client():
    """
    Returns LangSmith client.

    Returns:
        LangSmith Client instance
    """
    return LangSmithClient()


def get_langfuse_client():
    """
    Returns Langfuse client.

    Returns:
        Langfuse client instance
    """
    return Langfuse()


def get_openai_client_langfuse():
    """
    Returns OpenAI client with Langfuse tracing.

    Model and temperature are configurable via environment variables:
    - LLM_MODEL (default: gpt-4o-mini)
    - LLM_TEMPERATURE (default: 0)

    Returns:
        OpenAI client wrapped with Langfuse tracing
    """
    from langfuse.openai import OpenAI as LangfuseOpenAI
    return LangfuseOpenAI()
