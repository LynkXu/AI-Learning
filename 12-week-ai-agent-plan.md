# 12-Week AI Agent Learning Plan

## Goal

Build a minimal but usable coding agent from scratch in 12 weeks, while learning the core engineering concepts behind modern AI agents:

- model calling
- tool calling
- agent loop
- codebase navigation
- controlled execution
- patch generation
- tracing
- evals
- context management
- MCP
- RAG

This plan is designed for a developer with general programming experience and a small amount of ML background, but no prior hands-on experience building agents.

## Principles

Follow these principles throughout the 12 weeks:

1. Build before over-studying. Prefer small working systems over abstract understanding.
2. Start with one agent. Do not introduce multi-agent workflows early.
3. Use real tasks. Learn on top of coding tasks that resemble your work.
4. Measure progress. Keep logs, task results, and failure notes.
5. Add complexity only when the current version is clearly limiting you.

## Recommended Stack

- Language: `Python`
- Interface: `CLI`
- Main project name: `mini-coding-agent`
- Models: any model with function/tool calling support
- Search tool: `rg`
- Test task source: a small demo repo or one of your own side projects

## Before You Start

Prepare these before Week 1 so the 12 weeks stay focused on learning agent behavior instead of setup friction.

### Prerequisites

- Comfortable with basic Python
- Comfortable using the terminal
- Basic understanding of JSON
- Basic understanding of HTTP APIs
- A small local repo you are willing to use as a sandbox

### Environment Setup Checklist

- [ ] Install `Python 3.10+`
- [ ] Create and activate a virtual environment
- [ ] Install basic packages you expect to use, such as:
  - `openai` or another model SDK
  - `pydantic`
  - `rich`
  - `pytest`
- [ ] Confirm `rg` is installed
- [ ] Create a `.env` or equivalent secret-loading approach
- [ ] Add one test repository for experiments
- [ ] Create folders for:
  - `notes/`
  - `logs/`
  - `eval/`
  - `examples/`

### Suggested Project Rules

Use a few simple engineering rules from the beginning:

- Keep prompts in files, not only in source code.
- Log every run, even early prototypes.
- Do not give the agent unrestricted shell access.
- Prefer deterministic helper code outside the model.
- Version your prompts when you change them.

## Weekly Time Budget

Suggested weekly investment: `6-10` hours

- `2-3h` reading and notes
- `3-5h` implementation
- `1-2h` testing and reflection

## Weekly Routine

Repeat this rhythm every week:

1. Read `1-2` core docs
2. Implement one concrete capability
3. Run `3-5` test tasks
4. Record failures and next actions

### Recommended Weekly Split

If you want a default rhythm:

- Day 1: reading and note-taking
- Day 2: core implementation
- Day 3: polish and bug fixing
- Day 4: testing on real tasks
- Day 5: write retrospective and define next week focus

### Weekly Review Questions

Ask these every week:

- What did I build that is actually reusable?
- What did I learn about agent limitations?
- Did the model fail, or did my tool design fail?
- What part of the system is hardest to debug right now?

## Project Outcome

By the end of Week 12, you should have:

- a minimal coding agent
- a repo-reading workflow
- controlled command execution
- patch generation
- run logs and traces
- a small eval set
- basic context management
- a simple MCP understanding or proof of concept
- a basic document retrieval capability

## Milestones

These are the main checkpoints across the 12 weeks:

- End of Week 2: tool-calling loop works
- End of Week 4: agent can inspect a repo
- End of Week 6: agent can propose patches
- End of Week 7: first end-to-end coding agent demo
- End of Week 9: first eval baseline exists
- End of Week 10: context handling is no longer naive
- End of Week 12: coding agent can use docs outside code

## When To Slow Down

If a week feels too ambitious, do not push forward mechanically. Slow down when:

- you do not understand your own loop
- tool outputs are still inconsistent
- logs are too poor to explain failures
- you cannot reproduce whether a change helped or hurt

In that case, repeat the week with a smaller scope.

---

## Week 1: LLM App Basics

### Objective

Understand the minimum pieces of a modern LLM application before building an agent.

### Concepts

- `messages`
- `system prompt`
- `structured output`
- `tool calling`
- `streaming`
- `token usage`
- `cost`

### Tasks

- Set up API access for one model provider.
- Write a script that sends one user message and prints one model response.
- Write a script that asks for structured JSON output.
- Write a script that demonstrates one simple tool call.
- Print raw request and response data in a readable format.
- Record your own explanation of the difference between:
  - model
  - tool
  - agent

### Suggested Time Split

- `1h` API and environment setup
- `2h` first scripts
- `1h` structured output and tool call
- `1h` notes and cleanup

### Suggested Mini Exercises

- Ask the model for a plain answer.
- Ask it for a JSON object with strict fields.
- Ask it to choose whether to call a calculator tool.

### Deliverables

- `chat_basic.py`
- `structured_output.py`
- `single_tool.py`
- `notes/week1.md`

### Acceptance Criteria

- You can explain that the model does not execute tools directly.
- You can explain why an agent needs a control loop.
- You can get one tool call working end to end.

### Reflection Questions

- What does the model know on its own?
- What must your program do outside the model?
- What breaks if the model output is ambiguous?

### Common Failure Modes

- JSON output is malformed
- tool arguments are missing required fields
- script works once but is not reusable
- response printing is too noisy to inspect

### End-of-Week Check

- [ ] I can run all 3 scripts without guessing hidden setup
- [ ] I can explain the boundary between model and application code

---

## Week 2: Minimal Agent Loop

### Objective

Build the simplest usable agent loop.

### Concepts

- tool loop
- stop condition
- final answer
- max turns

### Tasks

- Design a loop that repeats until the task is complete.
- Support three outcomes:
  - direct final answer
  - tool call request
  - forced stop after max turns
- Add `2-3` safe tools:
  - `get_time`
  - `echo_text`
  - `read_text_file`
- Create a tool registry format.
- Log each turn in the console.
- Add basic error handling for invalid tool calls.

### Suggested Time Split

- `2h` loop structure
- `2h` tool registration and execution
- `1h` logging and stop conditions

### Suggested Internal API Shape

You do not need to implement exactly this, but use a stable shape early:

```python
ToolDefinition = {
    "name": "read_text_file",
    "description": "Read a UTF-8 text file from a safe path.",
    "input_schema": {...},
    "handler": read_text_file,
}
```

### Deliverables

- `agent_loop.py`
- `tools.py`
- `notes/week2.md`

### Acceptance Criteria

- The agent can call tools for multiple turns.
- The loop stops reliably.
- The final answer is separated from tool execution steps.

### Practice Tasks

- "What time is it?"
- "Read this file and summarize it."
- "Echo this sentence and then explain what you received."

### Common Failure Modes

- loop never exits
- tool results are not returned in a format the model can use
- tool names in code and prompt drift apart

### End-of-Week Check

- [ ] I can demonstrate a multi-step tool call
- [ ] I have a hard max-turn limit
- [ ] I can explain why the loop stops

---

## Week 3: Prompt and Tool Design

### Objective

Improve stability by designing better tools and prompts.

### Concepts

- tool ergonomics
- tool descriptions
- parameter design
- narrow tools vs broad tools
- instruction quality

### Tasks

- Rewrite tool descriptions so the model knows when to use each one.
- Add input validation for tool parameters.
- Rewrite your system prompt with explicit behavior rules.
- Compare:
  - one broad tool like `run_anything`
  - several narrow tools like `read_file`, `search_code`, `run_tests`
- Create a note with examples of bad tool interfaces.
- Run the same prompts against old and new tool descriptions and compare results.

### Suggested Time Split

- `1h` prompt rewrite
- `2h` tool description rewrite
- `1h` comparison tests
- `1h` notes

### Suggested Comparison Table

Create a small table like this in your notes:

| Prompt | Old tools result | New tools result | Better? | Why |
|---|---|---|---|---|
| Find config file | wrong tool | correct tool | yes | clearer description |

### Deliverables

- `prompt_v1.md`
- `prompt_v2.md`
- `tool_design_notes.md`
- `notes/week3.md`

### Acceptance Criteria

- Tool selection becomes more stable than Week 2.
- You can clearly explain why narrow tools are often better for agents.
- You have at least `5` examples of poor tool or prompt design.

### Reflection Questions

- Which tool descriptions caused wrong tool choices?
- Which instructions reduced unnecessary tool calls?
- Where was the model still confused?

### End-of-Week Check

- [ ] I have a written prompt, not just inline strings
- [ ] I have evidence that tool descriptions matter
- [ ] I can point to one specific improvement from this week

---

## Week 4: Read-Only Codebase Agent

### Objective

Teach the agent to inspect a repository instead of just chatting.

### Concepts

- file listing
- file reading
- code search
- context limits

### Tasks

- Implement:
  - `list_files(path)`
  - `read_file(path)`
  - `search_code(query)`
- Use `rg` for search where possible.
- Add output truncation to avoid huge results.
- Choose a small repo for practice.
- Create test questions such as:
  - where is the entry point
  - where is a function defined
  - where is a route registered
  - where is configuration loaded

### Suggested Practice Repo Size

Pick a repo small enough to understand in under one hour:

- ideally `5-30` source files
- preferably one language
- preferably with one obvious entry point

### Suggested Time Split

- `2h` repo tool implementation
- `1h` safe truncation and formatting
- `2h` question set and testing

### Deliverables

- `repo_tools.py`
- `test_repo_tasks.md`
- `notes/week4.md`

### Acceptance Criteria

- The agent can answer at least `4/5` repo-structure questions.
- The agent can locate files and symbols without manual help.
- File reads stay reasonably scoped.

### Stretch Goal

- Add line numbers to file output.

### Common Failure Modes

- returning whole files when only small snippets are needed
- search results without file paths
- tool output too long for the next model turn

### End-of-Week Check

- [ ] I can ask structural questions about a repo
- [ ] The agent can find code, not just repeat filenames
- [ ] File reading is scoped rather than naive

---

## Week 5: Controlled Command Execution

### Objective

Let the agent gather feedback from the environment safely.

### Concepts

- command whitelisting
- execution boundaries
- timeout
- output limits

### Tasks

- Implement `run_command(cmd)`.
- Restrict commands to a whitelist such as:
  - `pytest`
  - `rg`
  - `ls`
  - `cat`
- Limit working directory scope.
- Add timeout handling.
- Limit maximum output size.
- Handle common failures:
  - command not found
  - non-zero exit code
  - timeout
  - oversized output
- Test with simple failing test cases.

### Safety Rules To Write Down

Document the rules explicitly:

- allowed commands
- blocked commands
- allowed working directory
- output truncation rules
- timeout rules
- whether network access is allowed

### Suggested Time Split

- `2h` command wrapper
- `1h` whitelist enforcement
- `1h` failure formatting
- `1h` tests

### Deliverables

- `command_runner.py`
- `command_policy.md`
- `notes/week5.md`

### Acceptance Criteria

- The agent can run safe commands and consume the results.
- It cannot run arbitrary shell input.
- Failure cases produce readable output for the model.

### Reflection Questions

- Which command outputs are useful as-is?
- Which outputs need summarization?
- What safety risks still remain?

### End-of-Week Check

- [ ] Arbitrary shell input is blocked
- [ ] Large outputs do not overwhelm the agent
- [ ] I know exactly which commands are trusted and why

---

## Week 6: Patch Generation

### Objective

Move from analysis to proposed code changes.

### Concepts

- patch
- diff
- change planning
- reviewability

### Tasks

- Design a patch output format.
- Choose one:
  - unified diff
  - before/after snippet replacement
- Make the agent explain a change before producing it.
- Make the agent summarize affected files after producing it.
- Test on `3` easy bug types:
  - variable typo
  - wrong branch condition
  - incorrect user-facing text

### Suggested Time Split

- `2h` patch format
- `1h` plan-before-change behavior
- `2h` testing on bug cases

### Patch Review Checklist

Before accepting a patch, verify:

- Is the target file correct?
- Is the changed region small and relevant?
- Does the explanation match the change?
- Is there any obviously unrelated edit?

### Deliverables

- `patch_generator.py`
- `examples/`
- `notes/week6.md`

### Acceptance Criteria

- The agent can produce a readable patch for simple bugs.
- A human can inspect the patch quickly.
- The reasoning and the change stay aligned.

### Stretch Goal

- Add a dry-run mode that only previews changes.

### End-of-Week Check

- [ ] The agent can describe a fix before proposing it
- [ ] Patch output is stable enough to review manually
- [ ] I have at least 3 example tasks saved for reuse

---

## Week 7: Minimal Coding Agent Workflow

### Objective

Connect the previous capabilities into one usable CLI workflow.

### Concepts

- task flow
- planning
- execution sequence
- user approval

### Tasks

- Create one CLI entry point.
- Define a fixed workflow:
  1. read task
  2. inspect repo
  3. search relevant code
  4. read key files
  5. optionally run tests
  6. produce patch
  7. summarize result
- Add a lightweight plan output before action.
- Add flags like:
  - `--approve-run`
  - `--approve-patch`
- Test on `5` small fixed tasks.

### Suggested CLI Shape

You do not need to freeze the CLI yet, but aim for something like:

```bash
python main.py \
  --task "Find why tests fail and propose a patch" \
  --repo ./example_repo \
  --approve-run \
  --approve-patch
```

### Suggested Time Split

- `2h` integration
- `1h` CLI arguments
- `2h` test tasks

### Deliverables

- `main.py`
- `README.md`
- `notes/week7.md`

### Acceptance Criteria

- The full loop works on at least `3/5` tasks.
- The toolchain feels like one system, not scattered scripts.
- You can demo the workflow to another developer.

### Milestone

This is the first version that deserves the name `mini-coding-agent`.

### End-of-Week Check

- [ ] One command starts the workflow
- [ ] The workflow is understandable from logs or console output
- [ ] I can show the tool chain from task to patch

---

## Week 8: Tracing and Logs

### Objective

Make agent behavior inspectable and debuggable.

### Concepts

- run trace
- per-step logging
- failure taxonomy

### Tasks

- Record for each run:
  - input task
  - system prompt version
  - each model turn
  - each tool call
  - tool result summary
  - duration
  - token usage if available
- Generate a unique `run_id`.
- Save logs to disk.
- Create failure categories:
  - misunderstood task
  - wrong tool choice
  - incomplete tool output
  - context overload
  - invalid patch
- Review at least `5` failed runs.

### Suggested Log Structure

Save one log file per run. Include fields like:

```json
{
  "run_id": "run_001",
  "task": "Fix broken greeting test",
  "turns": [],
  "duration_seconds": 12.4,
  "result": "failed"
}
```

### Suggested Time Split

- `2h` structured logging
- `1h` file output
- `2h` failure review

### Deliverables

- `tracing.py`
- `logs/`
- `failure_taxonomy.md`
- `notes/week8.md`

### Acceptance Criteria

- You can replay a failed run from logs.
- You can classify the main failure mode.
- You have enough visibility to debug behavior changes.

### Reflection Questions

- Did the model fail, or did the tools fail it?
- Are failures clustered around certain task types?
- What information would have prevented the failure?

### End-of-Week Check

- [ ] Every run has a stable identifier
- [ ] I can inspect a failed run without rerunning it
- [ ] I have a first failure taxonomy, even if rough

---

## Week 9: Basic Evals

### Objective

Start measuring progress using tasks, not intuition.

### Concepts

- benchmark tasks
- pass/fail
- regression
- baseline

### Tasks

- Build a set of `10-20` representative tasks.
- For each task, define:
  - description
  - repo
  - expected result
  - whether commands are needed
  - how success is judged
- Create a simple scoring format:
  - success or failure
  - step count
  - duration
  - approximate cost
  - failure reason
- Run a baseline evaluation manually or semi-automatically.
- Save results in a stable format.

### Suggested Task Mix

Try to include a mix like:

- `3-5` repo navigation tasks
- `3-5` bug localization tasks
- `2-4` patch proposal tasks
- `2-4` test-analysis tasks

### Suggested Time Split

- `2h` task design
- `1h` scoring format
- `2h` baseline run

### Deliverables

- `eval/tasks.json`
- `eval/run_eval.py`
- `eval/baseline.md`
- `notes/week9.md`

### Acceptance Criteria

- You have a baseline score for your agent.
- You can compare two versions of prompts or tools.
- You stop relying only on demo success.

### Stretch Goal

- Add a small CSV or markdown report generator.

### End-of-Week Check

- [ ] I have a saved baseline result
- [ ] I can compare versions using the same tasks
- [ ] I have at least one known weak category

---

## Week 10: Context Management and Working Memory

### Objective

Reduce instability caused by growing context.

### Concepts

- working memory
- summary memory
- selective context loading
- context compression

### Tasks

- Classify context into:
  - persistent rules
  - task-specific context
  - recent tool results
- Summarize long tool outputs before reusing them.
- Keep only the most relevant recent information in each turn.
- Avoid loading large files unless needed.
- Compress long logs into concise summaries plus key snippets.
- Compare long-task behavior before and after context management.

### Suggested Memory Buckets

Use three buckets from the start:

- `rules`: stable instructions and boundaries
- `working_state`: current task facts and current hypothesis
- `recent_observations`: last tool results and summaries

### Suggested Time Split

- `2h` memory design
- `2h` summarization logic
- `1h` long-task comparison

### Deliverables

- `context_manager.py`
- `memory_notes.md`
- `notes/week10.md`

### Acceptance Criteria

- Long tasks degrade less than before.
- The agent repeats file reads less often.
- You can explain when to preload vs retrieve on demand.

### Reflection Questions

- What information is useful across many turns?
- What information becomes noise quickly?
- Which failures are actually context failures?

### End-of-Week Check

- [ ] I can show what goes into context on each turn
- [ ] I have reduced repeated large file loads
- [ ] I can identify at least one improvement from context compression

---

## Week 11: MCP Fundamentals

### Objective

Understand how agents can extend capabilities through standardized external tooling.

### Concepts

- MCP host
- MCP client
- MCP server
- tools
- resources
- prompts

### Tasks

- Read the MCP architecture overview.
- Write your own short explanation of MCP.
- Draw a diagram showing host, client, and server relationships.
- Compare:
  - local function tools
  - MCP tools
- If possible, test one simple MCP server or inspect an example.
- Note when MCP is useful and when it is unnecessary.

### Suggested Output For This Week

Aim to leave the week with:

- a one-page MCP explanation
- one architecture diagram
- one list of practical use cases
- one note on when you would not use MCP

### Suggested Time Split

- `2h` reading
- `1h` diagramming
- `1-2h` simple example or note writing

### Deliverables

- `notes/week11.md`
- `mcp_architecture_diagram.md`
- `mcp_poc.md`

### Acceptance Criteria

- You can explain MCP clearly to another developer.
- You understand the difference between local tools and MCP-based tools.
- You can identify at least `2-3` real cases where MCP would help.

### Reflection Questions

- When is local code enough?
- When does standardization become valuable?
- What tradeoffs does MCP introduce?

### End-of-Week Check

- [ ] I understand MCP at the architecture level
- [ ] I can compare MCP vs local tools without vague language
- [ ] I can name one integration idea relevant to my work

---

## Week 12: Basic RAG for Coding Context

### Objective

Let the coding agent retrieve information from docs outside the codebase.

### Concepts

- retrieval
- document chunking
- relevance
- grounded answering

### Tasks

- Collect a small document set:
  - README
  - design notes
  - API docs
  - FAQ
- Build a very simple retrieval pipeline.
- Start with a minimal flow:
  1. user asks a question
  2. retrieve relevant chunks
  3. pass chunks into the model
  4. answer with grounding
- Expose retrieval as a tool for the coding agent.
- Test on tasks where the answer is in docs, not code.

### Suggested First Retrieval Scope

Do not start with a large knowledge base. Start with:

- one README
- one design note
- one API reference
- one FAQ or troubleshooting document

### Suggested Time Split

- `1h` document prep
- `2h` retrieval prototype
- `1h` tool wiring
- `1h` evaluation

### Deliverables

- `doc_retriever.py`
- `docs_corpus/`
- `notes/week12.md`

### Acceptance Criteria

- The agent can answer doc-based questions better than without retrieval.
- It can include evidence from retrieved material.
- You understand why RAG is useful here, instead of treating it as a default feature.

### Stretch Goal

- Compare naive keyword retrieval vs vector-based retrieval.

### End-of-Week Check

- [ ] The agent can answer at least one doc-only question
- [ ] Retrieved evidence is visible in the answer or logs
- [ ] I understand the difference between retrieval and memory

---

## Recommended Reading Order

Use these resources progressively instead of reading everything at once.

### Core Build Phase

- OpenAI Tools Guide
- OpenAI Agents SDK Quickstart
- Anthropic: Building Effective AI Agents
- Anthropic: Writing effective tools for agents

### Stability and Measurement Phase

- OpenAI Agent Evals
- Anthropic: Effective context engineering for AI agents

### Extension Phase

- MCP Architecture Overview
- OpenAI File Search
- OpenAI Cookbook RAG orchestration

### Theory Support

- Understanding the planning of LLM agents: A survey
- A Survey on RAG Meeting LLMs

---

## Suggested Deliverable Schedule

If you want a compact project roadmap, use this:

| Week | Main output | Why it matters |
|---|---|---|
| 1 | 3 tiny scripts | understand core API behavior |
| 2 | agent loop | first real agent mechanism |
| 3 | better prompts and tools | stability improvement |
| 4 | repo inspection tools | coding context begins |
| 5 | command runner | environment feedback |
| 6 | patch generator | proposal capability |
| 7 | CLI workflow | first usable coding agent |
| 8 | traces and logs | debugging foundation |
| 9 | eval baseline | measurable progress |
| 10 | context manager | long-task stability |
| 11 | MCP notes or POC | extensibility understanding |
| 12 | retriever tool | doc-grounded answers |

## Scope Control Rules

If the project starts expanding too quickly, apply these rules:

- Do not add a new tool unless an existing task clearly needs it.
- Do not add a framework unless hand-written code is becoming harder to reason about.
- Do not add memory until logs show context overload.
- Do not add RAG until at least one task fails because the answer is outside the code.
- Do not add multi-agent orchestration in this 12-week plan.

## Optional Stretch Track

Only consider these after the base plan is working:

- add a simple web UI
- add structured patch application
- add prompt versioning
- add eval reports with charts
- compare two model providers
- compare local search vs retrieval search

## If You Only Have 4-5 Hours Per Week

Use this reduced mode:

- Skip most stretch goals.
- Reduce task count from `3-5` to `2-3`.
- Stretch the plan to `16-20` weeks if needed.
- Keep the sequence the same: loop, repo, run, patch, trace, eval, context, MCP, RAG.

## If You Finish Early

Use extra time to:

- clean up abstractions
- improve logging quality
- expand the eval set
- compare prompts on the same tasks
- document tradeoffs you discovered

## Final Advice

The best version of this plan is the one you actually run. Keep the system small enough that you can explain every important part of it, including where it fails.

---

## Suggested Repository Layout

```text
mini-coding-agent/
├── main.py
├── agent_loop.py
├── tools.py
├── repo_tools.py
├── command_runner.py
├── patch_generator.py
├── context_manager.py
├── tracing.py
├── doc_retriever.py
├── prompt_v1.md
├── prompt_v2.md
├── README.md
├── notes/
├── logs/
├── eval/
└── examples/
```

---

## Progress Tracking Template

Use this checklist every week.

### Week Checklist

- [ ] I finished the reading for this week
- [ ] I implemented the planned capability
- [ ] I tested at least `3` tasks
- [ ] I recorded failures
- [ ] I wrote a short weekly note

### Weekly Note Template

```md
# Week N

## What I built

## What worked

## What failed

## Biggest lesson

## What I will change next week
```

---

## Final Self-Assessment

At the end of Week 12, you should be able to answer yes to most of these:

- [ ] I can explain the difference between an LLM app and an agent.
- [ ] I can implement a tool-calling loop from scratch.
- [ ] I can design tools that are usable by an agent.
- [ ] I can let an agent inspect a repo safely.
- [ ] I can let an agent run limited commands safely.
- [ ] I can generate and review simple patches.
- [ ] I can trace and debug agent failures.
- [ ] I can evaluate changes using a task set.
- [ ] I understand context management tradeoffs.
- [ ] I can explain MCP at a practical level.
- [ ] I can build a minimal RAG workflow for documentation.

## What Not To Do Too Early

Avoid these until the single-agent foundation is solid:

- multi-agent orchestration
- browser automation
- autonomous git operations
- long-term memory systems
- large vector infrastructure
- framework-heavy abstractions before you understand the loop

## One-Sentence Summary

The goal is not to build a flashy agent quickly; the goal is to build a small agent that you understand deeply enough to improve deliberately.
