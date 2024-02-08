#!/usr/bin/python3

# === IMPORTS =================================================================

import os
import subprocess

from libqtile import bar, hook, layout, qtile
from libqtile.backend.wayland.inputs import InputConfig
from libqtile.command import lazy
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

# from libqtile.utils import guess_terminal
import API_keys

# === VARIABLES ===============================================================
mod = "mod4"  # Sets mod key to SUPER/WINDOWS
terminal = "alacritty"  # guess_terminal()
browser = "firefox"
file_manager = "alacritty -e ranger"
launcher = "rofi -show drun -theme catppuccin-macchiato"
# music_player = "alacritty -e spt"
music_player = "spotify"
scripts = "/home/jairot/.scripts/"
location = ["Munich, DE", "2867714"]  # for the OpenWeather widget
# location = ["Guadalajara, MX", "4005539"]   # for the OpenWeather widget
wallpaper_background = (
    "/home/jairot/Pictures/Wallpapers/JWST_NIRcam_ring_nebula_eye.png"
)

xorg_flag = qtile.core.name == "x11"
wayland_flag = qtile.core.name == "wayland"

catppuccin = {
    "crust": ["#181926", "#181926"],
    "mantle": ["#1e2030", "#1e2030"],
    "base": ["#24273a", "#24273a"],
    "surface0": ["#363a4f", "#363a4f"],
    "surface1": ["#494d64", "#494d64"],
    "surface2": ["#5b6078", "#5b6078"],
    "overlay0": ["#6e738d", "#6e738d"],
    "overlay1": ["#8087a2", "#8087a2"],
    "overlay2": ["#939ab7", "#939ab7"],
    "subtext0": ["#a5adcb", "#a5adcb"],
    "subtext1": ["#b8c0e0", "#b8c0e0"],
    "text": ["#cad3f5", "#cad3f5"],
    "lavander": ["#b7bdf8", "#b7bdf8"],
    "blue": ["#8aadf4", "#8aadf4"],
    "sapphire": ["#7dc4e4", "#7dc4e4"],
    "sky": ["#91d7e3", "#91d7e3"],
    "teal": ["#8bd5ca", "#8bd5ca"],
    "green": ["#a6da95", "#a6da95"],
    "yellow": ["#eed49f", "#eed49f"],
    "peach": ["#f5a97f", "#f5a97f"],
    "maroon": ["#ee99a0", "#ee99a0"],
    "red": ["#ed8796", "#ed8796"],
    "mauve": ["#c6a0f6", "#c6a0f6"],
    "pink": ["#f5bde6", "#f5bde6"],
    "flamingo": ["#f0c6c6", "#f0c6c6"],
    "rosewater": ["#f4dbd6", "#f4dbd6"],
}

# === FUNCTIONS ===============================================================


def WindowToPrevGroup(Qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


def WindowToNextGroup(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


def WindowToPreviousScreen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)
        qtile.focus_screen(i)  # focus to the screen to which the window was changed to
    else:
        group = qtile.screens[-1].group.name
        qtile.current_window.togroup(group)
        qtile.focus_screen(i)


def WindowToNextScreen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)
        qtile.focus_screen(i)  # focus to the screen to which the window was changed to
    else:
        group = qtile.screens[0].group.name
        qtile.current_window.togroup(group)
        qtile.focus_screen(i)


def SwitchScreens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)


# === KEYBINDINGS =============================================================
keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Launching my Programs
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "w", lazy.spawn(browser), desc="Launch browser"),
    Key([mod], "e", lazy.spawn(file_manager), desc="Launch file manager"),
    Key([mod], "f", lazy.spawn("thunar"), desc="Launch graphical file manager"),
    Key([mod, "shift"], "m", lazy.spawn(music_player), desc="Launch music player"),
    Key([mod], "p", lazy.spawn(launcher), desc="Run Launcher"),
    Key([mod], "b", lazy.spawn("rofi-bluetooth"), desc="Launch bluetooth manager"),
    Key([mod], "i", lazy.spawn("networkmanager_dmenu"), desc="Launch network manager"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
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
        lazy.function(WindowToPreviousScreen),
        desc="Move current window to previous screen",
    ),
    Key(
        [mod, "shift"],
        "period",
        lazy.function(WindowToNextScreen),
        desc="Move current window to next screen",
    ),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
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
        lazy.spawn(f"bash {scripts}powermenu/type-1/powermenu.sh"),
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
        lazy.spawn(f"python {scripts}volume_up.py"),
        desc="Raise Volume",
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn(f"python {scripts}volume_down.py"),
        desc="Lower Volume",
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn(f"python {scripts}mute_toggle.py"),
        desc="Mute toggle",
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn(f"python {scripts}brightness_down.py"),
        desc="Decrease Brightness",
    ),
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn(f"python {scripts}brightness_up.py"),
        desc="Increase Brightness",
    ),
    Key(
        [],
        "XF86AudioPlay",
        lazy.spawn("playerctl play-pause"),
        desc="Toggle play/pause of media",
    ),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Switch to next track"),
    Key(
        [],
        "XF86AudioPrev",
        lazy.spawn("playerctl previous"),
        desc="Switch to previous track",
    ),
    Key(["mod1"], "period", lazy.spawn("playerctl next"), desc="Switch to next track"),
    Key(
        ["mod1"],
        "comma",
        lazy.spawn("playerctl previous"),
        desc="Switch to previous track",
    ),
]

if xorg_flag:
    keys.extend(
        [
            # Toggle TouchPad
            Key(
                ["mod1", "control"],
                "t",
                lazy.spawn(f"python {scripts}toggle-touchpad.py"),
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
    )
if wayland_flag:
    keys.extend(
        [
            # Take screenshot
            Key(
                [],
                "Print",
                lazy.spawn(f"bash {scripts}/screenshot.sh"),
                desc="Screen grab",
            ),
            # Lock screen
            Key(
                ["mod1", "control"],
                "l",
                lazy.spawn(
                    "swaylock -f -k -l --color 181226f0 --font 'UbuntuMono Nerd Font'"
                ),
                desc="Lock Screen",
            ),
        ]
    )

# === Workspaces ==============================================================

# Groups are really Workspaces
groups = [
    Group("󰀘 ", layout="monadtall"),
    Group("󰃭 ", layout="monadtall"),
    Group(" ", layout="monadtall"),
    Group(" ", layout="monadtall"),
    Group(" ", layout="monadtall"),
    Group("󰈰", layout="monadtall"),
    Group("󰎈", layout="monadtall"),
    Group("󰙊", layout="floating"),
]

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

# === PANEL ===================================================================

layout_theme = {
    "border_width": 2,
    "margin": 20,
    "border_focus": catppuccin["pink"],
    "border_normal": catppuccin["base"],
}

layouts = [
    #    layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    #    layout.Stack(stacks=2, **layout_theme),
    #    layout.RatioTile(
    #        **layout_theme,
    #        clockwise=True,
    #        new_client_position='bottom',
    #        ratio = 0.5
    #    ),
    #    layout.Spiral(
    #        **layout_theme,
    #        clockwise=True,
    #        new_client_position='after_current',
    #        ratio = 0.5
    #    ),
    layout.Floating(**layout_theme),
]

# DEFAULT WIDGET SETTINGS
widget_defaults = dict(
    font="UbuntuMono Nerd Font Bold",
    fontsize=20,
    padding=2,
    background=catppuccin["red"],
)
extension_defaults = widget_defaults.copy()

# Qtile extras rounded corners
decorations_group = {
    "decorations": [
        RectDecoration(
            use_widget_background=True,
            filled=True,
            radius=18,
            group=True,
        )
    ]
}


def InitWidgetsList():
    widgets_list = [
        widget.TextBox(
            text="   ",
            font="UbuntuMono Nerd Font",
            background=catppuccin["blue"],
            foreground=catppuccin["surface0"],
            padding=5,
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(launcher)},
            fontsize=20,
            **decorations_group,
        ),
        widget.Spacer(background="ffffff00", length=3),
        widget.TextBox(
            text=" ",
            font="UbuntuMono Nerd Font",
            background=catppuccin["mauve"],
            foreground=catppuccin["surface0"],
            padding=5,
            fontsize=24,
            **decorations_group,
        ),
        widget.GroupBox(
            font="UbuntuMono Nerd Font",
            fontsize=20,
            margin_y=3,
            margin_x=0,
            padding_y=5,
            padding_x=3,
            borderwidth=3,
            active=catppuccin["surface0"],
            inactive=catppuccin["overlay2"],
            rounded=True,
            highlight_color=catppuccin["pink"],
            highlight_method="line",
            this_current_screen_border=catppuccin["green"],
            this_screen_border=catppuccin["flamingo"],
            other_current_screen_border=catppuccin["teal"],
            other_screen_border=catppuccin["maroon"],
            foreground=catppuccin["mantle"],
            background=catppuccin["mauve"],
            **decorations_group,
        ),
        widget.TextBox(
            text=" ",
            font="UbuntuMono Nerd Font",
            background=catppuccin["mauve"],
            foreground=catppuccin["surface0"],
            padding=5,
            fontsize=18,
            **decorations_group,
        ),
        widget.Spacer(background="ffffff00", length=3),
        widget.TextBox(
            text="  ",
            font="UbuntuMono Nerd Font",
            foreground=catppuccin["surface0"],
            background=catppuccin["yellow"],
            padding=5,
            fontsize=18,
            **decorations_group,
        ),
        widget.CurrentLayout(
            fmt="{} ",
            foreground=catppuccin["surface0"],
            background=catppuccin["yellow"],
            padding=5,
            **decorations_group,
        ),
        widget.Spacer(background="ffffff00", length=bar.STRETCH),
        widget.OpenWeather(
            background=catppuccin["sapphire"],
            foreground=catppuccin["surface0"],
            app_key=API_keys.OpenWeather,
            location=location[0],
            format="{location_city}: {icon} {main_temp:.0f}°{units_temperature}",
            fmt=" {}",
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(
                    f"xdg-open https://openweathermap.org/city/{location[1]}"
                )
            },
            **decorations_group,
        ),
        widget.TextBox(
            text="|",
            background=catppuccin["sapphire"],
            foreground=catppuccin["overlay1"],
            font="Ubuntu Mono",
            padding=5,
            fontsize=24,
            **decorations_group,
        ),
        widget.Clock(
            background=catppuccin["sapphire"],
            foreground=catppuccin["surface0"],
            format="  %H:%M  %a %d.%m.%Y ",
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(
                    f"xdg-open https://calendar.google.com"
                )
            },
            **decorations_group,
        ),
        widget.Spacer(background="ffffff00", length=bar.STRETCH),
    ]

    if xorg_flag:
        widgets_list.append(widget.Systray(background=None, icon_size=27, padding=5))
    elif wayland_flag:
        # widgets_list.append(
        #    widget.Pomodoro(
        #        background = catppuccin['red'],
        #        color_inactive = catppuccin['surface0'],
        #        color_active = catppuccin['surface0'],
        #        color_break = catppuccin['surface0'],
        #        font = "UbuntuMono Nerd Font",
        #        fmt = " {} ",
        #        prefix_inactive = ' ',
        #        prefix_active = '祥 ',
        #        prefix_paused = '  ',
        #        prefix_break = ' ',
        #        prefix_long_break = ' ',
        #        #length_pomodori = 0.25,
        #        #length_short_break = 0.25,
        #        #length_long_break = 0.25,
        #        **decorations_group
        #    )
        # )
        # widgets_list.append(
        #    widget.Spacer(
        #        background="ffffff00",
        #        length=3
        #    )
        # )
        widgets_list.append(
            # widget.Bluetooth(
            #     # adapter_format = '[{powered} {discovery}] {name}  ',
            #     # adapter_paths = [],
            #     # default_text = "{connected_devices}",
            #     # default_show_battery = True,
            #     # device_battery_format = '{battery}%',
            #     # device_format = "[{symbol}] {name} {battery_level}",
            #     # symbol_connected = "󰂱",
            #     # symbol_paired = "-",
            #     # symbol_powered = ('󰂯', '󰂲'),
            #     fmt=" 󰂯 {} ",
            #     hci="/dev_14_3F_A6_67_4E_88",  # /org/bluez/hci0/dev_
            widget.TextBox(
                text=" 󰂯 ",
                padding=5,
                fontsize=18,
                font="UbuntuMono Nerd Font",
                foreground=catppuccin["surface0"],
                background=catppuccin["sky"],
                mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("rofi-bluetooth")},
                **decorations_group,
            )
        )
        widgets_list.append(widget.Spacer(background="ffffff00", length=3))
        widgets_list.append(
            widget.Wlan(
                background=catppuccin["lavander"],
                foreground=catppuccin["surface0"],
                format=" 󰖩 ",
                disconnected_message=" 󰖪  ",
                interface="wlp2s0",
                update_interval=5,
                mouse_callbacks={
                    "Button1": lambda: qtile.cmd_spawn("networkmanager_dmenu")
                },
                **decorations_group,
            )
        )
        widgets_list.append(
            widget.Wlan(
                background=catppuccin["lavander"],
                foreground=catppuccin["surface0"],
                fmt="{} ",
                format="{percent:2.0%}",
                disconnected_message="",
                interface="wlp2s0",
                update_interval=5,
                mouse_callbacks={
                    "Button1": lambda: qtile.cmd_spawn("networkmanager_dmenu")
                },
                **decorations_group,
            )
        )
    widgets_list.append(widget.Spacer(background="ffffff00", length=3))
    widgets_list.append(
        widget.KeyboardLayout(
            configured_keyboards=["us", "latam", "de"],
            display_map={"us": "US", "latam": "ES", "de": "DE"},
            fmt=" 󰌌  {} ",
            foreground=catppuccin["surface0"],
            background=catppuccin["maroon"],
            padding=5,
            **decorations_group,
        )
    )
    widgets_list.append(widget.Spacer(background="ffffff00", length=3))
    widgets_list.append(
        widget.Battery(
            format="{char} {percent:2.0%} ",
            full_char=" 󰂄",
            charge_char=" 󰂄",
            discharge_char=" 󰁹",
            empty_char=" 󰂎",
            show_short_text=False,
            foreground=catppuccin["surface0"],
            background=catppuccin["green"],
            low_percentage=0.15,  # 0 < x < 1
            low_foreground=catppuccin["red"],
            notify_below=20,  # 0 < x < 100
            notification_timeout=0,
            padding=5,
            **decorations_group,
        )
    )
    widgets_list.append(widget.Spacer(background="ffffff00", length=3))
    widgets_list.append(
        widget.TextBox(
            text="  󰐥  ",
            font="UbuntuMono Nerd Font",
            foreground=catppuccin["red"],
            background=catppuccin["crust"],
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(
                    f"bash {scripts}powermenu/type-1/powermenu.sh"
                )
            },
            padding=0,
            fontsize=24,
            **decorations_group,
        )
    )
    return widgets_list


def InitWidgetsScreenExternal():
    widgets = InitWidgetsList()
    del widgets[-11]  # Slicing removes unwanted widgets (systray) on external moitor
    return widgets


def InitWidgetsScreen():
    widgets = InitWidgetsList()
    return widgets  # Laptop screen will display all widgets in widgets_list


def InitScreens():
    screenf = lambda x: Screen(
        wallpaper=wallpaper_background,
        wallpaper_mode="fill",
        top=bar.Bar(widgets=x, background="ffffff00", size=35, margin=[4, 6, 0, 6]),
    )
    if xorg_flag:
        screens_gen = [
            screenf(InitWidgetsScreen()),
            screenf(InitWidgetsScreenExternal()),
        ]
    elif wayland_flag:
        screens_gen = [screenf(InitWidgetsScreen()) for i in range(2)]
    return screens_gen


if __name__ in ["config", "__main__"]:
    widgets_list = InitWidgetsList()
    widgets_screen = InitWidgetsScreen()
    screens = InitScreens()


# === Floating windows ========================================================

mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# === HOOKS ===================================================================

if xorg_flag:
    autostart = "/.config/qtile/X11.sh"
elif wayland_flag:
    autostart = "/.config/qtile/wayland.sh"


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + autostart])


# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = {
    "1739:52759:SYNA32B5:00 06CB:CE17 Touchpad": InputConfig(
        natural_scroll=True, tap=True, dwt=True
    )
}

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
