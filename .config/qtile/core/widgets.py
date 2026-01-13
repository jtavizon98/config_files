from libqtile import bar, qtile
from qtile_extras import widget

from core import api_keys
from core.colors import catppuccin
from core.vars import launcher, location, script_path

# Qtile extras rounded corners
decorations_group = {
    "decorations": [
        widget.decorations.RectDecoration(
            use_widget_background=True,
            filled=True,
            radius=18,
            group=True,
        )
    ]
}


def init_widgets():
    widgets_list = [
        widget.TextBox(
            text="   ",
            font="UbuntuMono Nerd Font",
            background=catppuccin["blue"],
            foreground=catppuccin["surface0"],
            padding=5,
            mouse_callbacks={"Button1": lambda: qtile.spawn(launcher)},
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
            fontsize=22,
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
            app_key=api_keys.open_weather,
            location=location[0],
            # format="{location_city}: {icon} {main_temp:.0f}°{units_temperature}",
            fmt=" {}",
            mouse_callbacks={
                "Button1": lambda: qtile.spawn(
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
                "Button1": lambda: qtile.spawn(
                    f"xdg-open https://calendar.google.com"
                )
            },
            **decorations_group,
        ),
        widget.Spacer(background="ffffff00", length=bar.STRETCH),
        widget.Pomodoro(
            background=catppuccin["red"],
            color_inactive=catppuccin["surface0"],
            color_active=catppuccin["surface0"],
            color_break=catppuccin["surface0"],
            font="UbuntuMono Nerd Font",
            fmt=" {} ",
            prefix_inactive=" ",
            prefix_active="󰔟 ",
            prefix_paused="󱦠 ",
            prefix_break=" ",
            prefix_long_break=" ",
            # length_pomodori=0.25,
            # length_short_break=0.25,
            # length_long_break=0.25,
            **decorations_group,
        ),
        widget.Spacer(background="ffffff00", length=3),
        widget.Bluetooth(
            adapter_format=" {powered} {discovery} {name}   ",
            adapter_paths=[],
            default_text=" 󰂯 {connected_devices} ",
            default_show_battery=True,
            device_battery_format=" {battery}%",
            device_format=" {symbol} {name} {battery_level} ",
            symbol_connected="󰂱",
            symbol_paired="-",
            symbol_powered=("󰂯", "󰂲"),
            foreground=catppuccin["surface0"],
            background=catppuccin["sky"],
            mouse_callbacks={"Button1": lambda: qtile.spawn("rofi-bluetooth")},
            **decorations_group,
        ),
        widget.Spacer(background="ffffff00", length=3),
        widget.Wlan(
            background=catppuccin["lavander"],
            foreground=catppuccin["surface0"],
            format=" 󰖩  ",
            disconnected_message=" 󰖪  ",
            interface="wlp0s20f3",
            update_interval=5,
            mouse_callbacks={
                "Button1": lambda: qtile.spawn("networkmanager_dmenu")
            },
            **decorations_group,
        ),
        widget.Wlan(
            background=catppuccin["lavander"],
            foreground=catppuccin["surface0"],
            fmt="{} ",
            format="{percent:2.0%}",
            disconnected_message="",
            interface="wlp0s20f3",
            update_interval=5,
            mouse_callbacks={
                "Button1": lambda: qtile.spawn("networkmanager_dmenu")
            },
            **decorations_group,
        ),
        widget.Spacer(background="ffffff00", length=3),
        widget.KeyboardLayout(
            configured_keyboards=["us", "latam", "de"],
            display_map={"us": "US", "latam": "ES", "de": "DE"},
            fmt=" 󰌌  {} ",
            foreground=catppuccin["surface0"],
            background=catppuccin["maroon"],
            padding=5,
            **decorations_group,
        ),
        widget.Spacer(background="ffffff00", length=3),
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
        ),
        widget.Spacer(background="ffffff00", length=3),
        widget.TextBox(
            text="  󰐥  ",
            font="UbuntuMono Nerd Font",
            foreground=catppuccin["red"],
            background=catppuccin["crust"],
            mouse_callbacks={
                "Button1": lambda: qtile.spawn(
                    f"bash {script_path}powermenu/type-1/powermenu.sh"
                )
            },
            padding=0,
            fontsize=24,
            **decorations_group,
        ),
    ]
    return widgets_list
