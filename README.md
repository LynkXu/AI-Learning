# AI-Learning

This repository is a hands-on workspace for building a minimal coding agent step by step.

- Learning plans live in [docs/12-week-ai-agent-plan.md](/Users/link/Code/AI-Learning/docs/12-week-ai-agent-plan.md:1) and [docs/12-week-ai-agent-plan.zh-CN.md](/Users/link/Code/AI-Learning/docs/12-week-ai-agent-plan.zh-CN.md:1).
- Reusable application code lives in [src/mini_coding_agent](/Users/link/Code/AI-Learning/src/mini_coding_agent).
- Local practice repos and other disposable sandboxes live in [sandbox](/Users/link/Code/AI-Learning/sandbox).

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If `pip install` fails on this machine with certificate verification errors, retry with:

```bash
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```

Create your local secrets file from `.env.example`, then fill in the provider and API key you want to use.

If you do not want to activate the virtual environment every time, use the project-local binaries directly:

```bash
.venv/bin/python -V
.venv/bin/pytest -q
```

## Provider Config

Use `.env` to choose the model provider:

```env
LLM_PROVIDER=openai
OPENAI_API_KEY=
CEREBRAS_API_KEY=
MODEL_NAME=gpt-4.1-mini
```

For OpenAI:

- `LLM_PROVIDER=openai`
- fill in `OPENAI_API_KEY`
- set `MODEL_NAME` to an OpenAI model such as `gpt-4.1-mini`

For Cerebras:

- `LLM_PROVIDER=cerebras`
- fill in `CEREBRAS_API_KEY`
- set `MODEL_NAME` to a Cerebras-served model such as `gpt-oss-120b`

## Common Commands

- `make chat-basic`: send one minimal request through the configured model provider
- `make example-run`: run the local practice repo
- `make example-test`: run the practice repo tests

```bash
make chat-basic
make example-run
make example-test
```

The provider switch is implemented in [llm_client.py](/Users/link/Code/AI-Learning/src/mini_coding_agent/llm_client.py:1). It uses the standard `openai` Python package for both OpenAI and Cerebras, and points Cerebras requests at `https://api.cerebras.ai/v1`.

## Current Status

The repository is currently at a clean "Week 1 foundation" stage:

- environment is set up with a project-local `.venv`
- provider switching between OpenAI and Cerebras works through one shared client
- `make chat-basic` sends a real model request
- `sandbox/example_repo/` gives you one small local repo for code-reading and testing practice
- `make example-test` confirms the sandbox repo is still behaving as expected

This means the project is ready for the next small capabilities:

- strict structured output
- one simple tool call
- the first minimal agent loop

## Current Call Chain

`make chat-basic` currently flows like this:

1. `Makefile` runs `PYTHONPATH=src .venv/bin/python -m mini_coding_agent.chat_basic`
2. [chat_basic.py](/Users/link/Code/AI-Learning/src/mini_coding_agent/chat_basic.py:1) imports `create_client()`
3. [llm_client.py](/Users/link/Code/AI-Learning/src/mini_coding_agent/llm_client.py:11) loads `.env` and chooses `openai` or `cerebras`
4. `client.chat.completions.create(...)` sends the actual API request
5. the script prints the active provider, model name, and model response

`make example-run` currently flows like this:

1. `Makefile` runs `sandbox/example_repo/app.py`
2. `app.py` imports `config.py` and `greetings.py`
3. `build_greeting()` returns the greeting text
4. the app prints the final message

## Repository Layout

```text
AI-Learning/
├── README.md
├── Makefile
├── requirements.txt
├── docs/
│   ├── 12-week-ai-agent-plan.md
│   └── 12-week-ai-agent-plan.zh-CN.md
├── src/
│   └── mini_coding_agent/
│       ├── __init__.py
│       ├── chat_basic.py
│       └── llm_client.py
├── sandbox/
│   └── example_repo/
├── notes/
├── logs/
├── eval/
└── examples/
```

## Workspace

- `docs/`: learning plans and long-form project notes
- `src/mini_coding_agent/`: the reusable application code you are building
- `sandbox/example_repo/`: small practice repository for repo-reading and command tasks
- `notes/`: weekly notes and retrospectives
- `logs/`: run logs and traces
- `eval/`: evaluation tasks and baselines
- `examples/`: reusable examples and patch cases

## What To Build Next

As you continue the 12-week plan, new reusable code should usually go under `src/mini_coding_agent/`.

- Week 1-2: `structured_output.py`, `single_tool.py`, `agent_loop.py`, `tools.py`
- Week 4-6: `repo_tools.py`, `command_runner.py`, `patch_generator.py`
- Week 7+: `main.py`, `tracing.py`, `context_manager.py`, `doc_retriever.py`

Keep temporary practice targets, tiny broken repos, and throwaway experiments under `sandbox/` rather than in the repository root.

If you want the most practical next sequence from the current state, do it in this order:

1. Add `structured_output.py` and make one response conform to a fixed schema.
2. Add `single_tool.py` with one safe fake tool such as `get_time`.
3. Add `agent_loop.py` that can repeat until it gets either a final answer or a tool call.
4. Reuse `sandbox/example_repo/` once you start adding repo-reading tools.

## Troubleshooting

- If `make chat-basic` fails with a missing key error, check `.env` and make sure the key matches `LLM_PROVIDER`.
- If `make chat-basic` fails with authentication or `401`, your API key is wrong, expired, or tied to the wrong provider.
- If `make chat-basic` fails with a model error, check whether `MODEL_NAME` is valid for the selected provider.
- If `pip install` starts failing with certificate verification again after switching Python versions, the new Python installation may need its CA bundle repaired separately.
- If imports fail for code under `src/`, prefer running commands through `make` or with `PYTHONPATH=src`.
- If sandbox tests fail unexpectedly, rerun `make example-test` before changing agent code so you know whether the breakage came from the sandbox repo or your new code.

## Suggested First Hour

If you are not sure what to do next, spend the next hour like this:

1. Run `make chat-basic` once and read [chat_basic.py](/Users/link/Code/AI-Learning/src/mini_coding_agent/chat_basic.py:1) line by line.
2. Run `make example-run` and `make example-test` once so you know the sandbox repo baseline.
3. Create `src/mini_coding_agent/structured_output.py`.
4. Write a short note in `notes/week1.md` explaining the boundary between "model output" and "application code".

## reference
- https://learn.shareai.run/zh/s01/
- https://github.com/flingjie/Agent-100-Days/tree/main
