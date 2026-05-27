from .llm_client import create_client


def main() -> None:
    client, settings = create_client()
    response = client.chat.completions.create(
        model=settings["model"],
        messages=[
            {
                "role": "user",
                "content": "Use one sentence to explain what an AI agent is.",
            }
        ],
    )

    print(f"provider: {settings['provider']}")
    print(f"model: {settings['model']}")
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
