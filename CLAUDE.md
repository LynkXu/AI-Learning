# Project Guidelines for Claude

## After Every Code Change

### 1. Fix Import Errors

After modifying any file, check for and fix unresolved import errors (e.g., basedpyright `reportMissingImports`):

1. Verify all imported packages are listed in `requirements.txt`
2. If a package is missing, add it to `requirements.txt` and run `pip install -r requirements.txt`
3. Confirm the import resolves correctly before finishing the task

### 2. Explain Code Changes in Go Terms

After every code change, explain the modified code using Go concepts as analogies. For example:

- Python `BaseModel` inheritance → Go struct embedding
- Multiple return values → Go `val, err := fn()`
- `None` check → Go `nil` check
- `dict[str, str]` → Go `map[string]string`
- `response_format` / tool calling → Go interface / union type dispatch

The goal is to help the user build intuition by mapping unfamiliar Python/AI SDK patterns to familiar Go patterns.
