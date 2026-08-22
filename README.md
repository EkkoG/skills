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

Install interactively with the Skills CLI:

```bash
npx skills add EkkoG/skills
```

Add `-g` to install at user scope instead of the current project:

```bash
npx skills add EkkoG/skills -g
```

For manual installation, clone the repository and copy the skills into the
user-level Codex skills directory:

```bash
git clone https://github.com/EkkoG/skills.git ekko-skills
cd ekko-skills
mkdir -p "$HOME/.agents/skills"
for skill in commit deliver-with-evidence design-delivery-plan markitdown; do
  rsync -a --delete "skills/$skill/" "$HOME/.agents/skills/$skill/"
done
```

For repository-scoped use, copy or link the desired skill directories under
`<repo>/.agents/skills/` instead. Codex detects skill changes automatically; if
an update does not appear, restart Codex.

See the official OpenAI documentation for
[building and installing skills](https://learn.chatgpt.com/docs/build-skills).

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
skills/
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

使用 Skills CLI 进行交互式安装：

```bash
npx skills add EkkoG/skills
```

增加 `-g` 可以安装到用户级范围，而不是当前项目：

```bash
npx skills add EkkoG/skills -g
```

如需手工安装，可以克隆仓库并将 skill 复制到用户级 Codex skill 目录：

```bash
git clone https://github.com/EkkoG/skills.git ekko-skills
cd ekko-skills
mkdir -p "$HOME/.agents/skills"
for skill in commit deliver-with-evidence design-delivery-plan markitdown; do
  rsync -a --delete "skills/$skill/" "$HOME/.agents/skills/$skill/"
done
```

如果只希望在某个仓库中使用，可以把所需 skill 复制或链接到
`<repo>/.agents/skills/`。Codex 会自动检测 skill 变化；如果更新没有出现，请重启
Codex。

更多信息参见 OpenAI 官方文档：
[创建和安装 Skill](https://learn.chatgpt.com/docs/build-skills)。

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
skills/
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
