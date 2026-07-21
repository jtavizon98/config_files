import os

mod = "mod4"  # Sets mod key to SUPER/WINDOWS

terminal = "alacritty"  # guess_terminal()

browser = "zen-browser"

file_manager = "alacritty -e ranger"

launcher = "rofi -show drun"

music_player = "spotify"

bar_font_size = 20

# -- Localised values: load from core/local.py if present, else use defaults -----
_weather = ["", ""]
_wallpaper = "~/Pictures/Wallpapers/wallpaper.png"
_scripts = "~/.scripts"

try:
    from core.local import (  # noqa: E501  (not tracked, see local.example.py)
        weather_location as _weather,
        wallpaper as _wallpaper,
        scripts_dir as _scripts,
    )
except ImportError:
    pass

location = _weather
wallpaper_background = os.path.expanduser(_wallpaper)
script_path = os.path.expanduser(_scripts)
