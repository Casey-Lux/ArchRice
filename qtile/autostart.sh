#!/bin/sh

# Teclado
setxkbmap es &

# DPI
xrandr --dpi 96 &

# Wallpapers
/home/user0/wallpapers/wallpaper.py &

# picom: --no-vsync
picom -f &
