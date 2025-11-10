import os
from dataclasses import dataclass
from functools import lru_cache
from typing import TYPE_CHECKING, Literal, cast, get_args

from kosong.chat_provider import ChatProvider
from pydantic import SecretStr

if TYPE_CHECKING:
    from kimi_cli.config import LLMModel, LLMProvider

type ProviderType = Literal["openai", "anthropic"]

type ModelCapability = Literal["image_in", "thinking"]
ALL_MODEL_CAPABILITIES: set[ModelCapability] = set(get_args(ModelCapability))


@dataclass(slots=True)
class LLM:
    chat_provider: ChatProvider
    max_context_size: int
    capabilities: set[ModelCapability]
    use_cache: bool = False

    @property
    def model_name(self) -> str:
        return self.chat_provider.model_name

    @lru_cache(maxsize=128)
    def _cached_chat(self, *args, **kwargs):
        return self.chat_provider.chat(*args, **kwargs)

    def chat(self, *args, **kwargs):
        if self.use_cache:
            return self._cached_chat(*args, **kwargs)
        return self.chat_provider.chat(*args, **kwargs)


def augment_provider_with_env_vars(provider: "LLMProvider", model: "LLMModel") -> dict[str, str]:
    """Override provider/model settings from environment variables.

    Returns:
        Mapping of environment variables that were applied.
    """
    applied: dict[str, str] = {}

    match provider.type:
        case "openai":
            if base_url := os.getenv("OPENAI_BASE_URL"):
                provider.base_url = base_url
            if api_key := os.getenv("OPENAI_API_KEY"):
                provider.api_key = SecretStr(api_key)
        case _:
            pass

    return applied


def create_llm(
    provider: "LLMProvider",
    model: "LLMModel",
    *,
    stream: bool = True,
    session_id: str | None = None,
    use_cache: bool = False,
) -> LLM:
    match provider.type:
        case "openai":
            from kosong.contrib.chat_provider.openai_responses import OpenAIResponses

            chat_provider = OpenAIResponses(
                model=model.model,
                base_url=provider.base_url,
                api_key=provider.api_key.get_secret_value(),
                stream=stream,
            )
        case "anthropic":
            from kosong.contrib.chat_provider.anthropic import Anthropic

            chat_provider = Anthropic(
                model=model.model,
                base_url=provider.base_url,
                api_key=provider.api_key.get_secret_value(),
                stream=stream,
                default_max_tokens=50000,
            )

    return LLM(
        chat_provider=chat_provider,
        max_context_size=model.max_context_size,
        capabilities=model.capabilities or set(),
        use_cache=use_cache,
    )
