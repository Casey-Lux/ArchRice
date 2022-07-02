#!/bin/sh

# systray battery icon
cbatticon -u 5 &
# systray volume
#volumeicon &

#nm-applet &

setxkbmap es
xrandr -s 17
/home/user0/wallpapers/wallpaper.py
picom -f --no-vsync &
