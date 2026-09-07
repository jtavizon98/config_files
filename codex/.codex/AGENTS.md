# Model routing

Choose the model and reasoning effort for each delegated task explicitly.
Use the least expensive available model reasonably likely to do the task
correctly. These are starting points; judge results and escalate when needed.
Delegate only when the bounded work saves useful time, context, or cost.

Evaluate four distinct requirements:

| Dimension | Meaning | Evidence |
| --- | --- | --- |
| Physics | Correct physical, statistical, mathematical and numerical reasoning | CritPt at the measured effort; task-specific checks and domain review |
| Intelligence | Handling ambiguity, implementation, tools and multi-step reasoning | AA Intelligence Index, relevant coding evaluations and observed results |
| Availability | Model access, usable quota, latency and cost of completing the task | Current harness choices and actual account/runtime evidence; API cost is only a proxy |
| Taste | Writing voice, explanatory structure, restraint and presentation judgment | Jairo's preference and reviewed work; do not infer it from CritPt or aggregate intelligence |

| Work required | Starting model | Reasoning effort |
| --- | --- | --- |
| Narrow discovery, extraction, repetitive checks | `gpt-5.6-luna` | `low` |
| Clearly specified mechanical implementation and tests | `gpt-5.6-luna` | `medium` |
| General bounded implementation or debugging needing judgment | `gpt-5.6-sol` | `low` |
| Complex implementation, causal debugging, algorithmic or scientific reasoning | `gpt-5.6-sol` | `medium`; increase for demonstrated difficulty |
| Writing and reviewing copy, narrative structure, aesthetic judgment | `gpt-6-astra` | `low`; increase when structural ambiguity requires it |
| Visual inspection for clipping, labels and obvious layout defects | `gpt-5.6-luna` | `low`; route design judgment to Astra |
| Primary orchestration, architecture, integration and final judgment | `gpt-6-astra` | Preserve the user's selected effort; `medium` is the ordinary starting point |

For physics, prioritize physics capability, then general intelligence, then
availability. For copy, prioritize taste and fidelity to the author. For clear
mechanical work, prioritize availability once the capability requirement is
met. Sol is a strong economical option for reasoning and implementation;
Astra's preferred taste does not make it the default for all hard problems.

Give each child a concrete deliverable, necessary context, owned paths,
constraints and a verification criterion. Select both `model` and
`reasoning_effort` in the spawn call. In harnesses where a full-history fork
inherits the parent and disallows overrides, use `fork_turns="none"` with a
self-contained brief, or a supported bounded history fork. Do not silently
pay for Astra inheritance just to transfer context. Custom-agent configuration
may override spawn settings; check the effective route where the client exposes
it and report any inability to apply the requested model.

Escalate after one inadequate, inconsistent or inconclusive result; do not
repeatedly retry a cheap model. Use Sol directly when the capability need is
already clear. Increase reasoning for a concrete reasoning bottleneck; use
Astra when taste or unresolved broader judgment warrants it. Use max-effort
model comparisons as a practical prior for relative capability when lower-effort
measurements are missing; choose effort from task complexity and observed
results. Label this extrapolation rather than presenting max-effort scores as
measured low/medium performance. Scientific conclusions
still require suitable independent review and the human domain owner.

If a model is unavailable or quota is exhausted, choose an available model
meeting the same requirement and state the substitution. Do not silently
weaken physics or copy review to finish. Model routing applies to any useful
agent role; it does not require fixed role names or automatic fan-out.
