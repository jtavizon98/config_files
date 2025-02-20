import os
import subprocess

# from libqtile.utils import guess_terminal
from libqtile import bar, hook, layout, qtile
from libqtile.config import Match, Screen

from core.colors import catppuccin
from core.groups import init_groups
from core.keys import init_keys
from core.mouse import init_mouse
from core.vars import bar_font_size, wallpaper_background
from core.widgets import init_widgets

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

layout_theme = {
    "border_width": 2,
    "margin": 20,
    "border_focus": catppuccin["pink"],
    "border_normal": catppuccin["base"],
}
layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Floating(**layout_theme),
]


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
