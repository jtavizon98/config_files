# Package management & permissions

- Never use pip with --break-system-packages or --user.
- For missing Python packages, print the exact pacman command and
  ask the user to run it. Wait for confirmation before proceeding.
- Never run commands with sudo yourself. If root is needed, print the
  exact command and ask the user to run it. Wait for confirmation.

# Code Style

- Always strive for concise, simple solutions.
- If a problem can be solved in a simpler way, propose the simpler approach.
- Prefer the smallest correct change.
- Avoid abstractions unless they clarify hard logic or remove real duplication.

# General Preferences

- If asked to do too much work at once, stop and state that clearly.
- Prefer direct, factual collaboration over long speculative explanations.
- When debugging, prefer concrete evidence from tests, logs, or instrumentation over guessing.

# Model Routing

These are defaults, not limits. Judge the output, not the price tag.

Do not let cost prevent using the right model for the job. Instead, use cheaper models to gather information, try clear implementation paths, and reduce ambiguity before moving work to a more expensive model.

Definitions:

- Availability means how cheap, plentiful, and subscription-safe the model is for repeated use.
- Intelligence means how hard a problem can be handed to the model while still expecting a good unsupervised solution.
- Physics means the ability to reason about physical plausibility, dimensional analysis, QCD, conservation constraints, HEP analysis logic, uncertainties, MC/data comparisons, and whether values are physically possible.
- Image means the ability to understand screenshots, plots, figures, and visual diagnostics.
- Taste is how nice it feels to talk to the model and have the model explain things.

Model scores:

| model             | availability | intelligence | physics | image | taste |
| ----------------- | -----------: | -----------: | ------: | ----: | ----: |
| GPT-5.6 Sol       |            2 |            8 |       6 |     8 |       |
| GPT-5.6 Terra     |            3 |            8 |       5 |     8 |       |
| GPT-5.6 Luna      |            4 |            8 |       4 |     8 |       |
| DeepSeek V4 Pro   |            7 |            6 |       2 |   N/A |     7 |
| DeepSeek V4 Flash |           10 |            4 |       1 |   N/A |     6 |
| MiniMax M3        |            6 |            6 |       1 |     7 |     6 |

Routing:

| preferred agent | model             |
| --------------- | ----------------- |
| explore         | DeepSeek V4 Flash |
| cheap-worker    | MiMo-V2.5-Pro      |
| worker          | DeepSeek V4 Pro   |
| smart-worker    | GPT-5.6 Luna      |
| primary agent   | GPT-5.6 Sol       |
| vision-reader   | MiniMax M3        |

Physics escalation:

- DeepSeek V4 Pro may handle implementation around physics code.
- If harder physics reasoning is needed, use GPT-5.6 directly.
- If V4 Pro misses a physics issue while coding, do not ask V4 Pro to check again. Escalate to GPT-5.6.
- Use GPT-5.6 Terra or Luna for physics checks.
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
2. Use explore for repository discovery, cheap-worker for trivial mechanical work, and worker for normal bounded implementation and tests.
3. Use smart-worker only for a difficult bounded slice, focused review, or reasoning problem that worker is not suited to handle.
4. Do not send an entire large task to smart-worker. Keep architecture, coordination, integration, and final validation in the primary agent.
5. Delegate each task to the least capable suitable agent. Escalate only after concrete uncertainty, failure, or risk justifies it.
