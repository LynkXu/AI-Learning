import os

import openai
from pydantic import BaseModel

from .base import ToolDefinition
from .security import safe_path


# -------------
# utility functions
# -------------
class ListFiles(BaseModel):
    directory_path: str
    pattern: str = ""


class ReadFile(BaseModel):
    file_path: str


class SearchCode(BaseModel):
    query: str


# --------------
# tool handlers
# --------------
def list_files(directory_path: str, pattern: str = "") -> str:
    import fnmatch

    try:
        safe_dir = safe_path(directory_path or ".")
    except ValueError as e:
        return str(e)

    maxFileCount = 200
    files = []
    for root, dirs, filenames in os.walk(safe_dir):
        for filename in filenames:
            if pattern and not fnmatch.fnmatch(filename, f"*{pattern}*"):
                continue
            files.append(os.path.relpath(os.path.join(root, filename), safe_dir))
            if len(files) >= maxFileCount:
                break
        if len(files) >= maxFileCount:
            break

    if not files:
        return "No files found."
    return "\n".join(files)


def read_file(file_path: str) -> str:
    max_lines = 100
    try:
        safe_file = safe_path(file_path)
        with open(safe_file, "r") as f:
            lines = []
            truncated = False
            for line in f:
                if len(lines) >= max_lines:
                    truncated = True
                    break
                lines.append(line.rstrip("\n"))
        numbered = "\n".join(f"{i + 1}: {line}" for i, line in enumerate(lines))
        if truncated:
            numbered += "\n... (truncated)"
        return numbered
    except ValueError as e:
        return str(e)
    except Exception as e:
        return f"Error reading file: {e}"


def search_code(query: str) -> str:
    import shutil
    import subprocess

    max_matches = 100
    results: list[str] = []

    if shutil.which("rg"):
        # search file contents
        content_cmd = ["rg", "-n", "--", query]
        # search file names
        filename_cmd = ["rg", "--files", "-g", f"*{query}*"]
        cmds = [content_cmd, filename_cmd]
    else:
        cmds = [["grep", "-rn", "--", query, "."]]

    for cmd in cmds:
        try:
            output = subprocess.check_output(cmd, text=True, stderr=subprocess.DEVNULL)
            results.extend(output.strip().split("\n"))
        except subprocess.CalledProcessError:
            pass
        except Exception as e:
            return f"Error searching code: {e}"

    if not results:
        return "No matches found."

    truncated = len(results) > max_matches
    output_lines = results[:max_matches]
    if truncated:
        output_lines.append(f"... (truncated, showing {max_matches} of {len(results)} matches)")
    return "\n".join(output_lines)


# ----------------
# tool definitions
# ----------------

LIST_FILES_TOOL = ToolDefinition(
    name="list_files",
    schema=openai.pydantic_function_tool(
        ListFiles,
        name="list_files",
        description="List files recursively under a directory. "
        "directory_path is the root to search (use '.' for the project root). "
        "pattern is an optional filename filter (e.g. 'repo.py', '.py') — leave empty to list all files. "
        "Returns relative file paths, one per line, up to 200 results. "
        "Use this to explore directory structure or find files by name.",
    ),
    handler=list_files,
)


READ_FILE_TOOL = ToolDefinition(
    name="read_file",
    schema=openai.pydantic_function_tool(
        ReadFile,
        name="read_file",
        description="Read the content of a text file. "
        "The input is a file path. "
        "Return the content of the file. "
        "By default, only return the first 100 lines. "
        "Indicate if the content is truncated. "
        "Use this tool when you need to read the content of a file to answer the user's question or to get information about the file.",
    ),
    handler=read_file,
)

SEARCH_CODE_TOOL = ToolDefinition(
    name="search_code",
    schema=openai.pydantic_function_tool(
        SearchCode,
        name="search_code",
        description="Search codebase for files matching a query. "
        "The input is a search query. "
        "Return a list of file paths that match the query, one per line. "
        "If there are too many results, only return the first 100 matches and indicate that there are more matches not shown. "
        "Return lines in the format of 'file_path:line_number:line_content' to provide more context. "
        "Use this tool when you need to find files related to a specific topic, function, or keyword in the codebase.",
    ),
    handler=search_code,
)
