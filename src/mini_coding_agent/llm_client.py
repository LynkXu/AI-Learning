import os

from dotenv import load_dotenv
from openai import OpenAI

# To add a new provider, just add an entry here.
PROVIDERS: dict[str, dict[str, str]] = {
    "openai": {
        "base_url": "https://api.openai.com/v1",
        "api_key_env": "OPENAI_API_KEY",
    },
    "cerebras": {
        "base_url": "https://api.cerebras.ai/v1",
        "api_key_env": "CEREBRAS_API_KEY",
    },
    "openrouter": {
        "base_url": "https://openrouter.ai/api/v1",
        "api_key_env": "OPENROUTER_API_KEY",
    },
}


def load_settings() -> dict[str, str]:
    load_dotenv()

    provider = os.getenv("LLM_PROVIDER", "openai").strip().lower()
    if provider not in PROVIDERS:
        raise ValueError(f"LLM_PROVIDER must be one of: {', '.join(PROVIDERS)}.")

    model = os.getenv("MODEL_NAME", "").strip()
    if not model:
        raise ValueError("MODEL_NAME must be set in the environment.")

    cfg = PROVIDERS[provider]
    api_key = os.getenv(cfg["api_key_env"], "").strip()
    if not api_key:
        raise ValueError(
            f"Missing API key for provider '{provider}': set {cfg['api_key_env']}."
        )

    return {
        "provider": provider,
        "model": model,
        "api_key": api_key,
        "base_url": cfg["base_url"],
    }


def create_client() -> tuple[OpenAI, dict[str, str]]:
    settings = load_settings()
    client = OpenAI(
        api_key=settings["api_key"],
        base_url=settings["base_url"],
    )
    return client, settings
