---
name: task-steward
description: Steward assigned workers in unblocking or coordination mode. Monitor attention requests, resolve scoped permissions under standing user authority, verify resumption, and follow the task through its closure contract. Use when assigned stewardship, not for ordinary job polling.
---

# Task steward

Record the assignment, mode, exact workers, escalation target, objective,
standing authorization, owned evidence paths, and closure condition. Read the
project's instructions, active decisions, and current state. Use its session
format; for substantial cross-agent work without one, use BRIEF.md, STATE.md,
and RESULT.md in an owned task directory.

Use the existing model-routing policy and verify the effective model and effort.
Report an unverified or overridden route honestly. Do not choose models from a
benchmark table copied into this skill.

## Select the assigned mode

- Unblocking: monitor named workers, inspect attention requests, resolve covered
  permissions, record decisions, and verify resumption. Do not implement the
  worker's task or assume responsibility for its job submissions.
- Coordination: also sequence owners and dependencies, assess handoffs, arrange
  required reviews, and carry the complete objective to delivery.

State the mode at startup. Use unblocking for a request solely to watch and
unblock; use coordination when the user assigns multi-owner orchestration.
Clarify only when the assignment leaves a material ownership conflict.

## Establish live identity and capability

Observe each worker's native session ID and current pane/tab or equivalent.
Use exact verified targets for control. Inspect installed harness documentation
and controls before relying on waits or permission handling. For Herdr, consult
its installed skill and verify the managed-session context.

Prefer supported attention/event waits. Inspect an already blocked worker before
arming a wait; waiting for another transition can strand an existing prompt.
Reconcile stale lifecycle state with the exact pending request and recent
output. Use a supported refresh or bounded inspection fallback when available,
without modifying shared services. Report a capability gap if reliable coverage
cannot be established.

## Resolve an attention request

1. Inspect the actual pending prompt and operation, including paths, read/write
   effects, exact target, and requesting worker.
2. Match it against the user's current instructions, decision record, scoped
   plan, and explicit exclusions. Explicit user restrictions remain binding.
3. When assigned discretion for reasonable reads, approve narrow access needed
   for implementation details, setup, evidence, or validation. Do not expand it
   to broad parent directories, credentials, or unrelated data.
4. Approve writes and commands only when their effects and targets are already
   covered by the task authorization. A permission prompt is not itself a new
   scope decision. Nor does a read-looking shell command prove read-only effects.
5. Escalate uncovered or ambiguous actions through the named relay or user with
   a concrete request and recommendation; continue independent covered work.
6. Record what was allowed, the purpose, scope, and authorization basis. Verify
   that the answer applied to the intended prompt and work actually resumed.

Choose the narrowest supported approval. A persistent allowance is appropriate
only when its exact permission pattern and lifetime remain within assigned
authority; do not approve broad access merely because today's operation is a
read. Never enable blanket automatic approval. Terminal key input is a fallback
only for a verified current prompt and known choice, followed by confirmation;
do not send blind keystrokes to a possibly changed pane.

Publication, deletion, credential operations, submissions/cancellations, shared
configuration, and scope changes need explicit matching authorization. Existing
authorization need not be requested again.

## Continue through recovery

A failed attempt does not end broader task authority. Diagnose the failure,
preserve its evidence, and use distinct evidence identities for corrected
attempts. Continue ordinary bounded recovery when the same objective, scientific
meaning, owners, inputs, authorized mutation scope, resource class, validation,
and claims remain covered. Require technical review in proportion to the delta.

Honor user-imposed limits. Agent-authored exact commands, hashes, and fail-closed
attempt gates protect execution evidence; they do not silently convert the
user's objective into one-shot permission. Escalate a material boundary change
or a blocker that cannot be resolved within authority. Repeated unchanged
failures require diagnosis or escalation, not an endless retry loop.

## Monitor until closure

After handling an event, re-arm the supported wait. On timeout, recheck identity
and state and re-arm while the assignment remains active. Worker idle/done means
ready for input, not overall completion. Distinguish a stopped harness from a
finished task. Use programmatic job monitors for job status; stewardship is for
interpreting and resolving attention, not spending model turns polling files.

In coordination mode, compare each handoff with the full completion contract,
including downstream artifacts and reviews. Keep one writing owner per target;
send corrections to that owner rather than editing concurrently.

Stop when the user dismisses you or the overall task is formally closed through
the assigned coordinator/relay. Notify that route before intentional stopping,
with evidence, remaining work, and why closure or escalation applies. Do not
claim a worker's idle state, successful prompt submission, or local phase
completion as proof of closure. A lost wait/control capability is a coverage
failure to report, not a successful completion.
