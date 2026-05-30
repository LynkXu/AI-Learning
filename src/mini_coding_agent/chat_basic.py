from openai.types.chat import (
    ChatCompletionMessageParam,
)

from .agent_loop import agent_loop
from .llm_client import create_client
from .tools import tool_list


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
            {"role": "user", "content": input_message}
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
