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

# Claude Code Setup Guide

Full setup directions can be found here:
https://code.claude.com/docs/en/quickstart

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

## After installation, 
run **claude** at your terminal. The first time you run this command you will be prompted to authenticate

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

Use Git with Claude Code 

```bash 
what files have I changed?

commit my changes with a descriptive message

create a new branch called feature/quickstart

show me the last 5 commits

help me resolve merge conflicts
```

Fix a bug or add a feature

```bash
add input validation to the user registration form

there's a bug where users can submit empty forms - fix it
```

Test out other common workflows

```bash
refactor the authentication module to use async/await instead of callbacks
```

Write tests

```bash
write unit tests for the calculator functions
```

Update documentation

```bash 
update the README with installation instructions
```

Code review

```bash
review my changes and suggest improvements
```

## Claude Code Commands

| Command | What it does | Example |
|-------|-------|-------|
| `claude` | Start interactive mode | `claude` |
| `claude "task"` | Run a one-time task | `claude "fix the build error"` |
| `claude -p "query"` | Run one-off query, then exit | `claude -p "explain this function"` |
| `claude -c` | Continue most recent conversation in current directory | `claude -c` |
| `claude -r` | Resume a previous conversation | `claude -r` |
| `claude commit` | Create a Git commit | `claude commit` |
| `/clear` | Clear conversation history | `/clear` |
| `/help` | Show available commands | `/help` |
| `exit` or `Ctrl + C` | Exit Claude Code | `exit` |