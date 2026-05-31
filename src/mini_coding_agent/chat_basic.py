from openai.types.chat import (
    ChatCompletionMessageParam,
)

from .agent_loop import agent_loop
from .llm_client import create_client
from .tools import tool_list

SYSTEM_PROMPT = """You are a minimal coding assistant. You help users with coding questions and file-related tasks.

## Tools

You have access to the following tools:
- `get_time`: Get the current time in a specific timezone. Use only when the user explicitly asks for the current time or date.
- `read_text_file`: Read the content of a text file by path. Use when the user asks you to read a file, or when you need file content to answer a question.
- `echo_text`: Echo back a piece of text exactly. Use only when the user explicitly asks you to repeat something.

## Rules

- Only call a tool when it is clearly needed. Do not call tools speculatively.
- If a tool returns an error, report the error to the user clearly. Do not pretend it succeeded.
- Do not assume file content without reading it first.
- Keep responses short and direct. Do not repeat the user's question back to them.
- If you cannot answer without a tool and no suitable tool exists, say so."""


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
            tools=[t.schema for t in tool_list],
            tool_choice="auto",
        )

        msg = response.choices[0].message

        if msg.tool_calls:
            result = agent_loop(llm,messages,msg,tool_list,20)
            print(f"Assistant(Tool): {result}")
        else:
            print(f"Assistant: {msg.content}")


if __name__ == "__main__":
    main()
