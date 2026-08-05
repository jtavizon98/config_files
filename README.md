# Dotfiles

Personal configuration files managed with Git and GNU Stow.

## Layout

Each top-level directory is a Stow package. Its contents mirror the paths
where they should be installed relative to `$HOME`.

For example, `nvim/.config/nvim/init.lua` is installed as
`~/.config/nvim/init.lua`.

The `home` package contains portable home-directory files, including `.bashrc`,
`.vimrc`, `.bash_profile`, `.packages.txt`, and `.packages_AUR.txt`. Private
machine files remain local and are not managed by Stow.

The application packages include:

- `alacritty`
- `claude`
- `dunst`
- `fontconfig`
- `gtk`
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
```

Preview the symlinks Stow will create:

```bash
stow -n -v -t "$HOME" */
```

Install all packages:

```bash
stow -v -t "$HOME" */
```

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
alongside them. Only three entries come from this repository:

```text
~/.claude/CLAUDE.md     -> claude/.claude/CLAUDE.md
~/.claude/settings.json -> claude/.claude/settings.json
~/.claude/skills        -> claude/.claude/skills
```

Because `~/.claude` already exists as a real directory, Stow descends into it
and links only those entries; it does not replace the directory. Everything
else there is local runtime state and is excluded by `.gitignore`.

Machine-specific overrides belong in `~/.claude/settings.local.json`, which is
a regular local file and is never stowed. Per-project instructions live in each
repository as `CLAUDE.md`, symlinked to that repository's `AGENTS.md` so
Claude Code and OpenCode read the same file.

### Other local files

- Wyspr's `secrets.env` remains local and should use mode `0600`.
- GTK bookmarks (`~/.config/gtk-3.0/bookmarks`) are local only.
- OpenCode's `node_modules` and package metadata remain local.
- The separate `~/.scripts` repository is not managed here.

Machine-specific or secret values should be kept in local files and loaded
by the tracked configuration where possible. Private files should be regular
files with mode `0600`; do not place them inside this repository or use
`stow --adopt` on them.

When migrating an existing installation, copy private file contents to their
final paths before restowing, remove obsolete symlinks, then run `stow -n -v`
before applying `stow -v`. Generated `__pycache__` directories should not be
stowed.

## License

These configurations are shared as a commons. You are free to study, adapt,
and redistribute them. Please preserve attribution and share substantial
improvements under the same terms.

Licensed under the GNU General Public License version 3.
