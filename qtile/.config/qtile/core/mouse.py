from libqtile.backend.wayland.inputs import InputConfig
from libqtile.config import Click, Drag
from libqtile.lazy import lazy

from core.vars import mod

# Touchpad Wayland id (optional local override)
try:
    from core.local import touchpad_wl_id  # noqa: E501
except ImportError:
    touchpad_wl_id = ""


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
    if wayland and touchpad_wl_id:
        # When using the Wayland backend, this can be used to configure input devices.
        wl_input_rules[touchpad_wl_id] = InputConfig(
            natural_scroll=True,
            tap=True,
            dwt=True,
            accel_profile="adaptive",
        )
    return mouse, wl_input_rules
