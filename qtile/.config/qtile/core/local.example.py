"""
Local Qtile configuration values.
Copy to core/local.py and customize before starting Qtile:
  cp core/local.example.py core/local.py
  chmod 600 core/local.py
"""

# OpenWeather widget: [city_name_country, city_id]
# Find city_id at: https://openweathermap.org/
weather_location = ["", ""]

# Path to wallpaper image (~ for home directory)
wallpaper = "~/Pictures/Wallpapers/wallpaper.png"

# Directory containing utility scripts (e.g. powermenu, screenshot)
scripts_dir = "~/.scripts"

# Wireless network interface name (find with: ip link)
wlan_interface = ""

# Touchpad device identifiers
# X11: find with 'xinput list'
touchpad_xinput_name = ""
# Wayland: find with 'libinput list-devices'
touchpad_wl_id = ""
