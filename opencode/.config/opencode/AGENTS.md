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

- Prefer direct, factual collaboration over long speculative explanations.
- When debugging, prefer concrete evidence from tests, logs, or instrumentation
  over guessing.
- When changing workflows, skills or policy, trace the owning rule through its
  consumers: root instructions, skills, harness defaults, enforcing code/tests
  and human guides. Remove superseded requirements, test omitted-input and
  recovery behavior, and distinguish automatic enforcement from prose or explicit
  preflight. Follow the project's workflow-change procedure where one exists.

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
the harness. Check effective routes when possible.

Select the most available model and effort likely to complete each bounded task
correctly. Availability means cost **per completed task**, repeated-use limits
and current subscription headroom. Do not spend on broad unsolicited second
opinions. Escalate directly when a concrete required capability is missing, or
after one inconclusive or incorrect result; diagnose and escalate only the
unresolved part. Avoid repeatedly retrying an inadequate route. Implementation
around physics does not itself make a physics judgment. Review
physics/numerical conclusions with the `council` skill (one strong model per
reachable provider) and retain the human domain owner's approval.

The council members are Opus high and Sol xhigh
(CritPt v2 hard subset: 58% and 68% below), one
fresh session each, including for the final review pass. Report an unreachable
provider instead of substituting another model. Check a configured delegate's
model before dispatch. Respect current usage headroom; a usage-limit failure is
not evidence of a capability failure.

## OpenCode subagent defaults

Use the routes below, for default delegation. These defaults do not change
the primary session's model or effort.

| Agent         | Model                       | Effort                        |
| ------------- | --------------------------- | ----------------------------- |
| explore       | `openai/gpt-6-luna`         | Provider default; no override |
| vision-reader | `openai/gpt-6-luna`         | Provider default; no override |
| worker        | `openai/gpt-6.1-sol`        | Provider default; no override |
| copy-reviewer | `openai/gpt-6-astra#medium` | medium                        |

The configured defaults apply when dispatch omits a model override. Do not
invent a fixed effort or benchmark score for the provider default. The
copy-reviewer row is the user's explicit Astra exception for that OpenCode
subagent only; it does not set copy review in other harnesses, and it is not a
reason to use Astra for routine implementation, visual inspection, or physics
review.

## Evidence for routing

Intelligence Index v5.0 (broad, noisy prior), CritPt v2 (Hard Subset;
external physics proxy), and weighted USD per Intelligence Index task (API
benchmark cost, not subscription usage). Checked 2026-10-30. The v5 Index,
CritPt v2 and task costs use different evaluations from the previous v4.3.2
table; do not compare their values across versions. Numbers are measured at
the listed effort, not success probabilities for this task. CritPt percentages
are rounded as displayed in AA's pairwise comparisons. `—` means unverified
benchmark evidence or no grounded personal rating. Taste and alignment are
tentative 0–10 judgments, distinct from AA scores. Alignment means fidelity to
the intended outcome and existing decisions, including when clarification is
needed.

| Model             | Effort | AA Index v5 | CritPt v2 hard | $/task | Taste | Alignment |
| ----------------- | ------ | ----------: | -------------: | -----: | ----: | --------: |
| GPT-6 Luna        | low    |          10 |              — |   0.01 |     — |         — |
| GPT-6 Luna        | medium |          18 |              — |   0.04 |     — |         — |
| GPT-6 Luna        | high   |          21 |            31% |   0.07 |     — |         — |
| GPT-6 Luna        | xhigh  |          23 |            36% |   0.10 |     — |         — |
| GPT-6 Luna        | max    |          28 |            42% |   0.15 |     — |         — |
| GPT-6.1 Sol       | low    |          35 |            60% |   0.16 |     — |         — |
| GPT-6.1 Sol       | medium |          46 |            65% |   0.36 |     — |         — |
| GPT-6.1 Sol       | high   |          50 |            68% |   0.59 |     — |         — |
| GPT-6.1 Sol       | xhigh  |          52 |            68% |   0.76 |     5 |         5 |
| GPT-6 Astra       | low    |          43 |            60% |   1.42 |     — |         — |
| GPT-6 Astra       | medium |          51 |            71% |   2.73 |     7 |       7.5 |
| GPT-6 Astra       | high   |          55 |            72% |   3.24 |     — |         — |
| Claude Haiku 5.5  | low    |          19 |              — |   0.04 |     — |         — |
| Claude Haiku 5.5  | medium |          25 |            30% |   0.09 |     — |         — |
| Claude Haiku 5.5  | high   |          30 |            43% |   0.16 |     — |         — |
| Claude Haiku 5.5  | xhigh  |          34 |            45% |   0.25 |     — |         — |
| Claude Haiku 5.5  | max    |          36 |            41% |   0.41 |     — |         — |
| Claude Sonnet 5.5 | medium |          30 |            28% |   0.78 |     — |         — |
| Claude Sonnet 5.5 | high   |          41 |            48% |   1.64 |     — |         — |
| Claude Sonnet 5.5 | xhigh  |          50 |            54% |   4.09 |     — |         — |
| Claude Opus 5.5   | low    |          35 |            34% |   0.98 |     — |         — |
| Claude Opus 5.5   | medium |          48 |            53% |   2.45 |     — |         — |
| Claude Opus 5.5   | high   |          52 |            58% |   3.46 |     9 |         8 |
| Claude Opus 5.5   | xhigh  |          57 |            63% |   6.05 |     — |         — |

AA sources, checked 2026-10-30:

- [Index v5 methodology and version change](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5).
- Luna: [low](https://artificialanalysis.ai/models/gpt-6-luna-low),
  [medium](https://artificialanalysis.ai/models/gpt-6-luna-medium),
  [high/xhigh](https://artificialanalysis.ai/models/comparisons/gpt-6-luna-high-vs-gpt-6-luna-xhigh),
  [max and Sonnet medium](https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-5-medium-vs-gpt-6-luna).
- Sol: [low/medium](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-low-vs-gpt-6-1-sol-medium),
  [high/xhigh](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-high-vs-gpt-6-1-sol-xhigh).
- [Astra and Opus effort comparison](https://artificialanalysis.ai/models/releases/comparisons),
  [Astra high/medium](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-high-vs-gpt-6-astra-medium),
  [Opus low/medium](https://artificialanalysis.ai/models/comparisons/claude-opus-5-5-low-vs-claude-opus-5-5-medium),
  [Opus high/xhigh](https://artificialanalysis.ai/models/comparisons/claude-opus-5-5-high-vs-claude-opus-5-5-xhigh).
- Haiku: [low](https://artificialanalysis.ai/models/claude-haiku-5-5-low),
  [high/medium](https://artificialanalysis.ai/models/comparisons/claude-haiku-5-5-high-vs-claude-haiku-5-5-medium),
  [high/xhigh](https://artificialanalysis.ai/models/comparisons/claude-haiku-5-5-high-vs-claude-haiku-5-5-xhigh),
  [max/xhigh](https://artificialanalysis.ai/models/comparisons/claude-haiku-5-5-vs-claude-haiku-5-5-xhigh).
- Sonnet: [medium](https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-5-medium-vs-gpt-6-luna),
  [high/xhigh](https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-5-high-vs-claude-sonnet-5-5-xhigh).

Sonnet and Opus rows use AA's adaptive reasoning variants labelled "Default
Fallback". Verified CritPt v2 hard-subset values were unavailable for Luna low,
Luna medium and Haiku low in the accessible pages; those cells stay `—` rather
than carrying forward CritPt v1 scores. Some cached comparisons still show v4;
only explicitly v5/v2 evidence is used here. Personal ratings are unchanged.

## Dispatch

- Appearance-only review starts with an explicit economy image-capable route,
  after applicable programmatic checks. Use selected new/changed layouts,
  representative families and relevant flags; preserve accepted evidence.
  Final status or repagination does not mandate exhaustive inspection. Never
  inherit Opus/Astra for visual work merely from the primary. Expensive escalation
  needs a named unresolved finding or capability gap; quota failure is not one.
  Follow the project's visual preflight and record model, effort visibility,
  pages, task and stopping condition. Do not repeat source/numerical audits in
  appearance review or reopen accepted work for optional cosmetics.

- For substantial explanatory writing, start with a model at suitable effort
  and a confirmed reader brief. Reserve higher taste models for a specific
  unresolved writing problem after the first review, not as an automatic prose
  route. Use `grilling` where project policy requires it and check the artifact
  against the decision record.
- For routine discovery and bounded implementation, choose an inexpensive
  suitable worker. For bounded source/API reviews and physics, statistical,
  mathematical or numerical reasoning, use a model at the effort needed for the
  concrete question. Escalate only the unresolved part if that route is
  inadequate. CritPt is a prior, not domain validation. A physics or numerical
  conclusion still goes to the council before it is relied on.
- Keep a separate read-only copy-reviewer for independent structural and prose
  feedback on substantial copy. If available use the configured copy-reviewer
  subagent; otherwise use a capable native reviewer. Further escalation needs a
  documented structural/voice issue that review cannot resolve. Copy review
  does not replace source, physics or visual review.
- Give each delegate a self-contained brief with owned paths, evidence,
  constraints and verification. Preserve the user's provider-default effort
  choices above; otherwise select effort explicitly where the harness allows
  it. Report default, inherited or overridden routes honestly. An effort the
  harness cannot set is not a reason to leave it.

### Shell routes

Native subagents are the default. Use a shell route only to reach a model the
harness does not expose: a cheaper suitable model from another family, a
different-family reviewer, or a named capability no native model has. Leaving
the harness costs little, but never use it to change the effort of a model
available natively.

- OpenAI subscription models: `opencode run -m 'openai/<model>#<effort>'
'<brief>'`, for example `openai/gpt-6.1-sol#high`. Omit `#<effort>` when
  using the provider default. List current IDs with `opencode models`.
- Claude models from a non-Claude harness:
  `claude -p --model <model> --effort <level> '<brief>'`.
- Run from the delegate's owned working directory. The shell delegate gets the
  same brief, ownership and permission rules as a native subagent; it is a
  separate agent, so report its route and treat its output as delegate
  evidence, not verified fact.
