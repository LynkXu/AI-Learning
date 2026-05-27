# 12 周 AI Agent 学习计划

## 目标

在 12 周内从零做出一个最小但可用的 coding agent，同时系统掌握现代 AI agent 的核心工程要素：

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

这份计划面向这样的人：

- 已有通用编程经验
- 对 Python 和终端不陌生
- 学过一点机器学习或神经网络
- 但还没有亲手构建过 AI agent

## 原则

整个 12 周都遵循这几条原则：

1. 先做，再补理论。优先做出小而可运行的系统，而不是停留在概念层面。
2. 先做单 agent。不要太早引入 multi-agent。
3. 用真实任务学习。尽量基于接近你工作场景的 coding task。
4. 用记录推动进步。保留日志、任务结果和失败笔记。
5. 只有当当前版本明显受限时，才增加复杂度。

## 推荐技术栈

- 语言：`Python`
- 交互方式：`CLI`
- 主项目名：`mini-coding-agent`
- 模型：任意支持 function/tool calling 的模型
- 搜索工具：`rg`
- 测试任务来源：一个小型 demo repo，或者你自己的 side project

## 开始前准备

在第 1 周开始前把这些准备好，避免后面把时间浪费在环境问题上。

### 前置能力

- 熟悉基础 Python
- 能正常使用终端
- 理解 JSON 的基本结构
- 对 HTTP API 有基础认知
- 手上有一个愿意拿来做实验的小 repo

### 环境准备清单

- [x] 安装 `Python 3.10+`
- [x] 创建并激活虚拟环境
- [x] 安装基础依赖，例如：
  - `openai` 或其他模型 SDK
  - `pydantic`
  - `rich`
  - `pytest`
- [x] 确认本机安装了 `rg`
- [x] 准备 `.env` 或其他加载密钥的方式
- [x] 准备一个测试用 repo
- [x] 创建这些目录：
  - `notes/`
  - `logs/`
  - `eval/`
  - `examples/`

### 从一开始就建议遵守的工程规则

- prompt 放在文件里，不要只写死在源码中
- 每次 run 都记录日志，哪怕只是早期原型
- 不要给 agent 无限制 shell 权限
- 能用确定性代码完成的事，就不要强行交给模型
- prompt 修改后做版本记录

## 每周时间预算

建议每周投入：`6-10` 小时

- `2-3h` 阅读和记笔记
- `3-5h` 编码实现
- `1-2h` 测试和复盘

## 每周固定节奏

每周都重复下面的节奏：

1. 阅读 `1-2` 篇核心资料
2. 实现 `1` 个具体能力
3. 用 `3-5` 个真实任务测试
4. 记录失败和下一步动作

### 推荐的周内拆分

如果你想有一个默认节奏，可以这样分：

- 第 1 天：阅读和做笔记
- 第 2 天：实现核心能力
- 第 3 天：补 bug 和整理代码
- 第 4 天：在真实任务上测试
- 第 5 天：写复盘，定义下周重点

### 每周复盘时都问自己

- 这周做出的东西，哪些是真正可复用的？
- 这周我更理解了 agent 的哪些限制？
- 是模型能力不足，还是工具设计不好？
- 现在系统里最难 debug 的部分是什么？

## 项目最终产出

到第 12 周结束时，你应该拥有：

- 一个最小版 coding agent
- 一套 repo 读取工作流
- 一个受控命令执行器
- 基础 patch 生成能力
- 运行日志和 trace
- 一套小型 eval 任务集
- 基础 context 管理机制
- 对 MCP 的实践级理解或一个简单 POC
- 一个最小文档检索能力

## 里程碑

可以把 12 周拆成这些关键节点：

- 第 2 周结束：tool-calling loop 跑通
- 第 4 周结束：agent 能看懂一个 repo
- 第 6 周结束：agent 能产出 patch
- 第 7 周结束：出现第一个端到端 coding agent demo
- 第 9 周结束：有第一版 eval baseline
- 第 10 周结束：context 管理不再是 naive 方案
- 第 12 周结束：agent 能使用代码外文档

## 什么时候应该放慢节奏

如果某一周明显吃不下，不要机械推进。下面这些情况出现时，应该缩小范围甚至重复一周：

- 你还讲不清自己的 loop
- 工具输出仍然经常不可用
- 日志差到无法解释失败
- 你没法判断一次修改到底变好了还是变差了

这时最好的做法不是硬上新功能，而是回到当前层级把基础补稳。

---

## 第 1 周：LLM 应用基础

### 本周目标

先搞懂现代 LLM 应用的最小组成，再进入 agent。

### 重点概念

- `messages`
- `system prompt`
- `structured output`
- `tool calling`
- `streaming`
- `token usage`
- `cost`

### 具体任务

- 配好一个模型提供方的 API 访问
- 写一个最小脚本：发送一句用户输入并打印模型回答
- 写一个要求返回固定 JSON 的脚本
- 写一个演示单工具调用的脚本
- 把原始请求和响应打印成便于阅读的格式
- 记录你自己对下列概念的解释：
  - model
  - tool
  - agent

### 建议时间拆分

- `1h` 环境和 API 配置
- `2h` 完成前两个脚本
- `1h` structured output 和 tool call
- `1h` 记笔记和整理

### 建议参考资料

- 必读：[OpenAI Developer Quickstart](https://platform.openai.com/docs/quickstart)；先把最小请求跑通。
- 必读：[OpenAI Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)；理解“合法 JSON”和“符合 schema”不是一回事。
- 选读：[OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling)；为第 2 周的 loop 做准备。

### 建议小练习

- 让模型直接回答一个问题
- 让模型按严格字段输出 JSON
- 让模型判断是否需要调用计算器工具

### 本周产出

- `src/mini_coding_agent/chat_basic.py`
- `src/mini_coding_agent/structured_output.py`
- `src/mini_coding_agent/single_tool.py`
- `notes/week1.md`

### 验收标准

- 你能解释模型不会直接执行工具
- 你能解释为什么 agent 需要控制循环
- 你能把一次 tool call 端到端跑通

### 反思问题

- 模型自己知道什么？
- 哪些事必须由你的程序完成？
- 如果模型输出不稳定，会先坏在哪一层？

### 常见失败模式

- JSON 不合法
- 工具参数缺字段
- 脚本只能跑一次，复用性很差
- 打印信息过于混乱，无法排查问题

### 周末检查

- [ ] 这 3 个脚本都能稳定运行
- [ ] 我能讲清模型和应用代码的边界

---

## 第 2 周：最小 Agent Loop

### 本周目标

从“单次模型调用”进入“最小 agent 循环”。

### 重点概念

- tool loop
- stop condition
- final answer
- max turns

### 具体任务

- 设计一个循环，直到任务完成才退出
- 支持三种结果：
  - 直接 final answer
  - 请求调用工具
  - 超过最大轮数后强制停止
- 增加 `2-3` 个安全工具：
  - `get_time`
  - `echo_text`
  - `read_text_file`
- 设计工具注册格式
- 在控制台打印每一轮行为
- 为非法工具调用增加基础错误处理

### 建议时间拆分

- `2h` 设计 loop 结构
- `2h` 接工具注册和执行
- `1h` 停止条件和日志

### 建议参考资料

- 必读：[Anthropic Tool Use Overview](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview)；看清 tool call / tool result 的基本循环。
- 必读：[OpenAI Conversation State](https://platform.openai.com/docs/guides/conversation-state)；理解多轮状态到底由谁保存。
- 选读：[OpenAI Using Tools](https://platform.openai.com/docs/guides/tools)；补齐内置工具和自定义工具的整体视图。

### 建议内部数据结构

你不必完全照抄，但建议尽早固定一种结构：

```python
ToolDefinition = {
    "name": "read_text_file",
    "description": "Read a UTF-8 text file from a safe path.",
    "input_schema": {...},
    "handler": read_text_file,
}
```

### 本周产出

- `src/mini_coding_agent/agent_loop.py`
- `src/mini_coding_agent/tools.py`
- `notes/week2.md`

### 验收标准

- agent 能完成多轮工具调用
- loop 能稳定停止
- final answer 和工具执行过程是分开的

### 练习任务

- “现在几点”
- “读取这个文件并总结”
- “先 echo 这句话，再解释你收到的内容”

### 常见失败模式

- loop 不退出
- tool result 格式不利于模型继续使用
- prompt 里的工具名和代码里的工具名不一致

### 周末检查

- [ ] 我能演示一个多步 tool call
- [ ] 我有最大轮数限制
- [ ] 我能解释 loop 为什么停下

---

## 第 3 周：Prompt 与工具设计

### 本周目标

通过更好的 prompt 和 tool design 提升稳定性。

### 重点概念

- tool ergonomics
- tool descriptions
- parameter design
- narrow tools vs broad tools
- instruction quality

### 具体任务

- 重写每个工具描述，让模型知道何时使用它
- 给工具参数增加类型和校验
- 重写系统提示，明确行为规则
- 对比：
  - 一个大而全的工具，如 `run_anything`
  - 多个窄工具，如 `read_file`、`search_code`、`run_tests`
- 写一份坏工具接口示例笔记
- 用相同任务对比旧 prompt / 旧工具描述 和新版本效果

### 建议时间拆分

- `1h` 重写 prompt
- `2h` 重写工具描述
- `1h` 对比实验
- `1h` 记笔记

### 建议参考资料

- 必读：[Anthropic Prompt Engineering Overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)；建立 prompt 调优的总框架。
- 必读：[OpenAI Prompting Guide](https://platform.openai.com/docs/guides/prompting)；补 prompt 版本化、变量和迭代方法。
- 选读：[Anthropic Chain Complex Prompts](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-prompts)；理解什么时候该拆 prompt，而不是继续堆指令。

### 建议使用对比表

在笔记里至少做一个这样的表：

| Prompt | 旧工具结果 | 新工具结果 | 是否更好 | 原因 |
|---|---|---|---|---|
| 查配置文件 | 选错工具 | 选对工具 | 是 | 描述更清晰 |

### 本周产出

- `prompt_v1.md`
- `prompt_v2.md`
- `tool_design_notes.md`
- `notes/week3.md`

### 验收标准

- tool selection 比第 2 周更稳定
- 你能解释为什么窄工具更适合 agent
- 你至少整理出 `5` 个坏接口或坏 prompt 示例

### 反思问题

- 哪些工具描述最容易让模型选错？
- 哪些指令减少了无意义 tool call？
- 现在模型还在哪些地方迷糊？

### 周末检查

- [ ] prompt 已经落成文件，不只是源码里的字符串
- [ ] 我能证明工具描述确实影响结果
- [ ] 我能指出一个本周最明确的提升点

---

## 第 4 周：只读代码库 Agent

### 本周目标

让 agent 从普通聊天助手变成只读代码助手。

### 重点概念

- file listing
- file reading
- code search
- context limits

### 具体任务

- 实现：
  - `list_files(path)`
  - `read_file(path)`
  - `search_code(query)`
- 搜索优先用 `rg`
- 给输出做截断，避免一次塞入太多文本
- 选一个小 repo 做练习
- 设计如下测试问题：
  - 入口文件在哪里
  - 某个函数在哪里定义
  - 某个路由在哪里注册
  - 配置是从哪里加载的

### 建议练习用 repo 大小

尽量选一个你能在 1 小时内大致看明白的仓库：

- 理想大小：`5-30` 个源码文件
- 最好单一语言
- 最好有明显入口文件

### 建议时间拆分

- `2h` 实现 repo 工具
- `1h` 做输出截断和格式化
- `2h` 测试问题和跑任务

### 建议参考资料

- 必读：[ripgrep User Guide](https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md)；这是代码搜索能力的底层工具手册。
- 必读：[Python pathlib](https://docs.python.org/3/library/pathlib.html)；用标准库把路径约束和文件读取写扎实。
- 选读：[Anthropic Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)；重点看简单、可组合、可验证的 agent 设计思路。

### 本周产出

- `src/mini_coding_agent/repo_tools.py`
- `test_repo_tasks.md`
- `notes/week4.md`

### 验收标准

- agent 至少能回答 `4/5` 个 repo 结构问题
- agent 能自动定位文件和符号
- 文件读取范围是受控的，不是见文件就整篇读

### Stretch Goal

- 给输出加行号

### 常见失败模式

- 整个文件全返回，噪音太大
- 搜索结果没有路径信息
- 输出太长，下一轮模型无法有效使用

### 周末检查

- [ ] 我可以基于 repo 提问结构性问题
- [ ] agent 能定位代码，不只是报文件名
- [ ] 文件读取已经是“按需”的，而不是“全读”

---

## 第 5 周：受控命令执行

### 本周目标

让 agent 可以安全地从环境获取反馈。

### 重点概念

- command whitelisting
- execution boundaries
- timeout
- output limits

### 具体任务

- 实现 `run_command(cmd)`
- 限制命令白名单，例如：
  - `pytest`
  - `rg`
  - `ls`
  - `cat`
- 限制 working directory 范围
- 增加 timeout
- 限制最大输出长度
- 处理这些常见失败：
  - command not found
  - non-zero exit code
  - timeout
  - oversized output
- 用简单失败测试用例验证

### 安全规则要写成文档

明确写出：

- 哪些命令允许
- 哪些命令禁止
- 允许在哪些目录运行
- 输出截断规则
- timeout 规则
- 是否允许联网

### 建议时间拆分

- `2h` 包装命令执行器
- `1h` 实现白名单
- `1h` 失败输出格式化
- `1h` 测试

### 建议参考资料

- 必读：[Python subprocess](https://docs.python.org/3/library/subprocess.html)；重点看 `run()`、`timeout` 和 security considerations。
- 必读：[Python shlex](https://docs.python.org/3/library/shlex.html)；用它做参数切分和最基础的命令解析。
- 选读：[OpenAI Safety in Building Agents](https://platform.openai.com/docs/guides/agent-builder-safety)；把 prompt injection 和工具滥用风险提前纳入设计。

### 本周产出

- `src/mini_coding_agent/command_runner.py`
- `command_policy.md`
- `notes/week5.md`

### 验收标准

- agent 能执行安全命令并利用结果
- agent 不能执行任意 shell
- 失败输出对模型来说是可读的

### 反思问题

- 哪些命令输出可以直接使用？
- 哪些输出必须先摘要？
- 还剩下哪些安全风险？

### 周末检查

- [ ] 任意 shell 输入已经被挡住
- [ ] 大输出不会淹没 agent
- [ ] 我知道哪些命令可信、为什么可信

---

## 第 6 周：Patch 生成

### 本周目标

让 agent 从“分析问题”进入“提出修改”。

### 重点概念

- patch
- diff
- change planning
- reviewability

### 具体任务

- 设计 patch 输出格式
- 二选一：
  - unified diff
  - 原文片段 -> 新片段替换
- 要求 agent 在输出 patch 前先解释要改什么
- 要求 agent 在输出 patch 后总结影响文件
- 用 `3` 类简单 bug 做测试：
  - 变量名拼写错误
  - 分支判断错误
  - 用户提示文本错误

### 建议时间拆分

- `2h` patch 格式
- `1h` 先解释后修改
- `2h` 用 bug case 测试

### 建议参考资料

- 必读：[git-diff 文档](https://git-scm.com/docs/git-diff)；理解 diff 的使用方式和输出边界。
- 必读：[diff-format 文档](https://git-scm.com/docs/diff-format)；理解 patch 文本长什么样，便于你自己做格式约束。
- 选读：[Anthropic Effective Harnesses for Long-Running Agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)；重点看“先验证、再提交答案”的工作流思想。

### Patch 审查清单

在接受 patch 前，至少检查：

- 目标文件对不对
- 修改范围是否够小且相关
- 解释是否和改动一致
- 是否出现明显无关修改

### 本周产出

- `src/mini_coding_agent/patch_generator.py`
- `examples/`
- `notes/week6.md`

### 验收标准

- agent 能为简单 bug 输出可读 patch
- 人能快速审核 patch
- reasoning 和 patch 内容保持一致

### Stretch Goal

- 增加 dry-run 模式，只预览不真正变更

### 周末检查

- [ ] agent 会先解释修复计划
- [ ] patch 足够稳定，能人工 review
- [ ] 我保存了至少 3 个可复用示例任务

---

## 第 7 周：最小 Coding Agent 工作流

### 本周目标

把前面 6 周的能力拼成一个可用 CLI 工作流。

### 重点概念

- task flow
- planning
- execution sequence
- user approval

### 具体任务

- 统一成一个 CLI 入口
- 定义固定流程：
  1. 读取任务
  2. 检查 repo
  3. 搜索相关代码
  4. 读取关键文件
  5. 必要时跑测试
  6. 生成 patch
  7. 输出总结
- 在执行前打印轻量计划
- 增加参数：
  - `--approve-run`
  - `--approve-patch`
- 用 `5` 个固定小任务测试

### 建议 CLI 形式

不需要立刻最终定型，但建议尽量接近这种形式：

```bash
PYTHONPATH=src python -m mini_coding_agent.main \
  --task "Find why tests fail and propose a patch" \
  --repo ./sandbox/example_repo \
  --approve-run \
  --approve-patch
```

### 建议时间拆分

- `2h` 整体集成
- `1h` CLI 参数
- `2h` 跑 5 个任务

### 建议参考资料

- 必读：[Python Argparse Tutorial](https://docs.python.org/3/howto/argparse.html)；先把 CLI 入口做得清楚、可解释、可复现。
- 必读：[OpenAI Agents SDK Guide](https://platform.openai.com/docs/guides/agents-sdk/)；不是要你立刻上 SDK，而是借它看成熟 agent workflow 都抽象了什么。
- 选读：[OpenAI Agents Best Practices](https://platform.openai.com/docs/guides/agents/best-practices)；对照自己的 CLI 工作流检查缺口。

### 本周产出

- `src/mini_coding_agent/main.py`
- `README.md`
- `notes/week7.md`

### 验收标准

- 在 `5` 个任务里至少成功完成 `3` 个
- 整体感觉是一个系统，而不是一堆散脚本
- 你可以把这个工作流演示给另一个开发者

### 里程碑

这是第一个真正称得上 `mini-coding-agent` 的版本。

### 周末检查

- [ ] 一个命令就能启动整个流程
- [ ] 通过控制台输出或日志可以看懂流程
- [ ] 我可以完整展示从任务到 patch 的路径

---

## 第 8 周：Tracing 和日志

### 本周目标

让 agent 的行为可以被回放、解释和调试。

### 重点概念

- run trace
- per-step logging
- failure taxonomy

### 具体任务

- 为每次运行记录：
  - 输入任务
  - system prompt 版本
  - 每轮模型输出
  - 每次工具调用
  - 工具结果摘要
  - 耗时
  - token 用量
- 生成唯一 `run_id`
- 把日志保存到磁盘
- 建立失败分类：
  - misunderstood task
  - wrong tool choice
  - incomplete tool output
  - context overload
  - invalid patch
- 复盘至少 `5` 次失败运行

### 建议日志结构

建议至少能存成类似下面的结构：

```json
{
  "run_id": "run_001",
  "task": "Fix broken greeting test",
  "turns": [],
  "duration_seconds": 12.4,
  "result": "failed"
}
```

### 建议时间拆分

- `2h` 做结构化日志
- `1h` 输出到文件
- `2h` 做失败复盘

### 建议参考资料

- 必读：[OpenAI Agents SDK Tracing](https://openai.github.io/openai-agents-python/tracing/)；直接看一个成熟 tracing 体系会记录什么。
- 必读：[OpenAI Trace Grading](https://platform.openai.com/docs/guides/trace-grading)；理解为什么仅有日志还不够，最好还能做结构化评估。
- 选读：[OpenTelemetry Traces](https://opentelemetry.io/docs/concepts/signals/traces/)；借标准术语整理 `trace`、`span`、`attributes` 的概念。

### 本周产出

- `src/mini_coding_agent/tracing.py`
- `logs/`
- `failure_taxonomy.md`
- `notes/week8.md`

### 验收标准

- 你能在不重跑的情况下回看一次失败 run
- 你能给主要失败模式贴标签
- 你对 agent 行为已经有足够可观测性

### 反思问题

- 是模型失败，还是工具把模型坑了？
- 失败是否集中在某些任务类型？
- 如果多给一点什么信息，本次失败可能避免吗？

### 周末检查

- [ ] 每次运行都有稳定 run_id
- [ ] 失败可以离线复盘
- [ ] 我已经有一个第一版 failure taxonomy

---

## 第 9 周：基础 Evals

### 本周目标

开始用任务集衡量 agent，而不是靠“演示感觉不错”。

### 重点概念

- benchmark tasks
- pass/fail
- regression
- baseline

### 具体任务

- 整理 `10-20` 个代表性任务
- 每个任务定义：
  - 描述
  - repo
  - 预期结果
  - 是否需要命令执行
  - 如何判定成功
- 设计评分格式：
  - success / failure
  - step count
  - duration
  - approximate cost
  - failure reason
- 手工或半自动跑出一版 baseline
- 把结果存成稳定格式

### 建议任务组合

尽量混合这些任务：

- `3-5` 个 repo 导航任务
- `3-5` 个 bug 定位任务
- `2-4` 个 patch 提议任务
- `2-4` 个测试分析任务

### 建议时间拆分

- `2h` 设计任务集
- `1h` 设计评分格式
- `2h` 跑 baseline

### 建议参考资料

- 必读：[OpenAI Evaluation Best Practices](https://platform.openai.com/docs/guides/evaluation-best-practices)；先把 eval 设计原则立住。
- 必读：[OpenAI Agent Evals](https://platform.openai.com/docs/guides/agent-evals)；看 agent 级别 eval 和普通 prompt eval 的差异。
- 选读：[Anthropic Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)；补多轮、工具型系统的评测视角。

### 本周产出

- `eval/tasks.json`
- `eval/run_eval.py`
- `eval/baseline.md`
- `notes/week9.md`

### 验收标准

- 你已经有一版 baseline 成绩
- 你可以拿同一任务集比较两个版本
- 你不再只依赖 demo 成功与否来判断进步

### Stretch Goal

- 增加 CSV 或 markdown 报告导出

### 周末检查

- [ ] baseline 结果已经保存
- [ ] 我可以在同一任务集上比较版本
- [ ] 我已经知道至少一个明显薄弱项

---

## 第 10 周：Context 管理与工作记忆

### 本周目标

解决“上下文越来越长，agent 越来越乱”的问题。

### 重点概念

- working memory
- summary memory
- selective context loading
- context compression

### 具体任务

- 把上下文分成三类：
  - persistent rules
  - task-specific context
  - recent tool results
- 对长工具输出做摘要再复用
- 每轮只保留最相关的信息
- 非必要不读取大文件
- 长日志只保留摘要和关键片段
- 对比优化前后的长任务表现

### 建议 Memory Buckets

从一开始就把上下文按三个桶管理：

- `rules`：稳定约束和规则
- `working_state`：当前任务事实和当前假设
- `recent_observations`：最近工具结果和摘要

### 建议时间拆分

- `2h` 设计 memory 结构
- `2h` 实现摘要逻辑
- `1h` 对比长任务表现

### 建议参考资料

- 必读：[Anthropic Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)；这是本周最值得精读的一篇。
- 必读：[OpenAI Conversation State](https://platform.openai.com/docs/guides/conversation-state)；重新回看状态管理，但这次从长任务稳定性角度看。
- 选读：[Anthropic Prompt Caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)；理解哪些上下文适合复用，哪些适合按需加载。

### 本周产出

- `src/mini_coding_agent/context_manager.py`
- `memory_notes.md`
- `notes/week10.md`

### 验收标准

- 长任务比之前更稳定
- agent 重复读取大文件的次数下降
- 你能解释 preload 和按需检索的取舍

### 反思问题

- 哪些信息适合跨多轮保留？
- 哪些信息很快就会变成噪音？
- 哪些失败本质上是 context failure？

### 周末检查

- [ ] 我可以说明每轮上下文里放了什么
- [ ] 大文件重复加载明显减少
- [ ] 我能指出至少一个 context compression 带来的提升

---

## 第 11 周：MCP 基础

### 本周目标

理解 agent 如何通过标准化协议扩展外部能力。

### 重点概念

- MCP host
- MCP client
- MCP server
- tools
- resources
- prompts

### 具体任务

- 阅读 MCP 架构总览
- 用你自己的话写一段 MCP 解释
- 画出 host / client / server 关系图
- 对比：
  - 本地 function tools
  - MCP tools
- 如果可能，跑一个简单 MCP server，或者至少研究一个例子
- 记录 MCP 有用和没必要使用的场景

### 建议本周最少产物

至少留下这些内容：

- 一页 MCP 解释
- 一张架构图
- 一份实际 use case 列表
- 一份“不该用 MCP”的说明

### 建议时间拆分

- `2h` 阅读
- `1h` 画图
- `1-2h` 看例子或做笔记

### 建议参考资料

- 必读：[MCP Architecture Overview](https://modelcontextprotocol.io/docs/learn/architecture)；先把 host / client / server 和 primitives 搞清楚。
- 必读：[Understanding MCP Servers](https://modelcontextprotocol.io/docs/learn/server-concepts)；重点理解 tools、resources、prompts 的职责边界。
- 选读：[MCP Inspector](https://modelcontextprotocol.io/docs/tools)；如果你真的跑例子，这会是最快的调试入口。

### 本周产出

- `notes/week11.md`
- `mcp_architecture_diagram.md`
- `mcp_poc.md`

### 验收标准

- 你可以把 MCP 讲给另一个程序员听
- 你理解本地工具和 MCP 工具的区别
- 你能指出 `2-3` 个对你工作有意义的 MCP 场景

### 反思问题

- 什么场景下本地代码就够了？
- 什么场景下标准化会开始值钱？
- MCP 带来了什么额外成本和约束？

### 周末检查

- [ ] 我已经理解 MCP 的架构层面
- [ ] 我可以不含糊地比较 MCP 和本地工具
- [ ] 我能说出一个跟自己工作相关的 MCP 集成想法

---

## 第 12 周：面向 Coding Context 的最小 RAG

### 本周目标

让 coding agent 能读取代码外部文档，而不只靠源码。

### 重点概念

- retrieval
- document chunking
- relevance
- grounded answering

### 具体任务

- 准备一个小文档集：
  - README
  - design notes
  - API docs
  - FAQ
- 做一个最小检索管线
- 先实现最简单流程：
  1. 用户提问
  2. 检索相关片段
  3. 把片段塞给模型
  4. 让回答带 grounding
- 把检索能力暴露成 coding agent 的一个工具
- 测试“答案在文档里、不在代码里”的任务

### 建议第一版检索范围

不要一开始做大知识库。先从下面这几种文档开始：

- 一个 README
- 一个设计文档
- 一个 API 参考
- 一个 FAQ 或 troubleshooting 文档

### 建议时间拆分

- `1h` 准备文档
- `2h` 做最小检索原型
- `1h` 接成工具
- `1h` 测试

### 建议参考资料

- 必读：[OpenAI Retrieval Guide](https://platform.openai.com/docs/guides/retrieval)；先理解向量检索和 vector store 的基本模型。
- 必读：[OpenAI File Search](https://platform.openai.com/docs/guides/tools-file-search)；看一个托管式检索工具如何暴露给模型使用。
- 选读：[OpenAI Cookbook: Multi-Tool Orchestration with RAG](https://cookbook.openai.com/examples/responses_api/responses_api_tool_orchestration)；参考一个把检索接进 agent workflow 的更完整例子。

### 本周产出

- `src/mini_coding_agent/doc_retriever.py`
- `sandbox/docs_corpus/`
- `notes/week12.md`

### 验收标准

- agent 对文档型问题的表现优于无检索版本
- 回答中或日志中能看到证据来源
- 你理解为什么这里需要 RAG，而不是把 RAG 当默认配置

### Stretch Goal

- 对比关键词检索和向量检索

### 周末检查

- [ ] agent 至少能答对一个纯文档问题
- [ ] 检索到的证据在答案或日志里是可见的
- [ ] 我理解 retrieval 和 memory 的区别

---

## 推荐阅读顺序

先按每周的“建议参考资料”读。这里保留一个跨周导航版本，方便你回头补读。

### 核心构建阶段

- 第 1-3 周：OpenAI Quickstart、Structured Outputs、Function Calling、Prompting Guide
- 第 2-3 周：Anthropic Tool Use、Prompt Engineering Overview
- 第 4-7 周：`rg` Guide、`pathlib`、`subprocess`、`git diff`、`argparse`

### 稳定性与测量阶段

- 第 8 周：Tracing、Trace Grading、OpenTelemetry Traces
- 第 9 周：Evaluation Best Practices、Agent Evals、Demystifying Evals for AI Agents
- 第 10 周：Effective Context Engineering、Conversation State、Prompt Caching

### 扩展阶段

- 第 11 周：MCP Architecture Overview、Understanding MCP Servers、MCP Inspector
- 第 12 周：Retrieval Guide、File Search、RAG Orchestration Cookbook

### 理论补充

- [Anthropic Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
- [Anthropic Effective Harnesses for Long-Running Agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- [Understanding the planning of LLM agents: A survey](https://arxiv.org/abs/2402.02716)
- [A Survey on RAG Meeting LLMs](https://arxiv.org/abs/2405.06211)

---

## 建议的交付节奏

如果你想看更紧凑的项目路线图，可以用这个表：

| 周数 | 主产物 | 价值 |
|---|---|---|
| 1 | 3 个最小脚本 | 理解 API 基础行为 |
| 2 | agent loop | 第一个真正的 agent 机制 |
| 3 | 更好的 prompt 和 tools | 稳定性提升 |
| 4 | repo 检查工具 | 开始有 coding context |
| 5 | command runner | 从环境拿反馈 |
| 6 | patch generator | 开始提出修改 |
| 7 | CLI workflow | 第一版可用 coding agent |
| 8 | traces 和 logs | debug 基础设施 |
| 9 | eval baseline | 可衡量进步 |
| 10 | context manager | 长任务稳定性 |
| 11 | MCP 笔记或 POC | 理解扩展机制 |
| 12 | retriever tool | 基于文档回答 |

## 控制范围的规则

如果项目开始膨胀过快，就强制自己遵守这些规则：

- 没有明确任务需求时，不新增工具
- 手写代码还可控时，不上重框架
- 没有看到 context overload 前，不急着做 memory
- 没有出现“答案在代码外部”的失败前，不急着做 RAG
- 这 12 周里不要上 multi-agent

## 可选 Stretch Track

只有当主线已经顺了，才考虑这些：

- 加一个简单 Web UI
- 支持结构化 patch 应用
- 增加 prompt versioning
- 导出图表化 eval 报告
- 对比两个模型提供方
- 对比本地搜索和 retrieval 搜索

## 如果你每周只有 4-5 小时

可以用缩减版策略：

- 大部分 stretch goal 直接跳过
- 每周测试任务从 `3-5` 个降到 `2-3` 个
- 必要时把计划拉长到 `16-20` 周
- 但顺序不要乱：loop、repo、run、patch、trace、eval、context、MCP、RAG

## 如果你提前完成

多出来的时间优先做这些：

- 清理抽象和代码结构
- 提升日志质量
- 扩展 eval 集
- 在同一任务集上比较 prompt
- 记录你发现的 tradeoff

## 最后建议

这份计划最好的版本，不是“看起来最完整”的版本，而是“你真的跑完”的版本。系统要保持足够小，小到你能清楚解释它的每个关键部分，也能解释它为什么失败。

---

## 建议的仓库结构

```text
mini-coding-agent/
├── README.md
├── Makefile
├── requirements.txt
├── docs/
│   ├── 12-week-ai-agent-plan.md
│   ├── 12-week-ai-agent-plan.zh-CN.md
│   ├── prompt_v1.md
│   └── prompt_v2.md
├── src/
│   └── mini_coding_agent/
│       ├── main.py
│       ├── agent_loop.py
│       ├── tools.py
│       ├── repo_tools.py
│       ├── command_runner.py
│       ├── patch_generator.py
│       ├── context_manager.py
│       ├── tracing.py
│       └── doc_retriever.py
├── sandbox/
│   ├── example_repo/
│   └── docs_corpus/
├── notes/
├── logs/
├── eval/
└── examples/
```

如果你在第 1 周先用根目录脚本快速起步，建议最晚在第 3-4 周把可复用代码移动到 `src/mini_coding_agent/`。

---

## 进度跟踪模板

每周都用这个 checklist。

### 每周 Checklist

- [ ] 本周阅读已完成
- [ ] 本周核心能力已实现
- [ ] 至少测试了 `3` 个任务
- [ ] 已记录失败
- [ ] 已写周记

### 每周周记模板

```md
# Week N

## What I built

## What worked

## What failed

## Biggest lesson

## What I will change next week
```

---

## 最终自检

到第 12 周结束时，理想状态下你能对下面多数问题打勾：

- [ ] 我能解释 LLM app 和 agent 的区别
- [ ] 我能从零实现 tool-calling loop
- [ ] 我能设计适合 agent 使用的工具
- [ ] 我能让 agent 安全地检查 repo
- [ ] 我能让 agent 安全地执行受限命令
- [ ] 我能生成并 review 简单 patch
- [ ] 我能 trace 和 debug agent 失败
- [ ] 我能用任务集评估变更
- [ ] 我理解 context management 的取舍
- [ ] 我能用实践角度解释 MCP
- [ ] 我能为文档场景做最小 RAG

## 不要过早做的事

在单 agent 基础稳之前，不要急着做这些：

- multi-agent orchestration
- browser automation
- autonomous git operations
- long-term memory systems
- large vector infrastructure
- 在没理解 loop 前就上重框架

## 一句话总结

目标不是尽快做一个看起来很炫的 agent，而是做一个足够小、足够清楚、足够可迭代的 agent，让你真的理解它是怎么工作的。
