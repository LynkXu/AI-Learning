from .llm_client import create_client
from .single_tool import MATH_TOOL, MathReasoning


def main() -> None:
    print("Welcome to MINI_CODING_AGENT")

    client, settings = create_client()

    while True:
        input_message = input("You: ").strip()

        if not input_message:
            continue

        if input_message.lower() in ["exit", "quit"]:
            break

        response = client.chat.completions.create(
            model=settings["model"],
            messages=[{"role": "user", "content": input_message}],
            tools=[MATH_TOOL],
            tool_choice="auto",  # model decides whether to call the tool
        )

        msg = response.choices[0].message

        if msg.tool_calls:
            # Go 类比: union type 断言 — 模型返回了结构化数据
            raw = msg.tool_calls[0].function.arguments
            result = MathReasoning.model_validate_json(raw)
            print(result.model_dump_json(indent=2))
        else:
            print(f"Assistant: {msg.content}")


if __name__ == "__main__":
    main()
