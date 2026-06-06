from collections.abc import Callable
from dataclasses import dataclass

from openai.types.chat import ChatCompletionToolParam


@dataclass
class ToolDefinition:
    name: str
    schema: ChatCompletionToolParam
    handler: Callable[..., str]
