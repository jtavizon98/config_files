from libqtile import layout
from libqtile.config import Match

from colors import catppuccin

layout_theme = {
    "border_width": 2,
    "margin": 20,
    "border_focus": catppuccin["pink"],
    "border_normal": catppuccin["base"],
}


def init_layouts():
    layouts = [
        # layout.Zoomy(**layout_theme),
        layout.MonadTall(**layout_theme),
        layout.Max(**layout_theme),
        # layout.Stack(stacks=2, **layout_theme),
        # layout.RatioTile(
        #     **layout_theme,
        #     clockwise=True,
        #     new_client_position='bottom',
        #     ratio = 0.5
        # ),
        # layout.Spiral(
        #     **layout_theme,
        #     clockwise=True,
        #     new_client_position='after_current',
        #     ratio = 0.5
        # ),
        layout.Floating(**layout_theme),
    ]
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
    return layouts, floating_layout
