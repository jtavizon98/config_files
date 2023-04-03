#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

export PATH="${PATH}:/home/jairot/.scripts"
export GTK_THEME=Catppuccin-Macchiato-Standard-Blue-Dark

# Firefox Wayland support
if [ "$XDG_SESSION_TYPE" == "wayland"  ]; then
        export MOZ_ENABLE_WAYLAND=1
fi
