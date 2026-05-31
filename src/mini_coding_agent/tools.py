from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime

import openai
import pytz
from openai.types.chat import ChatCompletionToolParam
from pydantic import BaseModel


@dataclass
class ToolDefinition:
    name: str
    schema: ChatCompletionToolParam
    handler: Callable[..., str]


# ------------------------
# input schemas
# ------------------------


class GetTime(BaseModel):
    """Get the current time in a specified timezone."""

    timezone: str


class EchoText(BaseModel):
    """Echo back the input text."""

    text: str


class ReadTextFile(BaseModel):
    """Read the content of a text file given its file path."""

    file_path: str


# ------------------------
# tool implementations
# ------------------------


def run_get_time(timezone: str) -> str:
    try:
        tz = pytz.timezone(timezone)
    except pytz.UnknownTimeZoneError:
        return f"Error: Unknown timezone '{timezone}'. Please provide a valid timezone in the format 'Continent/City'."

    now = datetime.now(tz)
    return now.strftime("%Y-%m-%d %H:%M:%S")


def run_echo_text(text: str) -> str:
    return text


def run_read_text_file(file_path: str) -> str:
    try:
        with open(file_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: File not found at path '{file_path}'."
    except Exception as e:
        return f"Error reading file: {str(e)}"


# ------------------------
# tool registry
# ------------------------

GET_TIME = ToolDefinition(
    name="get_time",
    schema=openai.pydantic_function_tool(
        GetTime,
        name="get_time",
        description=(
            "Use this tool when the user asks for the current time or current date in a specific timezone. "
            "The input must be a valid IANA timezone string such as 'America/New_York' or 'Asia/Shanghai'. "
            "Do not use this tool for timezone conversion, scheduling advice, or when the user did not ask for the current time."
        ),
    ),
    handler=run_get_time,
)

ECHO_TEXT = ToolDefinition(
    name="echo_text",
    schema=openai.pydantic_function_tool(
        EchoText,
        name="echo_text",
        description=(
            "Use this tool to echo back the input text. The input is a string and the output should be exactly the same string. This tool is useful for testing and debugging purposes."
            "Do not use this tool unless the user explicitly asks you to repeat some text back to them, or if you want to confirm that you understood the user's input correctly by echoing it back."
        ),
    ),
    handler=run_echo_text,
)

READ_TEXT_FILE = ToolDefinition(
    name="read_text_file",
    schema=openai.pydantic_function_tool(
        ReadTextFile,
        name="read_text_file",
        description=(
            "Use this tool to read the content of a text file given its file path. The file path should be absolute or relative to the current working directory."
            "The input is a string representing the file path, and the output should be the content of the file as a string."
            "Use this tool when the user asks you to read a text file or when you need to access information stored in a text file. Make sure to handle errors gracefully, such as when the file does not exist or cannot be read."
            "Do not use this tool for non-text files, for writing to files, or when the user did not ask for file content."
        ),
    ),
    handler=run_read_text_file,
)

tool_list = [GET_TIME, ECHO_TEXT, READ_TEXT_FILE]
