from openai.types.chat import ChatCompletionMessageParam
from prompt_toolkit import prompt as pt_prompt

from .agent_loop import agent_loop
from .llm_client import create_client
from .tools import __WEEK4_TOOL_LIST__

SYSTEM_PROMPT = """You are a minimal coding assistant. You help users inspect and understand codebases.

## Tools

You have access to three tools:
- `list_files(directory_path, pattern?)`: list files recursively under a path (up to 200 entries, relative paths). Use optional `pattern` to filter by filename (e.g. `pattern="repo.py"`). Use this to explore directory structure or find a file by name.
- `read_file(file_path)`: read a text file, returns first 100 lines with line numbers, truncated if longer
- `search_code(query)`: search the codebase for a keyword or pattern. Searches both file contents (returns `file:line:content`) and file names matching the pattern. Use this to find where a function, symbol, or filename appears.

## Rules

- Only call a tool when it is clearly needed. Do not call tools speculatively.
- If a tool returns an error, report the error to the user clearly. Do not pretend it succeeded.
- Do not assume file content without reading it first.
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
            tools=[t.schema for t in __WEEK4_TOOL_LIST__],
            tool_choice="auto",
        )

        msg = response.choices[0].message

        if msg.tool_calls:
            result = agent_loop(llm, messages, msg, __WEEK4_TOOL_LIST__, 10)
            print(f"Assistant: {result}")
        else:
            print(f"Assistant: {msg.content}")


if __name__ == "__main__":
    main()
