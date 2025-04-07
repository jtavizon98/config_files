#!/usr/bin/env bash 

lxsession &
picom &
#conky -c $HOME/.config/conky/doomone-qtile.conkyrc
nm-applet &
blueman-applet&

# Set natural scrolling on touchpad
xinput set-prop "Example Touchpad" "libinput Natural Scrolling Enabled" 1
