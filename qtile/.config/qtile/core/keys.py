import os

from libqtile.config import Key
from libqtile.lazy import lazy

from core.vars import (
    browser,
    file_manager,
    launcher,
    mod,
    music_player,
    script_path,
    terminal,
)

# from libqtile.utils import guess_terminal


def _wyspr_toggle(qtile, output, live_preview=True):
    window = qtile.current_window
    app = None
    title = None
    if window is not None:
        title = str(window.name) if window.name else None
        try:
            wm_class = window.get_wm_class()
            if isinstance(wm_class, (list, tuple)):
                app = " ".join(item for item in wm_class if item)
            elif wm_class:
                app = str(wm_class)
        except (AttributeError, TypeError):
            pass

    command = [
        "wyspr",
        "--output",
        output,
    ]
    if not live_preview:
        command.append("--no-live-preview")
    if app:
        command.extend(["--app", app])
    if title:
        command.extend(["--title", title])
    qtile.spawn(command)


_wayland_keys = [
    # Voice dictation (toggle mode - press to start/stop)
    Key(
        [mod],
        "v",
        lazy.function(_wyspr_toggle, output="clipboard", live_preview=True),
        desc="Toggle voice recording with live GUI",
    ),
    Key(
        [mod, "shift"],
        "v",
        lazy.function(_wyspr_toggle, output="clipboard", live_preview=False),
        desc="Toggle voice recording with compact GUI",
    ),
    # Take screenshot
    Key(
        [],
        "Print",
        lazy.spawn(f"screenshot"),
        desc="Screen grab",
    ),
    # Lock screen
    Key(
        ["mod1", "control"],
        "l",
        lazy.spawn("hyprlock"),
        desc="Lock Screen",
    ),
]
_xorg_keys = [
    # Lock screen
    Key(
        ["mod1", "control"],
        "l",
        lazy.spawn("betterlockscreen -l dimblur"),
        desc="Lock Screen",
    ),
    # Switch between windows
    Key(
        ["mod1"],
        "Tab",
        lazy.spawn("rofi -show window -theme catppuccin-macchiato"),
        desc="Switch between windows",
    ),
    # Take screenshot
    Key(
        [],
        "Print",
        lazy.spawn("gnome-screenshot -i"),
        desc="Launch screen shooting utility",
    ),
]


def move_window_to_screen(qtile, offset):
    if qtile.current_window is None:
        return

    current = qtile.screens.index(qtile.current_screen)
    target = (current + offset) % len(qtile.screens)
    qtile.current_window.toscreen(target)
    qtile.focus_screen(target)


def _extend_keys(keys, groups, wayland=True):
    if wayland:
        keys += _wayland_keys
    else:
        keys += _xorg_keys

    for i, workspace in enumerate(groups):
        keys.extend(
            [
                # mod1 + letter of group = switch to group
                Key(
                    [mod],
                    f"{i+1}",
                    lazy.group[workspace.name].toscreen(),
                    desc=f"Switch to group {workspace.name}",
                ),
                # mod1 + shift + letter of group = switch to & move focused window to group
                Key(
                    [mod, "shift"],
                    f"{i+1}",
                    lazy.window.togroup(workspace.name, switch_group=True),
                    desc=f"Switch to & move focused window to group {workspace.name}",
                ),
                # mod1 + control + shift + letter of group = move focused window to group
                Key(
                    [mod, "control", "shift"],
                    f"{i+1}",
                    lazy.window.togroup(workspace.name),
                    desc=f"Move focused window to group {workspace.name}",
                ),
            ]
        )


def init_keys(groups, wayland=True):
    keys = [
        # A list of available commands that can be bound to keys can be found
        # at https://docs.qtile.org/en/latest/manual/config/lazy.html
        # Switch between windows
        Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
        Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
        Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
        Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
        # Launching my Programs
        Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
        Key([mod], "w", lazy.spawn(browser), desc="Launch browser"),
        Key([mod], "e", lazy.spawn(file_manager), desc="Launch file manager"),
        Key([mod], "f", lazy.spawn("thunar"), desc="Launch graphical file manager"),
        Key(
            [mod],
            "t",
            lazy.spawn(
                f"{terminal} -e bash -lc 'tzync copy; status=$?; "
                'read -rp "Press Enter to close..."; exit "$status"\''
            ),
            desc="Copy selected tzync profiles",
        ),
        Key(
            [mod, "shift"],
            "t",
            lazy.spawn(
                f"{terminal} -e bash -lc 'tzync sync; status=$?; "
                'read -rp "Press Enter to close..."; exit "$status"\''
            ),
            desc="Sync selected tzync profiles",
        ),
        Key([mod, "shift"], "m", lazy.spawn(music_player), desc="Launch music player"),
        Key([mod], "p", lazy.spawn(launcher), desc="Run Launcher"),
        Key([mod], "b", lazy.spawn("rofi-bluetooth"), desc="Launch bluetooth manager"),
        Key(
            [mod],
            "i",
            lazy.spawn("networkmanager_dmenu"),
            desc="Launch network manager",
        ),
        # Toggle between different layouts as defined below
        Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
        Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
        Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
        Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
        Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
        # Move windows between left/right columns or move up/down in current stack.
        # Moving out of range in Columns layout will create new column.
        Key(
            [mod, "shift"],
            "h",
            lazy.layout.shuffle_left(),
            desc="Move window to the left",
        ),
        Key(
            [mod, "shift"],
            "l",
            lazy.layout.shuffle_right(),
            desc="Move window to the right",
        ),
        Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
        Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
        # Move windows between screens
        Key(
            [mod, "shift"],
            "comma",
            lazy.function(move_window_to_screen, offset=-1),
            desc="Move current window to previous screen",
        ),
        Key(
            [mod, "shift"],
            "period",
            lazy.function(move_window_to_screen, offset=1),
            desc="Move current window to next screen",
        ),
        # Grow windows. If current window is on the edge of screen and direction
        # will be to screen edge - window would shrink.
        Key(
            [mod, "control"],
            "h",
            lazy.layout.grow_left(),
            desc="Grow window to the left",
        ),
        Key(
            [mod, "control"],
            "l",
            lazy.layout.grow_right(),
            desc="Grow window to the right",
        ),
        Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
        Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
        Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
        Key(
            [mod],
            "m",
            lazy.layout.maximize(),
            desc="Toggle window between minimum and maximum sizes",
        ),
        # Toggle between split and unsplit sides of stack.
        # Split = all windows displayed
        # Unsplit = 1 window displayed, like Max layout, but still with
        # multiple stack panes
        Key(
            [mod, "shift"],
            "Return",
            lazy.layout.toggle_split(),
            desc="Toggle between split and unsplit sides of stack",
        ),
        # Switch focus between monitors
        Key([mod], "period", lazy.next_screen(), desc="Move focus to next monitor"),
        Key([mod], "comma", lazy.prev_screen(), desc="Move focus to prev monitor"),
        # Power Menu
        Key(
            [mod, "shift"],
            "q",
            lazy.spawn(os.path.join(script_path, "powermenu")),
            desc="Display power menu",
        ),
        # Shut down system
        Key(
            [mod, "shift", "control"],
            "x",
            lazy.spawn("systemctl poweroff"),
            desc="Shutdown system",
        ),
        # Emoji picker
        Key([mod, "shift"], "e", lazy.spawn("rofimoji"), desc="Show emoji picker"),
        # Special charachter picker
        Key(
            [mod, "shift"],
            "s",
            lazy.spawn("rofimoji -f latin-1_supplement -r Special"),
            desc="Show emoji picker",
        ),
        # Change keyboard layout
        Key(
            [mod],
            "space",
            lazy.widget["keyboardlayout"].next_keyboard(),
            desc="Next keyboard layout",
        ),
        # Function Keys
        Key(
            [],
            "XF86AudioRaiseVolume",
            lazy.spawn("volumectl -i"),
            desc="Raise Volume",
        ),
        Key(
            [],
            "XF86AudioLowerVolume",
            lazy.spawn("volumectl -d"),
            desc="Lower Volume",
        ),
        Key(
            [],
            "XF86AudioMute",
            lazy.spawn("volumectl -m"),
            desc="Mute toggle",
        ),
        Key(
            [],
            "XF86MonBrightnessDown",
            lazy.spawn("pylight -d"),
            desc="Decrease Brightness",
        ),
        Key(
            [],
            "XF86MonBrightnessUp",
            lazy.spawn("pylight -i"),
            desc="Increase Brightness",
        ),
        Key(
            [],
            "XF86AudioPlay",
            lazy.spawn("playerctl play-pause"),
            desc="Toggle play/pause of media",
        ),
        Key(
            [],
            "XF86AudioNext",
            lazy.spawn("playerctl next"),
            desc="Switch to next track",
        ),
        Key(
            [],
            "XF86AudioPrev",
            lazy.spawn("playerctl previous"),
            desc="Switch to previous track",
        ),
        Key(
            ["mod1"],
            "period",
            lazy.spawn("playerctl next"),
            desc="Switch to next track",
        ),
        Key(
            ["mod1"],
            "comma",
            lazy.spawn("playerctl previous"),
            desc="Switch to previous track",
        ),
        Key(
            ["mod1", "control"],
            "t",
            lazy.spawn("toggle_colors"),
            desc="Toggle light and dark theme",
        ),
        # Toggle TouchPad
        Key(
            [mod, "control"],
            "t",
            lazy.spawn("toggle-touchpad.py"),
            desc="Toggle touchpad on and off",
        ),
    ]
    _extend_keys(keys, groups, wayland=wayland)
    return keys
