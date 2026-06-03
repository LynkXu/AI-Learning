import openai
from pydantic import BaseModel

from .tools import ToolDefinition, run_echo_text, run_get_time, run_read_text_file


class RunAnything(BaseModel):
    action: str
    args: str


def run_anything(action: str, args: str) -> str:
    if action == "get_time":
        return run_get_time(args)
    if action == "echo_text":
        return run_echo_text(args)
    if action == "read_text_file":
        return run_read_text_file(args)

    return (
        f"Error: Unknown action '{action}'. "
        "Valid actions are 'get_time', 'echo_text', and 'read_text_file'."
    )


RUN_ANYTHING_TOOL = ToolDefinition(
    name="run_anything",
    schema=openai.pydantic_function_tool(
        RunAnything,
        name="run_anything",
        description=(
            "Use this tool only when one of these three actions is clearly needed: "
            "'get_time' for the current time/date in a specific timezone, "
            "'echo_text' to repeat text exactly, or "
            "'read_text_file' to read a text file by path. "
            "Set 'action' to one of those exact names. "
            "Set 'args' to the single string argument required by that action: "
            "a timezone like 'Asia/Shanghai', text to echo, or a file path to read. "
            "Do not use this tool for any other action."
        ),
    ),
    handler=run_anything,
)
