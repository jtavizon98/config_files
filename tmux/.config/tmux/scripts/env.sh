#!/bin/bash
# Generic environment loader -- source this in tmux sessions or shells.
# Machine-specific or private values belong in env.local.sh (not tracked).

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ -f "$SCRIPT_DIR/env.local.sh" ]; then
    # shellcheck source=/dev/null
    source "$SCRIPT_DIR/env.local.sh"
fi
