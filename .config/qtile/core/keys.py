import os

from libqtile import qtile
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

_wayland_keys = [
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
        lazy.spawn("swaylock -f -k -l --color 181226f0 --font 'UbuntuMono Nerd Font'"),
        desc="Lock Screen",
    ),
]
_xorg_keys = [
    # Toggle TouchPad
    Key(
        ["mod1", "control"],
        "t",
        lazy.spawn("toggle-touchpad.py"),
        desc="Toggle touchpad on and off",
    ),
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


def window_to_previous_group():
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


def window_to_next_group():
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


def window_to_previous_screen():
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)
        qtile.focus_screen(i)  # focus to the screen to which the window was changed to
    else:
        group = qtile.screens[-1].group.name
        qtile.current_window.togroup(group)
        qtile.focus_screen(i)


def window_to_next_screen():
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)
        qtile.focus_screen(i)  # focus to the screen to which the window was changed to
    else:
        group = qtile.screens[0].group.name
        qtile.current_window.togroup(group)
        qtile.focus_screen(i)


def switch_screens():
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)


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
        Key(
            [mod], "space", lazy.layout.next(), desc="Move window focus to other window"
        ),
        # Launching my Programs
        Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
        Key([mod], "w", lazy.spawn(browser), desc="Launch browser"),
        Key([mod], "e", lazy.spawn(file_manager), desc="Launch file manager"),
        Key([mod], "f", lazy.spawn("thunar"), desc="Launch graphical file manager"),
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
        Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
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
            lazy.function(window_to_previous_screen),
            desc="Move current window to previous screen",
        ),
        Key(
            [mod, "shift"],
            "period",
            lazy.function(window_to_next_screen),
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
            "x",
            lazy.spawn(
                f"bash {os.path.join(script_path,'powermenu/type-1/powermenu.sh')}"
            ),
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
    ]
    _extend_keys(keys, groups, wayland=wayland)
    return keys
