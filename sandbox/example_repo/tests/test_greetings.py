from greetings import build_greeting


def test_build_greeting_uses_name() -> None:
    assert build_greeting("Link") == "Hello, Link!"


def test_build_greeting_falls_back_for_blank_name() -> None:
    assert build_greeting("   ") == "Hello, there!"
