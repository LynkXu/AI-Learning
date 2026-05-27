import os

from dotenv import load_dotenv
from openai import OpenAI


OPENAI_BASE_URL = "https://api.openai.com/v1"
CEREBRAS_BASE_URL = "https://api.cerebras.ai/v1"


def load_settings() -> dict[str, str]:
    load_dotenv()

    provider = os.getenv("LLM_PROVIDER", "openai").strip().lower()
    if provider not in {"openai", "cerebras"}:
        raise ValueError("LLM_PROVIDER must be either 'openai' or 'cerebras'.")

    model = os.getenv("MODEL_NAME", "").strip()
    if not model:
        raise ValueError("MODEL_NAME must be set in the environment.")

    if provider == "openai":
        api_key = os.getenv("OPENAI_API_KEY", "").strip()
        base_url = OPENAI_BASE_URL
    else:
        api_key = os.getenv("CEREBRAS_API_KEY", "").strip()
        base_url = CEREBRAS_BASE_URL

    if not api_key:
        raise ValueError(f"Missing API key for provider '{provider}'.")

    return {
        "provider": provider,
        "model": model,
        "api_key": api_key,
        "base_url": base_url,
    }


def create_client() -> tuple[OpenAI, dict[str, str]]:
    settings = load_settings()
    client = OpenAI(
        api_key=settings["api_key"],
        base_url=settings["base_url"],
    )
    return client, settings

