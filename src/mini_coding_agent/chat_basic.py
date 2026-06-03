from openai.types.chat import ChatCompletionMessageParam

from .agent_loop import agent_loop
from .llm_client import create_client
from .single_tool import RUN_ANYTHING_TOOL

SYSTEM_PROMPT = """You are a minimal coding assistant. You help users with coding questions and file-related tasks.

## Tool

You have access to one tool:
- `run_anything`: dispatch to one of three actions:
  - `get_time`: get the current time in a timezone
  - `read_text_file`: read a text file by path
  - `echo_text`: repeat text exactly

## Rules

- Only call a tool when it is clearly needed. Do not call tools speculatively.
- For `run_anything`, set `action` to exactly one of `get_time`, `read_text_file`, or `echo_text`.
- Set `args` to the single string argument required by that action.
- If a tool returns an error, report the error to the user clearly. Do not pretend it succeeded.
- Do not assume file content without reading it first.
- Keep responses short and direct. Do not repeat the user's question back to them.
- If you cannot answer without a tool and no suitable action exists, say so."""


def main() -> None:
    print("Welcome to MINI_CODING_AGENT")

    llm = create_client()

    while True:
        input_message = input("You: ").strip()

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
            tools=[RUN_ANYTHING_TOOL.schema],
            tool_choice="auto",
        )

        msg = response.choices[0].message

        if msg.tool_calls:
            result = agent_loop(llm, messages, msg, [RUN_ANYTHING_TOOL], 5)
            print(f"Assistant: {result}")
        else:
            print(f"Assistant: {msg.content}")


if __name__ == "__main__":
    main()
