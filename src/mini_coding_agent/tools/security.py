from pathlib import Path

PROJECT_ROOT = Path.cwd().resolve()

def _safe_path(user_path: str) -> Path:
    """Resolve path and reject anything outside PROJECT_ROOT."""
    resolved = (PROJECT_ROOT / user_path).resolve()
    if not resolved.is_relative_to(PROJECT_ROOT):
        raise ValueError(f"Access denied: '{user_path}' is outside the project root.")
    return resolved
