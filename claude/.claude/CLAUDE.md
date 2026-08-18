# Package management & permissions

- Never use pip with `--break-system-packages` or `--user`.
- For missing Python packages, print the exact pacman command and
  ask the user to run it. Wait for confirmation before proceeding.
- Never run commands with sudo yourself. If root is needed, print the
  exact command and ask the user to run it. Wait for confirmation.

# Code Style

- Always strive for concise, simple solutions.
- If a problem can be solved in a simpler way, propose the simpler approach.
- Prefer the smallest coherent change at the appropriate abstraction level.
  Minimize incidental scope, not restructuring needed to fully resolve the
  problem. Fewer changed lines are not better when they preserve duplication,
  a mismatched structure, or accumulated patches.
- Avoid abstractions unless they clarify hard logic or remove real duplication.

# General Preferences

- If asked to do too much work at once, stop and state that clearly.
- Prefer direct, factual collaboration over long speculative explanations.
- When debugging, prefer concrete evidence from tests, logs, or instrumentation over guessing.

# Workspace Layout

- Managed configuration lives in `~/.dotfiles`, deployed with GNU stow;
  inspect its `README.md` before changing system configuration.
- Personal scripts live in the separate `~/.scripts` repository.
- Software projects live as independent repositories under `~/.software`.
- Before changing a repository, read its root `AGENTS.md` and `README.md` when present.

# Delegation

- Prefer the built-in subagents (Explore, Plan, general-purpose) for delegation.
- For bulk mechanical work where primary-model tokens are not worth spending,
  the `delegate-opencode` skill routes tasks to cheaper external models.
