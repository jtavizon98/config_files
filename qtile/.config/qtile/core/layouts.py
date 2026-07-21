from libqtile import layout
from libqtile.config import Match

from core.colors import catppuccin

layout_theme = {
    "border_width": 2,
    "margin": 20,
    "border_focus": catppuccin["pink"],
    "border_normal": catppuccin["base"],
}


def init_layouts():
    layouts = [
        layout.MonadTall(**layout_theme),
        layout.Max(**layout_theme),
        layout.Floating(**layout_theme),
    ]
    floating_layout = layout.Floating(
        float_rules=[
            *layout.Floating.default_float_rules,
            Match(wm_type="popup"),
            Match(wm_type="menu"),
            Match(wm_type="tooltip"),
            Match(wm_type="dropdown_menu"),
            Match(func=lambda c: c.is_transient_for() is not None),
            Match(wm_class="zen", title=""),
            Match(wm_class="swappy"),
        ]
    )
    return layouts, floating_layout
