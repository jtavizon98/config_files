#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

export PATH="${PATH}:/home/jairot/.scripts"
export GTK_THEME=catppuccin-macchiato-pink-standard+default

# Firefox Wayland support
export MOZ_ENABLE_WAYLAND=1

# ranger :terminal command
export TERMCMD=alacritty
