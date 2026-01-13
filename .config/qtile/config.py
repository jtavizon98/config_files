import os
import subprocess

from libqtile import bar, hook, qtile
from libqtile.config import Match, Screen

from core.colors import catppuccin
from core.groups import init_groups
from core.keys import init_keys
from core.mouse import init_mouse
from core.vars import bar_font_size, wallpaper_background
from core.widgets import init_widgets
from core.layouts import init_layouts

xorg_flag = qtile.core.name == "x11"
wayland_flag = qtile.core.name == "wayland"

groups = init_groups()
keys = init_keys(groups, wayland=wayland_flag)

widget_defaults = {
    "font": "UbuntuMono Nerd Font Bold",
    "fontsize": bar_font_size,
    "padding": 2,
    "background": catppuccin["red"],
}

layouts, floating_layout = init_layouts()


def init_screens():
    screens = [
        Screen(
            wallpaper=wallpaper_background,
            wallpaper_mode="fill",
            top=bar.Bar(
                widgets=init_widgets(),
                background="ffffff00",
                size=35,
                margin=[4, 6, 0, 6],
            ),
        )
        for i in range(2)
    ]

    return screens


if __name__ in ["config", "__main__"]:
    screens = init_screens()

mouse, wl_input_rules = init_mouse(wayland=wayland_flag)

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True


from libqtile import hook

@hook.subscribe.client_new
def force_popup_focus(window):
    # If it's a Zen window with no name (the 'Replace' prompt)
    if window.get_wm_class() and "zen" in window.get_wm_class():
        if not window.name or window.name == "":
            # Force it to be floating, topmost, and focused
            window.floating = True
            window.cmd_bring_to_front()
            window.cmd_focus()

@hook.subscribe.startup_once
def start_once(wayland=True):
    command = ["dunst"]
    if not wayland:
        command.extend(
            [
                "lxsession",
                "picom",
                "nm-applet",
                "blueman-applet",
                'xinput set-prop "VEN_04F3:00 04F3:3242 Touchpad" "libinput Natural Scrolling Enabled" 1',
            ]
        )
    else:
        command.extend(["/usr/lib/hyprpolkitagent/hyprpolkitagent"])
    command = [line + " & " for line in command]
    command_str = "".join(command)
    subprocess.Popen(
        command_str,
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        preexec_fn=os.setpgrp,
    )


# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
