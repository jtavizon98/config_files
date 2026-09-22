# Dotfiles

Personal configuration files managed with Git and GNU Stow.

## Layout

Each top-level directory is a Stow package. Its contents mirror the paths
where they should be installed relative to `$HOME`.

For example, `nvim/.config/nvim/init.lua` is installed as
`~/.config/nvim/init.lua`.

The `home` package contains laptop home-directory files, including `.bashrc`,
`.vimrc`, `.bash_profile`, `.packages.txt`, and `.packages_AUR.txt`. Do not Stow
this package on remote hosts. Their machine-specific shell files remain local
and are not managed by this repository.

The application packages include:

- `agent-skills`
- `alacritty`
- `claude`
- `codex`
- `dunst`
- `environment`
- `fontconfig`
- `gtk`
- `herdr`
- `hypr`
- `matplotlib`
- `mpv`
- `networkmanager-dmenu`
- `nvim`
- `paru`
- `opencode`
- `qtile`
- `ranger`
- `rofi`
- `tmux`
- `tzync`
- `wyspr`
- `zathura`

## Installation

Install GNU Stow using your system package manager, then clone this
repository into `~/.dotfiles`:

```bash
git clone https://github.com/jtavizon98/config_files.git ~/.dotfiles
cd ~/.dotfiles
mkdir -p ~/.config/herdr
```

The real Herdr directory must exist before stowing so Stow links only the
tracked `config.toml` and leaves runtime state in `~/.config/herdr`.

Preview the symlinks Stow will create:

```bash
stow -n -v -t "$HOME" */
```

Install all packages:

```bash
stow -v -t "$HOME" */
```

This full installation is intended for the laptop. On remote hosts, install
only the explicitly required application packages and leave the `home` package
unstowed.

Install only selected packages:

```bash
stow -v -t "$HOME" home nvim tmux
```

Reinstall or update links after changing the layout:

```bash
stow -R -v -t "$HOME" */
```

Remove a package's links without deleting the files in this repository:

```bash
stow -D -v -t "$HOME" nvim
```

## Packages

From the repository root, reinstall the packages listed for the system and
the AUR:

```bash
sudo pacman -Syu
sudo pacman -S --needed - < home/.packages.txt
paru -S --needed - < home/.packages_AUR.txt
```

The package lists may contain packages that have been renamed or removed
since they were created. Review any errors and update the lists as needed.

## Environment Ownership

On the Arch laptop, system executable paths come from `/etc/profile` and its
`/etc/profile.d/` snippets. Alacritty starts Bash as a login shell so those
distribution-maintained files remain authoritative. Do not copy their paths
into `environment.d` or other user configuration.

The laptop `.bashrc` adds only personal prefixes: `~/.local/bin`, `~/.scripts`,
and `~/perl5/bin`. Files under `environment.d` are reserved for graphical
session variables, not `PATH`.

Remote hosts keep their own shell startup files outside this repository. Put
host-wide user-space installations in that host's private shell configuration;
keep virtual environments and toolchain setup owned by the relevant project.

## Updating Configurations

Edit the files in `~/.dotfiles`; the installed files in `$HOME` are
symlinks. Review and commit changes normally with Git:

```bash
git status
git diff
git add .
git commit
git push
```

To add another configuration, create a package directory and mirror its
destination under `$HOME`. For example:

```text
new-app/.config/new-app/config.toml
```

Then install it with:

```bash
stow -t "$HOME" new-app
```

Existing real files can conflict with Stow. Back them up or move them out
of the way before installing a package. Use `stow -n -v` first to preview
the result.

## Local Files

Generated dependencies, caches, secrets, and machine-specific values are
intentionally not tracked. Before using the configurations, create these
local files:

### Qtile local config

```bash
cp qtile/.config/qtile/core/local.example.py \
   ~/.config/qtile/core/local.py
chmod 600 ~/.config/qtile/core/local.py
```

Edit `~/.config/qtile/core/local.py` and set your weather location,
wallpaper path, scripts directory, network interface, and touchpad
identifiers.

The example remains in the repository and is excluded from Stow. The local
file is a regular file under `~/.config`, not a symlink into this repository.

### Qtile API secrets

```bash
cp qtile/.config/qtile/secrets.env.example ~/.config/qtile/secrets.env
chmod 600 ~/.config/qtile/secrets.env
```

Set `OPENWEATHER_API_KEY` in the file.

### Tmux environment

```bash
cp tmux/.config/tmux/scripts/env.local.example.sh \
   ~/.config/tmux/scripts/env.local.sh
chmod 600 ~/.config/tmux/scripts/env.local.sh
```

Place machine-specific exports (private paths and toolchain variables) in
`env.local.sh`.  Source `env.sh` from tmux sessions or shells; it
automatically loads `env.local.sh` when present.

The tracked `env.sh` is installed by Stow. The example is not installed, and
`env.local.sh` remains a regular local file.

### Claude Code

`~/.claude` is a mixed directory: Claude Code writes credentials, sessions,
history, and caches there at runtime, and Stow links the tracked files
alongside them. Only two entries come from this repository:

```text
~/.claude/CLAUDE.md     -> claude/.claude/CLAUDE.md
~/.claude/settings.json -> claude/.claude/settings.json
```

Because `~/.claude` already exists as a real directory, Stow descends into it
and links only those entries; it does not replace the directory. Everything
else there is local runtime state and is excluded by `.gitignore`.

Machine-specific overrides belong in `~/.claude/settings.local.json`, which is
a regular local file and is never stowed. OpenCode is the authoritative harness:
the global `CLAUDE.md` imports `~/.config/opencode/AGENTS.md`, while per-project
`CLAUDE.md` files link to their repository's `AGENTS.md`. Claude-specific
settings remain here only to support it as a fallback harness.

### Codex configuration

The `codex` package owns portable subagent routing guidance in
`codex/.codex/AGENTS.md`. It defines physics, intelligence, availability and
taste, and guides the primary to decompose work and choose the highest-
availability suitable model and effort. Its single numerical table covers
Luna, Sol and Astra, with availability derived from Artificial Analysis cost
per task and effort-specific intelligence and CritPt evidence. Missing data
are explicit. Concrete bypass reasons, bounded escalation and a default limit
on expensive delegations apply regardless of the primary model; role names
do not assign models. The user's primary model and effort remain their choice.

For the standard Codex home, preview and install with:

```bash
stow -n -v -t "$HOME" codex
stow -v -t "$HOME" codex
```

When `~/.codex` is a symlink or `CODEX_HOME` names a different existing directory,
link only the tracked `AGENTS.md` into the resolved Codex home. Inspect both
paths first and preserve any existing instructions; do not overwrite a file
or replace the Codex home directory. Keep `config.toml`, credentials, caches,
plugins and session state local. This package does not manage them.

Start a new Codex session to load changed global instructions. Existing custom
agents may override explicit spawn choices; check their model and reasoning
settings when a route does not match the policy.

### OpenCode configuration

Global behavioral policy lives in `opencode/.config/opencode/AGENTS.md`.
`opencode.jsonc`, the custom agents, and `cli.json` use native OpenCode V2
configuration. `cli.json` owns portable terminal preferences; do not recreate
the retired V1 `tui.json`. Reusable skills are owned by the shared
`agent-skills` package below.
Use a fresh OpenCode session to verify changed skill discovery; checkpoint
active work before restarting any existing process.

### Shared agent skills

`agent-skills/.agents/skills/<name>/SKILL.md` is the single maintained source
for personal skills used by Codex and OpenCode. Both clients discover
`~/.agents/skills`. Install only this package to share skills without changing
either client's provider, permissions, model, or runtime configuration:

```bash
stow -n -v -t "$HOME" agent-skills
stow -v -t "$HOME" agent-skills
```

The package contains scientific-coding, relay, task-steward, grilling, unslop,
report-writing, wizard, and frontend-design. Preserve third-party source
attribution and bundled licenses. Keep project-specific skills in each
repository's `.agents/skills`, and project policy, scientific evidence, private
transcripts, host identities, and credentials outside this portable package.

When migrating from the former OpenCode skill directory, inspect exact source
and destination paths first. Preserve existing contents and local edits; move
the skill directories with their resources into this package. Remove only
verified obsolete installation links, including old Codex skill links and the
report-writing link that points back to OpenCode. Do not leave duplicate skill
names in several discovery roots. Preview Stow before installing and verify
discovery in fresh processes of both clients without restarting live work.
Rollback restores the prior source locations and exact links from the migration
record; do not overwrite unrelated skills or runtime state.

The three new workflows are instruction-only. Scientific coding scales its
trace to the task. Relay and stewardship require assigned targets and existing
authority; installing them does not start workers or approve actions.

### Herdr configuration

The `herdr` package links only `~/.config/herdr/config.toml`. Herdr writes logs,
session state, and plugin metadata beside that link at runtime; those files are
local, ignored by Git and Stow, and must not be moved into repository history.

### Other local files

- Wyspr's `secrets.env` remains local and should use mode `0600`.
- GTK bookmarks (`~/.config/gtk-3.0/bookmarks`) are local only.
- OpenCode's `node_modules` and package metadata remain local.
- The separate `~/.scripts` repository is not managed here.

OpenCode autoupdates are disabled because replacing the running npm-installed
binary can leave an incomplete package on NFS-backed home directories. Exit all
OpenCode clients before upgrading it manually:

```bash
npm install --global opencode-ai@latest
opencode --version
```

Machine-specific or secret values should be kept in local files. Private files
should be regular files with mode `0600`; do not place them inside this
repository or use `stow --adopt` on them.

When migrating an existing installation, copy private file contents to their
final paths before restowing, remove obsolete symlinks, then run `stow -n -v`
before applying `stow -v`. Generated `__pycache__` directories should not be
stowed.

## License

These configurations are shared as a commons. You are free to study, adapt,
and redistribute them. Please preserve attribution and share substantial
improvements under the same terms.

Licensed under the GNU General Public License version 3.
