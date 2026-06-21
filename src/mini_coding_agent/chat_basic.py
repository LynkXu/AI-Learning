from openai.types.chat import ChatCompletionMessageParam
from prompt_toolkit import prompt as pt_prompt

from .agent_loop import agent_loop
from .llm_client import create_client
from .tools import DEFAULT_TOOLS

SYSTEM_PROMPT = """You are a minimal coding assistant. You help users inspect, understand, and safely validate codebases.

## Tool use

Use the provided tool schemas as the source of truth for available tools and arguments.
Prefer read-only repo tools before command execution.

## Rules

- Only call a tool when it is clearly needed. Do not call tools speculatively.
- Treat tool arguments as untrusted input; rely on tools to enforce safety boundaries.
- If a tool returns an error, report the error to the user clearly. Do not pretend it succeeded.
- Do not assume file content without reading it first.
- Never claim a command succeeded unless tool output confirms it.
- Keep responses short and direct. Do not repeat the user's question back to them.
- If you cannot answer without a tool and no suitable tool exists, say so.
- When displaying tool output (file contents, search results), always show it verbatim. Do not add, remove, reformat, or modify any content including line numbers and comments."""


def main() -> None:
    print("Welcome to MINI_CODING_AGENT")

    llm = create_client()

    while True:
        input_message = pt_prompt("You: ").strip()

        if not input_message:
            continue

        if input_message.lower() in ["exit", "quit"]:
            break

        messages: list[ChatCompletionMessageParam] = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": input_message},
        ]

        response = llm.client.chat.completions.create(
            model=llm.model,
            messages=messages,
            tools=[t.schema for t in DEFAULT_TOOLS],
            tool_choice="auto",
        )

        msg = response.choices[0].message

        if msg.tool_calls:
            result = agent_loop(llm, messages, msg, DEFAULT_TOOLS, 10)
            print(f"Assistant: {result}")
        else:
            print(f"Assistant: {msg.content}")


if __name__ == "__main__":
    main()
