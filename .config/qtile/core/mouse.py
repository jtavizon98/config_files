from libqtile.backend.wayland.inputs import InputConfig
from libqtile.config import Click, Drag
from libqtile.lazy import lazy

from core.vars import mod


def init_mouse(wayland=True):
    wl_input_rules = {}
    mouse = [
        Drag(
            [mod],
            "Button1",
            lazy.window.set_position_floating(),
            start=lazy.window.get_position(),
        ),
        Drag(
            [mod],
            "Button3",
            lazy.window.set_size_floating(),
            start=lazy.window.get_size(),
        ),
        Click([mod], "Button2", lazy.window.bring_to_front()),
    ]
    if wayland:
        # When using the Wayland backend, this can be used to configure input devices.
        wl_input_rules["1267:12866:VEN_04F3:00 04F3:3242 Touchpad"] = InputConfig(
            natural_scroll=True,
            tap=True,
            dwt=True,
            accel_profile="adaptive",
        )
    return mouse, wl_input_rules
