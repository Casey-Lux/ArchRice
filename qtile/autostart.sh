#!/bin/sh

# Keys
setxkbmap latam &

# DPI
xrandr --dpi 96 &

# Resolution
xrandr --output Virtual-1 --mode 1366x768 & # <- Adjust this for your screen

# Wallpapers
/home/user0/wallpapers/wallpaper.py &

# picom
picom --config ~/.config/picom/picom.conf &
