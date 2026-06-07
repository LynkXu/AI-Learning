import json

from openai.types.chat import (
    ChatCompletionMessage,
    ChatCompletionMessageParam,
    ChatCompletionToolMessageParam,
)
from openai.types.chat.chat_completion_message_function_tool_call import (
    ChatCompletionMessageFunctionToolCall,
)

from .llm_client import LLMClient
from .tools import ToolDefinition


def agent_loop(
    llm: LLMClient,
    messages: list[ChatCompletionMessageParam],
    first_response: ChatCompletionMessage,
    tool_list: list[ToolDefinition],
    max_turns: int = 10,
) -> str:
    msg = first_response

    for _ in range(max_turns):
        if not msg.tool_calls:
            return msg.content or ""

        messages.append(msg.model_dump(exclude_unset=True))  # type: ignore[arg-type]

        for tool_call in msg.tool_calls or []:
            if not isinstance(tool_call, ChatCompletionMessageFunctionToolCall):
                continue
            result = execute_tool(tool_call, tool_list)
            messages.append(tool_result_message(tool_call, result))

        response = llm.client.chat.completions.create(
            model=llm.model,
            messages=messages,
            tools=[t.schema for t in tool_list],
        )

        msg = response.choices[0].message

    return "Error: Exceeded maximum number of turns without a final answer."


def execute_tool(
    tool_call: ChatCompletionMessageFunctionToolCall, tools: list[ToolDefinition]
) -> str:
    handlers = {t.name: t.handler for t in tools}
    handler = handlers.get(tool_call.function.name)
    if handler is None:
        return f"Error: Unknown tool '{tool_call.function.name}'."
    args = json.loads(tool_call.function.arguments)

    print(f"Executing tool '{tool_call.function.name}' with arguments: {args} \n")
    return handler(**args)


def tool_result_message(
    tool_call: ChatCompletionMessageFunctionToolCall, result: str
) -> ChatCompletionToolMessageParam:
    return {
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": result,
    }
