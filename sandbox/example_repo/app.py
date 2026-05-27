from config import APP_NAME, DEFAULT_USER
from greetings import build_greeting


def main() -> None:
    message = build_greeting(DEFAULT_USER)
    print(f"[{APP_NAME}] {message}")


if __name__ == "__main__":
    main()
