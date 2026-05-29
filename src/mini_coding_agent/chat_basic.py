from typing import cast

from openai.types.chat import (
    ChatCompletionAssistantMessageParam,
    ChatCompletionMessageParam,
    ChatCompletionToolMessageParam,
)

from .llm_client import create_client
from .single_tool import CALCULATOR_TOOL, CalculatorInput, run_calculator


def main() -> None:
    print("Welcome to MINI_CODING_AGENT")

    client, settings = create_client()

    while True:
        input_message = input("You: ").strip()

        if not input_message:
            continue

        if input_message.lower() in ["exit", "quit"]:
            break

        messages: list[ChatCompletionMessageParam] = [
            {"role": "user", "content": input_message}
        ]

        response = client.chat.completions.create(
            model=settings["model"],
            messages=messages,
            tools=[CALCULATOR_TOOL],
            tool_choice="auto",
        )

        msg = response.choices[0].message

        if msg.tool_calls:
            assistant_message = cast(
                ChatCompletionAssistantMessageParam,
                msg.model_dump(exclude_none=True),
            )
            messages.append(assistant_message)

            for tool_call in msg.tool_calls:
                args = CalculatorInput.model_validate_json(tool_call.function.arguments)
                result = run_calculator(args.expression)
                tool_message: ChatCompletionToolMessageParam = {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result,
                }
                messages.append(tool_message)

            follow_up = client.chat.completions.create(
                model=settings["model"],
                messages=messages,
            )
            print(f"Assistant(Tool): {follow_up.choices[0].message.content}")
        else:
            print(f"Assistant: {msg.content}")


if __name__ == "__main__":
    main()
