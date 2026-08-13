[[ -f ~/.bashrc ]] && . ~/.bashrc

export XDG_DATA_DIRS="${XDG_DATA_DIRS:-/usr/local/share:/usr/share}"
# Firefox Wayland support
export MOZ_ENABLE_WAYLAND=1
