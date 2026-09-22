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

# Model routing

Decompose work before choosing a delegate. Select the highest-availability
model and effort reasonably likely to complete each bounded subtask correctly.
These rules apply regardless of the primary model. Preserve the user's primary
model and effort; do not infer that a delegate should match them.

## Selection and escalation

1. Keep architecture, coordination, integration and final validation with the
   primary. Delegate small, independently verifiable deliverables when doing so
   saves useful time, context or cost. Do not delegate an entire large task to
   a more expensive model.
2. Start with the highest-availability suitable option below. Ordinary bounded
   implementation, debugging, refactoring and tests do not by themselves justify
   a more expensive option. Supply enough context and acceptance criteria to
   make the cheaper option effective.
3. Before bypassing a higher-availability option, state the concrete capability
   it lacks for this subtask, the relevant evidence, or its observed failure.
   "Difficult", "non-trivial", "needs judgment", "scientific" and "writing" are
   not sufficient reasons. Do not invent benchmark thresholds to justify a
   preferred model. Required capabilities constrain selection; do not maximize
   intelligence or combine the columns into a weighted overall score.
4. Compare model AND effort before escalating. Consider more reasoning on the
   cheaper model before switching families; choose from the whole table rather
   than following a fixed model ladder. Direct escalation is allowed for a
   precisely scoped capability requirement; a deliberately unsuitable trial
   is not required.
5. After one inconclusive, inconsistent, incomplete or incorrect result,
   diagnose the gap and escalate only the unresolved part. Do not repeatedly
   retry the same inadequate option or promote the rest of the task with it.
   Reassess availability for each new subtask.
6. Do not use expensive delegates for unsolicited second opinions or broad
   "review everything" passes. Default to at most one Sol/Astra delegation per
   user request. Another needs a distinct critical blocker or an explicitly
   required independent review; name it before dispatch. A separate component
   alone is not a reason. This is a spending guard, not a waiver of required
   correctness or review.
7. Physics, statistical, mathematical and numerical correctness requirements
   must be explicit. Use CritPt as physics evidence at the measured effort,
   alongside task-specific checks. Implementation around physics does not
   automatically require the same model as adjudicating the physics.
   Scientific conclusions still need capable independent review and the human
   domain owner.
8. Taste means fidelity to Jairo's voice, explanatory structure and presentation
   judgment. It is a separate preference, not inferred from AA or CritPt.
   Astra is preferred where that taste is material; this does not assign every
   writing task to Astra. Image input support likewise is not an image-quality
   score. Use task-specific evidence for visual review.
9. Filter out unavailable model/effort options using the current harness and
   account state. State substitutions. Do not silently reduce required
   capability when quota or access prevents the selected route.

## Numerical evidence

Artificial Analysis snapshot: 2026-09-10, Intelligence Index v4.3.
Intelligence is the AA aggregate score; physics is CritPt percent correct.
These are effort-specific benchmark results, not success probabilities for
the current task. Costs are AA's weighted API cost per Intelligence Index task
in USD, including token usage, not merely token prices.

Availability = 10 × minimum published cost in this table / row cost.
The minimum published cost is $0.04, so availability = 0.40 / row cost,
rounded to two decimals. Higher means cheaper. This is benchmark affordability,
not subscription quota or latency. Recompute all ratings together when updating
the dated snapshot; keep benchmark versions consistent.

| Model        | Effort | Availability ↑ | Cost/task USD ↓ | Intelligence ↑ | CritPt ↑ |
| ------------ | ------ | -------------: | --------------: | -------------: | -------: |
| gpt-5.6-luna | low    |              — |               — |            22* |       3% |
| gpt-5.6-luna | medium |              — |               — |            26* |       5% |
| gpt-5.6-luna | high   |          10.00 |            0.04 |             32 |      17% |
| gpt-5.6-luna | xhigh  |           4.44 |            0.09 |             35 |      21% |
| gpt-5.6-luna | max    |           2.22 |            0.18 |             38 |      21% |
| gpt-5.6-sol  | low    |           1.54 |            0.26 |             34 |      15% |
| gpt-5.6-sol  | medium |           0.80 |            0.50 |             39 |      23% |
| gpt-5.6-sol  | high   |           0.49 |            0.81 |             42 |      26% |
| gpt-5.6-sol  | xhigh  |           0.34 |            1.18 |             44 |      29% |
| gpt-5.6-sol  | max    |           0.20 |            1.99 |             47 |      32% |
| gpt-6-astra  | low    |           0.49 |            0.82 |             46 |      26% |
| gpt-6-astra  | medium |           0.26 |            1.54 |             50 |      29% |
| gpt-6-astra  | high   |           0.23 |            1.72 |             51 |      29% |
| gpt-6-astra  | xhigh  |           0.17 |            2.31 |             53 |      31% |
| gpt-6-astra  | max    |           0.12 |            3.26 |             53 |      32% |

- AA marks Luna low/medium intelligence as estimated and publishes no cost per
  task for those rows. Missing availability is unknown, not zero. Luna high is
  the cheapest measured option. Lower efforts may be chosen for a bounded task
  using observed results or explicitly labelled extrapolation; do not fabricate
  costs or transfer high/max capability scores to lower efforts. Break rounded
  availability ties using cost. Unmeasured efforts remain unranked.

Sources: [Luna low/medium][ll], [Luna high/xhigh][lh],
[Luna/Sol max][lm], [Sol low/medium][sl], [Sol high/xhigh][sh],
[Astra low/xhigh][al], [Astra medium/max][am], [Astra high/max][ah].
Refresh this table in place; do not duplicate scores in agent definitions.

[ll]: https://artificialanalysis.ai/models/comparisons/gpt-5-6-luna-low-vs-gpt-5-6-luna-medium
[lh]: https://artificialanalysis.ai/models/comparisons/gpt-5-6-luna-high-vs-gpt-5-6-luna-xhigh
[lm]: https://artificialanalysis.ai/models/comparisons/gpt-5-6-luna-vs-gpt-5-6-sol
[sl]: https://artificialanalysis.ai/models/comparisons/gpt-5-6-sol-low-vs-gpt-5-6-sol-medium
[sh]: https://artificialanalysis.ai/models/comparisons/gpt-5-6-sol-high-vs-gpt-5-6-sol-xhigh
[al]: https://artificialanalysis.ai/models/comparisons/gpt-6-astra-low-vs-gpt-6-astra-xhigh
[am]: https://artificialanalysis.ai/models/comparisons/gpt-6-astra-vs-gpt-6-astra-medium
[ah]: https://artificialanalysis.ai/models/comparisons/gpt-6-astra-high-vs-gpt-6-astra

## Codex dispatch

Give each child a concrete deliverable, necessary context, owned paths,
constraints and a verification criterion. Tell writing delegates they share
the codebase and must preserve others' edits. Select both model and
reasoning_effort explicitly. If a full-history fork inherits the parent and
disallows overrides, use fork_turns="none" with a self-contained brief or a
supported bounded history fork. Never pay for parent-model inheritance just
to transfer context. Role names do not select models.

Check the effective model and effort where the harness exposes them.
Custom-agent settings may override spawn choices; report an override rather
than claiming the requested route ran. Keep any required session record of
the actual route and escalation reason concise.
