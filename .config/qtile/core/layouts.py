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
            Match(wm_class="zen", title=""),
        ]
    )
    return layouts, floating_layout
