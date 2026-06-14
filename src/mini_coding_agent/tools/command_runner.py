import shlex

import openai
from pydantic import BaseModel

from .base import ToolDefinition
from .security import _safe_path


# tool class
class CommandRunner(BaseModel):
    command: str


# tool handler
Tool_Whitelist = ["ls", "cat", "echo", "pwd", "date","rg","pytest"]
def command_runner(command: str) -> str:
    # tool white list
    # work directory check
    # timeout
    # response length limit
    # common error handling, like command not found, non-zero exit code, timeout, overize output, etc.


    # 1. split the command by shlex
    try:
        command_parts = shlex.split(command)
    except ValueError as e:
        return f"Error: Failed to parse command. {str(e)}"

    command = command_parts[0]  # Get the base command


    # 2. check the command is in the white list
    if command not in Tool_Whitelist:
        return f"Error: Command '{command}' is not allowed. Allowed commands are: {', '.join(Tool_Whitelist)}."
    # 3. check the work directory is safe
    # 4. run the command with timeout and output limit
    # 5. return the output or error message



    return ""



# Tool definition
COMMAND_RUNNER_TOOL = ToolDefinition(
    name="command_runner",
    schema=openai.pydantic_function_tool(
        CommandRunner,
        name="command_runner",
        description="Run a shell command and return its output. "
        "command is the shell command to execute. "
        "Returns the command output or an error message if the command fails.",
    ),
    handler=run_command,
)
