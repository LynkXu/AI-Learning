# AI-Learning

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

## First Request

Run the minimal example:

```bash
make chat-basic
```

The provider switch is implemented in [llm_client.py](/Users/link/Code/AI-Learning/src/mini_coding_agent/llm_client.py:1). It uses the standard `openai` Python package for both OpenAI and Cerebras, and points Cerebras requests at `https://api.cerebras.ai/v1`.

## Example Repo Commands

Run the local practice repo:

```bash
make example-run
```

Run its tests:

```bash
make example-test
```

## Workspace

- `docs/`: learning plans and long-form project notes
- `src/mini_coding_agent/`: the reusable application code you are building
- `sandbox/example_repo/`: small practice repository for repo-reading and command tasks
- `notes/`: weekly notes and retrospectives
- `logs/`: run logs and traces
- `eval/`: evaluation tasks and baselines
- `examples/`: reusable examples and patch cases

## reference
- https://learn.shareai.run/zh/s01/
- https://github.com/flingjie/Agent-100-Days/tree/main
