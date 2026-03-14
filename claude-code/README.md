# Coding Agent

A **coding agent** is an AI system that can understand programming tasks, make a plan to solve them, and use tools (like reading files, writing code, or running commands) to complete the task automatically.

Unlike simple code assistants that only suggest code, a coding agent can **analyze problems, interact with the codebase, and take actions to fix or improve software**.

## In Simple Words

A coding agent is like a **smart programmer assistant** that can:

* Understand a problem
* Decide what steps are needed
* Use tools to read or change code
* Execute commands
* Provide a solution

## Key Idea

**AI brain + tools = coding agent**

![Tools with Claude Code](tools-with-cc.png)

---

# Claude Code Setup Guide

Full setup directions can be found here:
https://code.claude.com/docs/en/quickstart

## Prerequisites

Before installing Claude Code, make sure you have:

* **Node.js** v18 or later
* **npm** v9 or later (bundled with Node.js)
* A supported operating system: macOS 12+, Ubuntu 20.04+, Windows 10+ (via WSL or CMD)
* An **Anthropic account** — sign up at [claude.ai](https://claude.ai)

> **Note:** On Windows, WSL (Windows Subsystem for Linux) is strongly recommended for the best experience. Native CMD support is available but limited.

## Quick Installation

Below are the commands to install **Claude Code** depending on your operating system.

### MacOS (Homebrew)

```bash
brew install --cask claude-code
```

### MacOS, Linux, WSL

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

### Windows (CMD)

```cmd
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

## After Installation

Run **claude** at your terminal. The first time you run this command you will be prompted to authenticate.

### Ask your first questions

```bash
what does this project do?

what technologies does this project use?

where is the main entry point?

explain the folder structure
```

Ask Claude about its own capabilities:

```bash
what can Claude Code do?

how do I create custom skills in Claude Code?

can Claude Code work with Docker?
```

Make your first code change:

```bash
add a hello world function to the main file
```

Use Git with Claude Code:

```bash
what files have I changed?

commit my changes with a descriptive message

create a new branch called feature/quickstart

show me the last 5 commits

help me resolve merge conflicts
```

Fix a bug or add a feature:

```bash
add input validation to the user registration form

there's a bug where users can submit empty forms - fix it
```

Test out other common workflows:

```bash
refactor the authentication module to use async/await instead of callbacks
```

Write tests:

```bash
write unit tests for the calculator functions
```

Update documentation:

```bash
update the README with installation instructions
```

Code review:

```bash
review my changes and suggest improvements
```

---

# Configuration

## CLAUDE.md

Claude Code looks for a `CLAUDE.md` file in your project root. Use it to give Claude persistent context about your project — coding conventions, architecture notes, important commands, and anything else it should always know.

```markdown
# My Project

## Stack
- Backend: FastAPI (Python 3.11)
- Frontend: React + TypeScript
- Database: PostgreSQL

## Dev commands
- `make dev` — start local dev server
- `make test` — run test suite
- `make lint` — run linters

## Conventions
- All API routes live in `app/routes/`
- Use `snake_case` for Python, `camelCase` for TypeScript
- Every PR must include tests
```

Claude reads this file at the start of each session. The more specific it is, the less you need to repeat yourself.

## Settings File

Global settings are stored at `~/.claude/settings.json`. You can edit this directly or use the `claude config` command.

```json
{
  "model": "claude-sonnet-4-5",
  "theme": "dark",
  "auto_approve_tools": false,
  "max_tokens": 8192
}
```

Project-level settings can be placed in `.claude/settings.json` inside your repo and will override global settings when Claude Code is run from that directory.

---

# MCP Server Configuration

[Model Context Protocol (MCP)](https://modelcontextprotocol.io) lets Claude Code connect to external tools and data sources — databases, APIs, internal services, and more.

## Adding an MCP Server

```bash
claude mcp add <name> --url <server-url>
```

Example:

```bash
claude mcp add postgres --url http://localhost:3100/sse
```

## Listing Configured Servers

```bash
claude mcp list
```

## Removing a Server

```bash
claude mcp remove <name>
```

## MCP Config File

MCP servers can also be declared in `.claude/mcp.json` at the project root:

```json
{
  "servers": [
    {
      "name": "postgres",
      "url": "http://localhost:3100/sse"
    },
    {
      "name": "github",
      "url": "http://localhost:3101/sse"
    }
  ]
}
```

Servers defined here are scoped to the project and don't affect your global Claude Code setup.

---

# Claude Code CLI Reference

Complete reference for the **Claude Code command-line interface**, including commands and flags.

## CLI Commands

Start sessions, pipe content, resume conversations, and manage authentication with these commands.

| Command | Description | Example |
|------|------|------|
| `claude` | Start interactive session | `claude` |
| `claude "query"` | Start interactive session with initial prompt | `claude "explain this project"` |
| `claude -p "query"` | Run query and exit (print mode) | `claude -p "explain this function"` |
| `cat file \| claude -p "query"` | Process piped content | `cat logs.txt \| claude -p "explain"` |
| `claude -c` | Continue most recent conversation | `claude -c` |
| `claude -c -p "query"` | Continue conversation via SDK | `claude -c -p "Check for type errors"` |
| `claude -r "<session>" "query"` | Resume session by ID or name | `claude -r "auth-refactor" "Finish this PR"` |
| `claude update` | Update Claude Code to latest version | `claude update` |
| `claude auth login` | Log in to Anthropic account | `claude auth login --email user@example.com` |
| `claude auth logout` | Log out of account | `claude auth logout` |
| `claude auth status` | Show authentication status | `claude auth status` |
| `claude agents` | List configured subagents | `claude agents` |
| `claude mcp` | Configure MCP servers | `claude mcp` |
| `claude remote-control` | Start remote control session | `claude remote-control` |

## Useful CLI Flags

Customize Claude's behavior with flags.

| Flag | Description | Example |
|------|------|------|
| `--add-dir` | Add extra directories Claude can access | `claude --add-dir ../apps ../lib` |
| `--agent` | Specify which agent to use | `claude --agent my-custom-agent` |
| `--agents` | Define custom subagents using JSON | `claude --agents '{...}'` |
| `--append-system-prompt` | Add instructions to the default prompt | `claude --append-system-prompt "Always use TypeScript"` |
| `--continue` / `-c` | Continue last conversation | `claude --continue` |
| `--debug` | Enable debug logging | `claude --debug "api,mcp"` |
| `--model` | Specify model (sonnet, opus) | `claude --model sonnet` |
| `--output-format` | Specify output format | `claude -p "query" --output-format json` |
| `--resume` / `-r` | Resume specific session | `claude --resume auth-refactor` |
| `--system-prompt` | Replace default system prompt | `claude --system-prompt "You are a Python expert"` |
| `--tools` | Restrict tools Claude can use | `claude --tools "Bash,Edit,Read"` |
| `--verbose` | Enable verbose logging | `claude --verbose` |
| `--version` / `-v` | Show version number | `claude -v` |

## System Prompt Flags

These flags control how you customize Claude's system prompt.

| Flag | Behavior | Modes | Use Case |
|------|------|------|------|
| `--system-prompt` | Replace entire default prompt | Interactive + Print | Full control of Claude behavior |
| `--system-prompt-file` | Replace prompt with file contents | Print only | Use version-controlled prompts |
| `--append-system-prompt` | Append instructions to default prompt | Interactive + Print | Add rules without losing defaults |
| `--append-system-prompt-file` | Append file contents to default prompt | Print only | Add version-controlled rules |

---

# Example: Custom Agents

```bash
claude --agents '{
  "code-reviewer": {
    "description": "Expert code reviewer",
    "prompt": "You are a senior code reviewer focusing on code quality and security",
    "tools": ["Read", "Grep", "Glob", "Bash"],
    "model": "sonnet"
  },
  "debugger": {
    "description": "Debugging specialist",
    "prompt": "Analyze errors and identify root causes"
  }
}'
```

![Controlling Context](controlling-context.png)

---

# Tips & Best Practices

**Be specific in your prompts.** "Fix the login bug" is harder to act on than "The login form submits even when the email field is empty — add client-side validation."

**Use `CLAUDE.md` to reduce repetition.** If you find yourself saying "we use FastAPI" or "never use `var`" in every session, put it in `CLAUDE.md` instead.

**Name your sessions.** Use `claude -r "feature/auth"` to resume long-running tasks without losing context.

**Pipe in context.** Commands like `cat error.log | claude -p "what caused this?"` are great for quick, targeted questions.

**Restrict tools when appropriate.** In sensitive environments, use `--tools "Read,Grep"` to prevent Claude from writing or executing anything.

**Combine agents for complex workflows.** Set up a `code-reviewer` agent for PRs and a `debugger` agent for production issues, each with a focused prompt and minimal tool access.

---

# Troubleshooting

### `claude: command not found`

The install script may not have updated your `PATH`. Add this to your shell profile (`~/.zshrc`, `~/.bashrc`, etc.) and restart your terminal:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

### Authentication errors

Run `claude auth status` to check your session. If expired, re-authenticate:

```bash
claude auth logout
claude auth login
```

### Claude is not reading my `CLAUDE.md`

Make sure the file is in the **root** of the directory you're running `claude` from. Claude does not traverse parent directories to find it.

### MCP server not connecting

Check that your MCP server is running and reachable at the configured URL before starting Claude Code. Use `--debug "mcp"` for detailed connection logs:

```bash
claude --debug "mcp" "list available tools"
```

### Responses are truncated

Increase `max_tokens` in your settings file (`~/.claude/settings.json`) or pass `--max-tokens` as a flag.

---

# SDKs

There are two official SDKs for building with Claude programmatically — the **Client SDK** for direct API access and the **Claude Agent SDK** for building autonomous agents.

---

## Anthropic Client SDK

The Client SDK gives you access to the Claude Messages API from your own code. Official SDKs are available in Python, TypeScript, Java, Go, Ruby, C#, and PHP, each providing idiomatic interfaces, type safety, and built-in support for features like streaming, retries, and error handling.

**Full docs:** https://docs.claude.com/en/api/client-sdks

### Installation

**Python** — requires Python 3.8+

```bash
pip install anthropic
```

**TypeScript / JavaScript** — works with Node.js and browser environments

```bash
npm install @anthropic-ai/sdk
# or
yarn add @anthropic-ai/sdk
```

Additional language SDKs are available for Java, Go, Ruby, and C# (beta).

### Basic Usage

**Python:**

```python
import os
from anthropic import Anthropic

client = Anthropic()  # reads ANTHROPIC_API_KEY from environment

message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)
print(message.content)
```

**TypeScript:**

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic(); // reads ANTHROPIC_API_KEY from environment

const message = await client.messages.create({
  model: "claude-opus-4-6",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hello, Claude" }],
});
console.log(message.content);
```

### Streaming

```python
with client.messages.stream(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Write a haiku"}],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

```typescript
const stream = await client.messages.stream({
  model: "claude-opus-4-6",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Write a haiku" }],
});

for await (const chunk of stream.textStream) {
  process.stdout.write(chunk);
}
```

### Authentication

Set your API key as an environment variable — the SDK picks it up automatically:

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

Or pass it explicitly when constructing the client:

```python
client = Anthropic(api_key="sk-ant-...")
```

---

## Claude Agent SDK

The Agent SDK lets you build AI agents that autonomously read files, run commands, search the web, edit code, and more — giving you the same tools, agent loop, and context management that power Claude Code, programmable in Python and TypeScript.

**Full docs:** https://docs.anthropic.com/en/docs/claude-code/sdk

### Installation

**Python:**

```bash
pip install claude-agent-sdk
```

**TypeScript:**

```bash
npm install @anthropic-ai/claude-agent-sdk
```

### Basic Usage

**Python:**

```python
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

async def main():
    async for message in query(
        prompt="What files are in this directory?",
        options=ClaudeAgentOptions(allowed_tools=["Bash", "Glob"]),
    ):
        if hasattr(message, "result"):
            print(message.result)

asyncio.run(main())
```

**TypeScript:**

```typescript
import { query } from "@anthropic-ai/claude-agent-sdk";

for await (const message of query({
  prompt: "What files are in this directory?",
  options: { allowedTools: ["Bash", "Glob"] },
})) {
  if (message.result) {
    console.log(message.result);
  }
}
```

### Available Tools

The Agent SDK exposes the same built-in tools as Claude Code:

| Tool | Description |
|------|-------------|
| `Bash` | Run shell commands |
| `Read` | Read file contents |
| `Edit` | Make targeted edits to files |
| `Write` | Write new files |
| `Glob` | Find files by pattern |
| `Grep` | Search file contents |
| `WebSearch` | Search the web |
| `TodoRead` / `TodoWrite` | Manage task lists |

Restrict the tools available to an agent using `allowed_tools` (Python) or `allowedTools` (TypeScript) to limit its scope and reduce risk.

### Custom Agents

You can combine multiple specialized agents in a single workflow:

```python
from claude_agent_sdk import query, ClaudeAgentOptions

reviewer_options = ClaudeAgentOptions(
    system_prompt="You are a senior code reviewer. Focus on security and correctness.",
    allowed_tools=["Read", "Grep", "Glob"],
    model="claude-opus-4-6",
)

fixer_options = ClaudeAgentOptions(
    system_prompt="You are a bug fixer. Apply minimal, targeted changes.",
    allowed_tools=["Read", "Edit", "Bash"],
)

async def review_then_fix(filepath: str):
    issues = []
    async for msg in query(f"Review {filepath} for bugs", options=reviewer_options):
        if hasattr(msg, "result"):
            issues.append(msg.result)

    async for msg in query(f"Fix these issues in {filepath}: {issues}", options=fixer_options):
        if hasattr(msg, "result"):
            print(msg.result)
```

### CLAUDE.md Support

The Agent SDK respects your project's `CLAUDE.md` file, so agents inherit the same project context as interactive Claude Code sessions — no duplication needed.

---

## Choosing the Right SDK

| | Client SDK | Agent SDK |
|---|---|---|
| **Use case** | Chat, completions, structured outputs | Autonomous coding agents |
| **Tools** | You define custom tools | Built-in file, shell, and web tools |
| **Control** | Full — you manage the loop | Managed agent loop |
| **Best for** | Apps, pipelines, integrations | CI automation, coding workflows |

---

# Updating Claude Code

Keep Claude Code up to date to get the latest models, tools, and bug fixes:

```bash
claude update
```

To check your current version:

```bash
claude --version
```