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

These are starting points, not model assignments. Preserve the user's choice of
primary model and effort. Decompose work before delegating; keep architecture,
coordination, integration and final validation with the primary. Use the
subagents and model/effort controls actually exposed by the active harness.
Never shell out to a model the harness exposes natively: when a native model
fits but its effort cannot be set, use it at the effort the harness gives and
report that. The shell routes under Dispatch are a fallback for models outside
the harness. OpenCode profiles may have configured model defaults;
other harnesses need not recreate those profiles. Check effective routes when
possible.

Select the most available model and effort likely to complete each bounded task
correctly. Availability means cost **per completed task**, repeated-use limits
and current subscription headroom, not token price alone. Do not spend on broad
unsolicited second opinions. Escalate directly when a concrete required
capability is missing, or after one inconclusive or incorrect result; diagnose
and escalate only the unresolved part. Avoid repeatedly retrying an inadequate
route. Implementation around physics does not itself make a physics judgment.
Use capable independent review for physics/numerical conclusions and retain the
human domain owner's approval.

Reserve Astra for escalation with a named unresolved capability or a demonstrated
failed review. Required independent review does not itself require Astra: use a
separate session of any model at the Sol xhigh / Opus high-xhigh tier (CritPt
31-32% below). Prefer a different family than the author when one is
available, including for the final review pass. Check a configured delegate's
model before dispatch rather than inheriting an Astra default. Respect current
usage headroom; a usage-limit failure is not evidence of a capability failure.

## Evidence for routing

Intelligence Index v4.3.2 (broad, noisy prior), CritPt (best available external
physics proxy; currently under review), and weighted USD per Intelligence Index
task (API benchmark cost, not subscription usage). Numbers are measured at the
listed effort, not success probabilities for this task. `—` means no grounded
local rating. Taste and alignment are tentative 0–10 judgments, distinct from
AA scores. Alignment means fidelity to the intended outcome and existing
decisions, including when clarification is needed. The local writing comparison
had different review budgets; do not treat its ratings as controlled model
performance measurements.

| Model               | Effort  | AA Index | CritPt | $/task | Taste | Alignment |
| ------------------- | ------- | -------: | -----: | -----: | ----: | --------: |
| DeepSeek V4.1 Flash | max     |       39 |    14% |   0.27 |     3 |         — |
| GLM-5.3-Flash       | default |       42 |    15% |   0.25 |     4 |         — |
| GPT-6 Luna          | low     |       22 |     3% | 0.0045 |     — |         — |
| GPT-6 Luna          | medium  |       30 |    11% |   0.02 |     — |         — |
| GPT-6 Luna          | high    |       33 |    15% |   0.03 |     — |         — |
| GPT-6 Luna          | xhigh   |       35 |    17% |   0.04 |     — |         — |
| GPT-6 Luna          | max     |       38 |    19% |   0.07 |     — |         — |
| GPT-6.1 Sol         | low     |       42 |    25% |   0.13 |     — |         — |
| GPT-6.1 Sol         | medium  |       48 |    28% |   0.21 |     — |         — |
| GPT-6.1 Sol         | high    |       50 |    30% |   0.32 |     — |         — |
| GPT-6.1 Sol         | xhigh   |       51 |    32% |   0.39 |     5 |         5 |
| GPT-6 Astra         | low     |       46 |    26% |   0.82 |     — |         — |
| GPT-6 Astra         | medium  |       50 |    29% |   1.54 |     7 |       7.5 |
| GPT-6 Astra         | high    |       51 |    29% |   1.73 |     — |         — |
| Claude Sonnet 5.5   | medium  |       41 |    17% |   0.59 |     — |         — |
| Claude Sonnet 5.5   | high    |       47 |    25% |   1.08 |     — |         — |
| Claude Sonnet 5.5   | xhigh   |       52 |    31% |   2.74 |     — |         — |
| Claude Opus 5.5     | low     |       42 |    18% |   0.55 |     — |         — |
| Claude Opus 5.5     | medium  |       51 |    28% |   1.34 |     — |         — |
| Claude Opus 5.5     | high    |       54 |    31% |   1.82 |     9 |         8 |
| Claude Opus 5.5     | xhigh   |       56 |    32% |   3.46 |     — |         — |

AA sources: [Flash/GLM](https://artificialanalysis.ai/models/comparisons/deepseek-v4-1-flash-vs-glm-5-3-flash),
[Astra low/high](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-low-vs-gpt-6-astra-high),
[Astra medium](https://artificialanalysis.ai/models/gpt-6-astra-medium).
[release/efforts](https://artificialanalysis.ai/models/releases/gpt-6-1-sol),
[low/medium](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-low-vs-gpt-6-1-sol-medium),
[medium/high](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-medium-vs-gpt-6-1-sol-high),
[xhigh/max](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-xhigh-vs-gpt-6-1-sol),
[Luna](https://artificialanalysis.ai/models/releases/gpt-6-luna),
[Opus](https://artificialanalysis.ai/models/releases/claude-opus-5-5),
[Sonnet](https://artificialanalysis.ai/models/releases/claude-sonnet-5-5),
[Fable](https://artificialanalysis.ai/models/releases/claude-fable-5-1);
CritPt from the pairwise variant comparisons. Claude rows are AA's adaptive
reasoning variants; AA has not scored Sonnet 5.5 low.

## Dispatch

- For substantial explanatory writing, start with a model at suitable effort
  and a confirmed reader brief. Reserve higher taste models for a specific
  unresolved writing problem after the first review, not as an automatic prose
  route. Use `grilling` where project policy requires it and check the artifact
  against the decision record.
- For routine discovery and bounded implementation, choose an inexpensive
  suitable worker. For bounded
  source/API reviews and physics, statistical, mathematical or numerical reasoning,
  use a model at the effort needed for the concrete question. Escalate only
  the unresolved part if that route is inadequate. CritPt is a prior, not
  domain validation.
- Keep a separate read-only copy-reviewer for independent structural and prose
  feedback on substantial copy. Use a capable copy-reviewer by default and
  reserve higher taste models for a documented structural/voice issue that
  review cannot resolve. Copy review does not replace source, physics or visual
  review.
- Give each delegate a self-contained brief with owned paths, evidence,
  constraints and verification. Select effort explicitly where the harness
  allows it, and report inherited or overridden routes honestly. An effort the
  harness cannot set is not a reason to leave it.

### Shell routes

Native subagents are the default. Use a shell route only to reach a model the
harness does not expose: a cheaper suitable model from another family, a
different-family reviewer, or a named capability no native model has. Leaving
the harness costs little, but never use it to change the effort of a model
available natively.

- OpenAI and OpenCode Go models: `opencode run -m '<provider>/<model>#<effort>'
  '<brief>'`, for example `openai/gpt-6.1-sol#high` or
  `opencode-go/glm-5.3-flash`. List current IDs with `opencode models`.
- Claude models from a non-Claude harness:
  `claude -p --model <model> --effort <level> '<brief>'`.
- Run from the delegate's owned working directory. The shell delegate gets the
  same brief, ownership and permission rules as a native subagent; it is a
  separate agent, so report its route and treat its output as delegate
  evidence, not verified fact.
