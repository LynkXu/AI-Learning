import subprocess
from pathlib import Path

import openai
from pydantic import BaseModel, Field

from .base import ToolDefinition
from .security import PROJECT_ROOT, safe_path


# tool class
class CommandRunner(BaseModel):
    command: str
    args: list[str] = Field(default_factory=list)
    working_directory: str = "."


# tool handler
TOOL_WHITELIST = {"ls", "cat", "echo", "pwd", "date", "rg", "pytest"}
MAX_OUTPUT_CHARS = 4000
TIMEOUT_SECONDS = 10


def _format_output(stdout: str, stderr: str) -> str:
    parts = []
    if stdout:
        parts.append(stdout.rstrip())
    if stderr:
        parts.append(f"stderr:\n{stderr.rstrip()}")

    output = "\n".join(parts).strip()
    if not output:
        output = "Command completed successfully with no output."

    if len(output) > MAX_OUTPUT_CHARS:
        return output[:MAX_OUTPUT_CHARS] + (
            f"\n... (truncated, output exceeded {MAX_OUTPUT_CHARS} characters)"
        )
    return output


def _check_project_path(path_arg: str, cwd: Path) -> None:
    candidate = Path(path_arg)
    resolved = (candidate if candidate.is_absolute() else cwd / candidate).resolve()
    if not resolved.is_relative_to(PROJECT_ROOT):
        raise ValueError(f"Access denied: '{path_arg}' is outside the project root.")


def _looks_like_path(arg: str) -> bool:
    return arg.startswith((".", "/")) or "/" in arg


def _validate_path_args(command: str, args: list[str], cwd: Path) -> None:
    if command in {"ls", "cat"}:
        for arg in args:
            if arg.startswith("-"):
                continue
            _check_project_path(arg, cwd)
        return

    if command == "rg":
        non_option_args = [arg for arg in args if not arg.startswith("-")]
        for path_arg in non_option_args[1:]:
            _check_project_path(path_arg, cwd)
        return

    if command == "pytest":
        for arg in args:
            if arg.startswith("-"):
                continue
            if "::" in arg:
                path_part = arg.split("::", 1)[0]
                if path_part:
                    _check_project_path(path_part, cwd)
            elif _looks_like_path(arg):
                _check_project_path(arg, cwd)


def command_runner(
    command: str, args: list[str] | None = None, working_directory: str = "."
) -> str:
    args = args or []

    if command not in TOOL_WHITELIST:
        return (
            f"Error: Command '{command}' is not allowed. "
            f"Allowed commands are: {', '.join(sorted(TOOL_WHITELIST))}."
        )

    try:
        safe_cwd = safe_path(working_directory)
        _validate_path_args(command, args, safe_cwd)
    except ValueError as e:
        return str(e)

    try:
        result = subprocess.run(
            [command, *args],
            cwd=safe_cwd,
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
            shell=False,
            check=False,
        )
    except FileNotFoundError:
        return f"Error: Command '{command}' was not found."
    except subprocess.TimeoutExpired as e:
        stdout = e.stdout if isinstance(e.stdout, str) else ""
        stderr = e.stderr if isinstance(e.stderr, str) else ""
        output = _format_output(stdout, stderr)
        return f"Error: Command timed out after {TIMEOUT_SECONDS} seconds.\n{output}"
    except Exception as e:
        return f"Error: Failed to run command: {e}"

    output = _format_output(result.stdout, result.stderr)
    if result.returncode != 0:
        return f"Error: Command exited with code {result.returncode}.\n{output}"
    return output



# Tool definition
COMMAND_RUNNER_TOOL = ToolDefinition(
    name="command_runner",
    schema=openai.pydantic_function_tool(
        CommandRunner,
        name="command_runner",
        description="Run an allowed command without a shell and return its output. "
        "args is the argument list; do not combine command and args into one string. "
        "working_directory is the directory to run in and must stay inside the project root. "
        "Output is truncated if it exceeds the limit, and the command times out if it runs too long.",
    ),
    handler=command_runner,
)
