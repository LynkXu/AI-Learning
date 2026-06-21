from .base import ToolDefinition
from .basic import ECHO_TEXT, GET_TIME, READ_TEXT_FILE, tool_list
from .broad import RUN_ANYTHING_TOOL
from .command_runner import COMMAND_RUNNER_TOOL
from .repo import LIST_FILES_TOOL, READ_FILE_TOOL, SEARCH_CODE_TOOL

WEEK4_TOOLS = [LIST_FILES_TOOL, READ_FILE_TOOL, SEARCH_CODE_TOOL]
WEEK5_TOOLS = [COMMAND_RUNNER_TOOL]
DEFAULT_TOOLS = WEEK5_TOOLS

__all__ = [
    "ToolDefinition",
    "GET_TIME",
    "ECHO_TEXT",
    "READ_TEXT_FILE",
    "RUN_ANYTHING_TOOL",
    "LIST_FILES_TOOL",
    "READ_FILE_TOOL",
    "SEARCH_CODE_TOOL",
    "COMMAND_RUNNER_TOOL",
    "WEEK4_TOOLS",
    "WEEK5_TOOLS",
    "DEFAULT_TOOLS",
    "tool_list",
]

__WEEK4_TOOL_LIST__ = WEEK4_TOOLS
