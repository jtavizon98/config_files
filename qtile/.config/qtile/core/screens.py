from libqtile import bar
from libqtile.config import Screen

from vars import wallpaper_path
from widgets import init_widget_secondary_screen, init_widgets


def init_screens(wayland=True):
    if wayland:
        mybar = bar.Bar(
            widgets=init_widgets(wayland=True),
            background="ffffff00",
            size=35,
            margin=[4, 6, 0, 6],
        )
        screens = [
            Screen(wallpaper=wallpaper_path, wallpaper_mode="fill", top=mybar)
            for i in range(2)
        ]
    else:
        mybar_main = bar.Bar(
            widgets=init_widgets(wayland=wayland),
            background="ffffff00",
            size=35,
            margin=[4, 6, 0, 6],
        )
        mybar_secondary = bar.Bar(
            widgets=init_widget_secondary_screen(wayland=False),
            background="ffffff00",
            size=35,
            margin=[4, 6, 0, 6],
        )
        screens = [
            Screen(wallpaper=wallpaper_path, wallpaper_mode="fill", top=mybar_main),
            Screen(
                wallpaper=wallpaper_path, wallpaper_mode="fill", top=mybar_secondary
            ),
        ]
    return screens
