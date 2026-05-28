from .llm_client import create_client
from .structured_output import MathReasoning


def main() -> None:
    # welcome
    print("Welcome to MINI_CODING_AGENT")

    # create client
    client, settings = create_client()

    # while True:
    #     input_message = input("You: ").strip()

    #     if not input_message:
    #         continue

    #     if input_message.lower() in {"exit", "quit"}:
    #         print("Bye")
    #         break

    #     response = client.chat.completions.create(
    #         model=settings["model"],
    #         messages=[
    #             {
    #                 "role": "user",
    #                 "content": input_message,
    #             }
    #         ],
    #     )

    #     print(f"provider: {settings['provider']}")
    #     print(f"model: {settings['model']}")
    #     print(response.choices[0].message.content)
    #
    #

    response = client.chat.completions.parse(
        model=settings["model"],
        messages=[
            {
                "role": "user",
                "content": "How can I solve 8x + 7 = -23? Guide the user through the solution step by step.",
            }
        ],
        response_format=MathReasoning,
    )

    parsed = response.choices[0].message.parsed

    if parsed is None:
        print("No structured output was parsed.")
        return

    print(parsed.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
