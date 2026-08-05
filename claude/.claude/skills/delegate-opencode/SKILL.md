---
name: delegate-opencode
description: Delegate bounded work to cheaper external models through the opencode CLI (DeepSeek, GLM, Qwen, Kimi, MiniMax, GPT). Use for bulk mechanical edits, wide repository surveys, or independent tasks that can run in parallel, where spending primary-model tokens is not worth it. Not for work that depends on this conversation's context.
---

# Delegating to opencode

`opencode run` is a headless agent. It gets its own fresh context, its own
tool loop, and writes directly to the filesystem.

## Use this when

- The task is mechanical and clearly specified (rename across N files, add
  type hints, write tests against a fixed spec, port a pattern).
- You want a wide survey of a large repo and only need the summary back.
- Several independent tasks can run concurrently in the background.

## Do not use this when

- The task needs anything from this conversation — the delegate starts cold.
- The task is architectural, ambiguous, or a judgment call.
- You only need to look at an image. Read handles images natively here;
  shelling out for vision is pointless.
- A built-in subagent (Explore, Plan, general-purpose) would do. Try those first.

## Invocation

```bash
opencode run -m <provider/model> --dir <absolute/path> "<self-contained prompt>"
```

- The prompt must stand alone: state the files, the goal, and the definition
  of done. The delegate cannot see anything you know.
- `--dir` scopes it to a project. It picks up that project's `AGENTS.md`
  and the global `~/.config/opencode/AGENTS.md` automatically.
- Add `--format json` when you need to parse events rather than read prose.
- Runs routinely exceed the 120s default Bash timeout. Raise `timeout`, or
  use `run_in_background` for anything substantial or parallel.

## Model routing

| model                       | id                              | use for                                 |
| --------------------------- | ------------------------------- | --------------------------------------- |
| DeepSeek V4 Flash           | `opencode-go/deepseek-v4-flash` | default; mechanical work, cheapest       |
| GLM-5.2                     | `opencode-go/glm-5.2`           | needs real reasoning, still cheap        |
| GPT-5.6 Sol                 | `openai/gpt-5.6-sol`            | hardest reasoning; physics               |

Escalate rather than retry: if Flash returns an inconsistent or incomplete
result once, move up. Re-asking the same model the same question wastes time.
For physics correctness, do not trust Flash — use GLM-5.2 or Sol.

`opencode models` lists everything available.

## Safety: the delegate writes to disk unprompted

**Verified behaviour: `opencode run` edits files with no approval step, even
without `--auto`.** A plain `opencode run ... "fix the function"` modified the
file directly. There is no review gate. Treat every delegation as an
unsupervised write.

Protocol:

1. Check the tree before delegating: `git -C <dir> status --short`.
   Never delegate into a dirty tree you have not inspected — afterwards you
   cannot separate the delegate's edits from pre-existing ones.
2. Delegate.
3. Review what it actually did: `git -C <dir> diff`. Do not report the task
   as done based on the delegate's own summary. It reports its intent, not
   its effect.
4. For analysis only, put `Report only. Do not modify any files.` in the
   prompt. That is respected in practice, but still diff to confirm.
5. Outside a git repo, back up the target files first or refuse.
