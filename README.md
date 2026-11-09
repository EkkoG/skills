# Ekko Skills

English | [简体中文](#zh-cn)

Reusable Codex skills for focused Git commits, Markdown conversion, and
evidence-driven planning and delivery of multi-step engineering work.

## Included Skills

| Skill | Purpose |
|---|---|
| `commit` | Inspects local changes and creates focused, reviewable Git commits. |
| `design-delivery-plan` | Creates approval-ready plans with evidence-backed goals, dependency-ordered Work Packages, and proportional acceptance conditions; reports evidence gaps instead of inventing missing system facts. |
| `deliver-with-evidence` | Executes approved plans through reviewable Slices, maintains a private persistent Delivery document, and verifies Work Package and whole-Goal completion separately. |
| `markitdown` | Converts local files, standard input, and public web pages to Markdown. |

## Planning and Delivery Workflow

1. Use `$design-delivery-plan` to inspect a complex engineering goal and draft
   an approval-ready plan.
2. Review and explicitly approve the Goal, boundaries, Work Packages, and
   acceptance conditions.
3. Use `$deliver-with-evidence` to initialize a private persistent Delivery
   document before the first production edit, then select and execute the next
   reviewable Slice from the current code and evidence.
4. Repeat until Milestone and Final acceptance prove the whole Goal complete.

Plans define stable outcomes and constraints; they do not predefine every
future Slice. The delivery skill chooses Slices at runtime and records why the
current Slice was selected, what it covers, and what proves it complete. If
material current-state evidence is unavailable, the planning skill reports the
evidence gap instead of presenting an approval-ready plan based on assumptions.

## Installation

For `commit` and `markitdown`, use the Skills CLI and select these two skills:

```bash
npx skills add EkkoG/skills
```

Add `-g` to install at user scope instead of the current project:

```bash
npx skills add EkkoG/skills -g
```

Install `design-delivery-plan` and `deliver-with-evidence` in the Codex directory
`${CODEX_HOME:-$HOME/.codex}/skills/`. Install `commit` and `markitdown` in the
shared directory `$HOME/.agents/skills/`:

```bash
git clone https://github.com/EkkoG/skills.git ekko-skills
cd ekko-skills
codex_skills_dir="${CODEX_HOME:-$HOME/.codex}/skills"
mkdir -p "$codex_skills_dir" "$HOME/.agents/skills"
for skill in design-delivery-plan deliver-with-evidence; do
  rsync -a --delete "skills/$skill/" "$codex_skills_dir/$skill/"
done
for skill in commit markitdown; do
  rsync -a --delete "skills/$skill/" "$HOME/.agents/skills/$skill/"
done
```

For repository-scoped use of `commit` and `markitdown`, copy or link them under
`<repo>/.agents/skills/`. Restart Codex if a skill does not appear after installation.

See the official OpenAI documentation for
[building and installing skills](https://learn.chatgpt.com/docs/build-skills).

## Repository Maintenance

Preview changes from the local Codex skills, agents, and user instructions:

```bash
./scripts/sync-skills.sh --dry-run
```

Mirror the four maintained skills, agent role configurations, and user-level
`AGENTS.md` into this repository. Full sync is the default; `--full` selects it
explicitly:

```bash
./scripts/sync-skills.sh --full
```

Full sync mirrors complete agent TOML files, including `model`,
`model_reasoning_effort`, permissions, and instructions. The configured local
source is authoritative for these maintained files. Remote synchronization uses
the same full mode: mirror all four maintained skills, all agent files, and
`user-AGENTS.md` into their installed locations and verify the complete maintained
file set and contents. Repository instructions in `AGENTS.md` define this default.

The script reads skills from `${CODEX_SKILLS_DIR}`, `${CODEX_HOME}/skills`, or
`$HOME/.codex/skills`, and agent roles from `${CODEX_AGENTS_DIR}`,
`${CODEX_HOME}/agents`, or `$HOME/.codex/agents`. Use `--source <dir>` or
`--agents-source <dir>` for a one-time override. It never copies `.system` and
removes `__pycache__/` and `*.pyc` artifacts from mirrored directories.

User instructions come from `${CODEX_HOME}/AGENTS.md` or `$HOME/.codex/AGENTS.md`
and are stored as `user-AGENTS.md`. Use `--instructions-source <file>` to override
the source. This filename keeps the snapshot separate from repository-scoped
instructions. Review it for private or machine-specific content before publishing
or merging it into another machine's user-level `AGENTS.md`.

The script updates this repository only. Remote installation is a separate step;
`config.toml`, credentials, plans, Delivery records, and sessions are not mirrored.

## Usage

Invoke a skill explicitly:

```text
Use $commit to create a focused commit for the current changes.
```

```text
Use $design-delivery-plan to create an approval-ready plan for this refactor.
```

```text
Use $deliver-with-evidence to execute the approved plan.
```

```text
Use $markitdown to convert this document to Markdown.
```

These skills also allow implicit invocation when the request matches their
declared scope.

## Repository Structure

```text
.
├── user-AGENTS.md
├── agents/
│   ├── challenger.toml
│   ├── explorer.toml
│   ├── final_reviewer.toml
│   ├── implementation_reviewer.toml
│   ├── plan_challenger.toml
│   └── plan_reviewer.toml
├── scripts/
│   └── sync-skills.sh
└── skills/
    ├── commit/
    │   ├── SKILL.md
    │   └── agents/openai.yaml
    ├── deliver-with-evidence/
    │   ├── SKILL.md
    │   ├── agents/openai.yaml
    │   └── references/
    ├── design-delivery-plan/
    │   ├── SKILL.md
    │   ├── agents/openai.yaml
    │   └── references/plan-template.md
    └── markitdown/
        ├── SKILL.md
        └── agents/openai.yaml
```

<a id="zh-cn"></a>

## 简体中文

这是一组可复用的 Codex skill，用于创建聚焦的 Git 提交、转换 Markdown，以及基于
证据规划和实施多步骤工程任务。

### 包含的 Skill

| Skill | 用途 |
|---|---|
| `commit` | 检查本地改动并创建聚焦、便于 Review 的 Git 提交。 |
| `design-delivery-plan` | 制定可供审批的计划，基于证据明确目标、按依赖排序的 Work Package 和适度的验收条件；证据不足时报告缺口，而不是虚构系统事实。 |
| `deliver-with-evidence` | 通过可 Review 的 Slice 执行已批准计划，维护私有、持久的 Delivery document，并分别验收 Work Package 和整个 Goal。 |
| `markitdown` | 将本地文件、标准输入和公开网页转换为 Markdown。 |

### 规划与交付流程

1. 使用 `$design-delivery-plan` 检查复杂工程目标并制定可供审批的计划。
2. Review 并明确批准 Goal、边界、Work Package 和验收条件。
3. 使用 `$deliver-with-evidence`，在首次修改生产内容前初始化私有、持久的
   Delivery document，再根据当前代码和证据选择并执行下一个可独立 Review 的
   Slice。
4. 重复执行，直到 Milestone 和 Final 验收证明整个 Goal 已经完成。

计划负责固定稳定的结果与约束，不预先拆死所有未来 Slice。交付 skill 在运行时选择
Slice，并记录为什么选择当前 Slice、它覆盖哪些条件，以及什么证据可以证明它完成。
如果缺少关键的当前状态证据，规划 skill 会报告证据缺口，而不是基于假设提交可供审批
的完整计划。

### 安装

对于 `commit` 和 `markitdown`，可使用 Skills CLI 交互式安装并选择这两个 skill：

```bash
npx skills add EkkoG/skills
```

增加 `-g` 可以安装到用户级范围，而不是当前项目：

```bash
npx skills add EkkoG/skills -g
```

将 `design-delivery-plan` 和 `deliver-with-evidence` 安装到 Codex 专用目录
`${CODEX_HOME:-$HOME/.codex}/skills/`；将 `commit` 和 `markitdown` 安装到
共享目录 `$HOME/.agents/skills/`：

```bash
git clone https://github.com/EkkoG/skills.git ekko-skills
cd ekko-skills
codex_skills_dir="${CODEX_HOME:-$HOME/.codex}/skills"
mkdir -p "$codex_skills_dir" "$HOME/.agents/skills"
for skill in design-delivery-plan deliver-with-evidence; do
  rsync -a --delete "skills/$skill/" "$codex_skills_dir/$skill/"
done
for skill in commit markitdown; do
  rsync -a --delete "skills/$skill/" "$HOME/.agents/skills/$skill/"
done
```

如果只希望在某个仓库中使用 `commit` 和 `markitdown`，可以将它们复制或链接到
`<repo>/.agents/skills/`。安装后若未显示 skill，请重启 Codex。

更多信息参见 OpenAI 官方文档：
[创建和安装 Skill](https://learn.chatgpt.com/docs/build-skills)。

### 仓库维护

预览本地 Codex skills、agents 和用户级指令与仓库之间的差异：

```bash
./scripts/sync-skills.sh --dry-run
```

将维护的四个 skill、agent 角色配置和用户级 `AGENTS.md` 镜像到本仓库。
默认采用全量同步，也可以用 `--full` 显式指定：

```bash
./scripts/sync-skills.sh --full
```

全量同步完整复制 agent TOML，包括 `model`、`model_reasoning_effort`、权限和提示词，
这些维护文件以指定的本机来源为准。同步远端时也采用全量模式：将四个维护的 skill、
全部 agent 文件和 `user-AGENTS.md` 镜像到对应安装位置，并校验整个维护范围的文件
集合及内容。仓库级 `AGENTS.md` 记录这一默认约定。

脚本从 `${CODEX_SKILLS_DIR}`、`${CODEX_HOME}/skills` 或
`$HOME/.codex/skills` 读取 skill，并从 `${CODEX_AGENTS_DIR}`、
`${CODEX_HOME}/agents` 或 `$HOME/.codex/agents` 读取 agent 角色。可以用
`--source <dir>` 或 `--agents-source <dir>` 临时指定来源。脚本不会复制 `.system`，
并会从镜像目录中清理 `__pycache__/` 和 `*.pyc` 文件。

用户级指令来自 `${CODEX_HOME}/AGENTS.md` 或 `$HOME/.codex/AGENTS.md`，保存为
`user-AGENTS.md`，可用 `--instructions-source <file>` 覆盖来源。该文件名将同步
副本与仓库自身的指令区分开。发布或合并到其他机器的用户级 `AGENTS.md` 前，
应检查是否包含私密或机器专属内容。

脚本只更新本仓库，远端安装单独执行；不会镜像 `config.toml`、凭据、计划、
Delivery 记录或会话数据。

### 调用

可以显式调用任意 skill：

```text
Use $commit to create a focused commit for the current changes.
```

```text
Use $design-delivery-plan to create an approval-ready plan for this refactor.
```

```text
Use $deliver-with-evidence to execute the approved plan.
```

```text
Use $markitdown to convert this document to Markdown.
```

当请求与声明的适用范围匹配时，这些 skill 也允许被隐式调用。

### 仓库结构

```text
.
├── user-AGENTS.md
├── agents/
│   ├── challenger.toml
│   ├── explorer.toml
│   ├── final_reviewer.toml
│   ├── implementation_reviewer.toml
│   ├── plan_challenger.toml
│   └── plan_reviewer.toml
├── scripts/
│   └── sync-skills.sh
└── skills/
    ├── commit/
    │   ├── SKILL.md
    │   └── agents/openai.yaml
    ├── deliver-with-evidence/
    │   ├── SKILL.md
    │   ├── agents/openai.yaml
    │   └── references/
    ├── design-delivery-plan/
    │   ├── SKILL.md
    │   ├── agents/openai.yaml
    │   └── references/plan-template.md
    └── markitdown/
        ├── SKILL.md
        └── agents/openai.yaml
```
