import openai
from pydantic import BaseModel

from .base import ToolDefinition


class ListFiles(BaseModel):
    directory_path: str


class ReadFile(BaseModel):
    file_path: str


class SearchCode(BaseModel):
    query: str


# --------------
# tool handlers
# --------------
def list_files(directory_path: str) -> str:
    # - 列出某目录下的文件/子目录
    # - 限制返回条数，比如最多 200 条
    # - 返回相对路径，不要绝对路径噪音
    maxFileCount = 200
    import os

    files = []
    for root, dirs, filenames in os.walk(directory_path):
        for filename in filenames:
            files.append(os.path.relpath(os.path.join(root, filename), directory_path))
            if len(files) >= maxFileCount:
                break
        if len(files) >= maxFileCount:
            break
    return "\n".join(files)


def read_file(file_path: str) -> str:
    # - 读取文本文件内容
    # - 默认只返回前 100 行
    # - 说明是否发生截断
    max_lines = 100
    try:
        with open(file_path, "r") as f:
            lines = []
            truncated = False
            for line in f:
                if len(lines) >= max_lines:
                    truncated = True
                    break
                lines.append(line.rstrip("\n"))
        content = "\n".join(lines)
        if truncated:
            content += "\n... (truncated)"
        return content
    except Exception as e:
        return f"Error reading file: {e}"


# ----------------
# tool definitions
# ----------------

LIST_FILES_TOOL = ToolDefinition(
    name="list_files",
    schema=openai.pydantic_function_tool(
        ListFiles,
        name="list_files",
        description="List files and subdirectories in a specified directory. "
        "The input is a directory path. "
        "Return a list of relative file paths, one per line. "
        "Limit the output to at most 200 files. "
        "Use this tool when the user asks to see the contents of a directory or when you need to find files in a directory.",
    ),
    handler=list_files,
)
