# Package management & permissions

- Never use pip with --break-system-packages or --user.
- Ordinary pip installs are allowed inside an explicitly named virtual
  environment when the user authorizes them. Verify that both Python and pip
  resolve inside that environment before installing; never target system Python.
- For missing system Python packages, print the exact pacman command and ask the
  user to run it. Wait for confirmation before proceeding.
- Never run commands with sudo yourself. If root is needed, print the
  exact command and ask the user to run it. Wait for confirmation.

# Environment ownership

- Diagnose package ownership, executable location, and process launch context
  before changing `PATH` or installing another copy of a tool.
- On the Arch laptop, distribution executable paths come from `/etc/profile`
  and `/etc/profile.d/`. Do not duplicate those paths in dotfiles or shadow a
  packaged tool to unblock one project.
- Shared configuration may contain portable personal paths only. On hosts
  without root access, additional user-space paths belong in private
  machine-local shell configuration and must not leak to other machines.
- Keep project dependencies and toolchain setup in the project's virtual
  environment, wrapper, or documented setup script rather than global shell
  startup files.

# Code Style

- Always strive for concise, simple solutions.
- If a problem can be solved in a simpler way, propose the simpler approach.
- Prefer the smallest coherent change at the appropriate abstraction level.
  Minimize incidental scope, not restructuring needed to fully resolve the
  problem. Fewer changed lines are not better when they preserve duplication,
  a mismatched structure, or accumulated patches.
- Avoid abstractions unless they clarify hard logic or remove real duplication.

# General Preferences

- At the start of every session, load `unslop`; apply it to every response.
- If asked to do too much work at once, stop and state that clearly.
- Prefer direct, factual collaboration over long speculative explanations.
- When debugging, prefer concrete evidence from tests, logs, or instrumentation
  over guessing.

# Workspace Layout

- Managed configuration lives in `~/.dotfiles`; inspect its `README.md` before changing system configuration.
- Personal scripts live in the separate `~/.scripts` repository.
- Software projects live as independent repositories under `~/.software`.

# Model Routing

These are defaults, not limits. Judge the output, not the price tag.

Do not let cost prevent using the right model for the job. Instead, use cheaper models to gather information, try clear implementation paths, and reduce ambiguity before moving work to a more expensive model.

Physics escalation:

- DeepSeek V4 Flash may handle implementation around physics code.
- Luna edges Flash on physics, but not by much; for stronger physics reasoning use Luna, GPT-5.6, or GLM-5.2 directly.
- If Flash misses a physics issue while coding, do not ask Flash to check again. Escalate.
- Use Luna/GPT/GLM for physics checks.
- Use GPT-5.6 Sol for more complex physics reasoning.

Escalation rules:

- For physics work: physics > intelligence > availability.
- For clear mechanical work: availability > intelligence.
- Start cheap when the task is exploratory, reversible, or clearly specified.
- Escalate when the cheap model is uncertain, inconsistent, or produces a mediocre solution.
- Escalating costs less than doing bad work.
- Use subagents according to these routing rules when they reduce cost, context, or risk.

Subagent routing:

1. Decompose multi-step work into small, independently verifiable tasks before delegating.
2. Use explore for repository discovery, and worker by default for all bounded implementation, trivial mechanical work, debugging, refactoring, and tests.
3. Use smart-worker for a precisely scoped physics, statistical, mathematical, numerical, or algorithmic correctness question when that reasoning is central to the task. It may be used directly only when the prompt names the concrete capability required; prior worker failure is not mandatory.
4. Do not send an entire large task to smart-worker. Keep architecture, coordination, integration, and final validation in the primary agent.
5. Delegate each task to the least expensive agent reasonably likely to complete it correctly on the first attempt.
6. For general implementation and debugging, use worker first. Escalate after one inconclusive, inconsistent, incomplete, or incorrect result rather than repeatedly retrying worker.
7. Do not use smart-worker merely because work is difficult or non-trivial, for broad reviews, or for unsolicited second opinions.
8. Default to at most one smart-worker call per user request. Make another only for a distinct critical blocker, not merely another component to review.
9. Use copy-reviewer for independent structural and prose feedback on
   substantial reports or written copy. It is read-only and does not replace
   factual, physics, numerical, or visual review.
