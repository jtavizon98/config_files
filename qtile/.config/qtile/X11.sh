#!/usr/bin/env bash 

lxsession &
picom &
#conky -c $HOME/.config/conky/doomone-qtile.conkyrc
nm-applet &
blueman-applet&

# Touchpad settings are now configured in Qtile's core/local.py
# (touchpad_xinput_name).  See core/local.example.py for details.
