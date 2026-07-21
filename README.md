# Dotfiles

Personal configuration files managed with Git and GNU Stow.

These configurations are shared as a commons. You are free to study, adapt,
and redistribute them. Please preserve attribution and share substantial
improvements under the same terms.

Licensed under the GNU General Public License version 3.

## Layout

Each top-level directory is a Stow package. Its contents mirror the paths
where they should be installed relative to `$HOME`.

For example, `nvim/.config/nvim/init.lua` is installed as
`~/.config/nvim/init.lua`.

The `home` package contains home-directory files, including `.bashrc`,
`.vimrc`, `.bash_profile`, `.rootrc`, `.packages.txt`, and
`.packages_AUR.txt`.

The application packages include:

- `alacritty`
- `dunst`
- `fontconfig`
- `gtk`
- `hypr`
- `matplotlib`
- `mpv`
- `networkmanager-dmenu`
- `nvim`
- `opencode`
- `qtile`
- `ranger`
- `rofi`
- `tmux`
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

Generated dependencies, caches, and secrets are intentionally not tracked.
In particular:

- OpenCode's `node_modules` and package metadata remain local.
- Qtile's `secrets.env` remains local. Copy the tracked example and set its
  permissions before starting Qtile:

  ```bash
  cp qtile/.config/qtile/secrets.env.example ~/.config/qtile/secrets.env
  chmod 600 ~/.config/qtile/secrets.env
  ```

- Wyspr's `secrets.env` remains local.
- The separate `~/.scripts` repository is not managed here.

Machine-specific or secret values should be kept in local files and loaded
by the tracked configuration where possible.
