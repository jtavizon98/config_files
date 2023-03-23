#!/usr/bin/env bash 

lxsession &
picom &
#conky -c $HOME/.config/conky/doomone-qtile.conkyrc
nm-applet &
blueman-applet&

# Set natural scrolling on touchpad
xinput set-prop "VEN_04F3:00 04F3:3242 Touchpad" "libinput Natural Scrolling Enabled" 1
