#!/bin/sh

# Keys
setxkbmap es &

# DPI
xrandr --dpi 96 &

# Resolution
xrandr --output Virtual-1 --mode 1366x768 & # <- Adjust this for your screen

# Wallpapers
/home/user0/wallpapers/wallpaper.py &

# picom: --no-vsync
picom -f &
