# Multimonitor support

from libqtile.config import Screen
from libqtile import bar
from settings.widgets import primary_widgets, secondary_widgets
import subprocess


def status_bar(widgets):
    return bar.Bar(widgets, 24, opacity=0.95)


screens = [
    Screen(top=status_bar(primary_widgets))
]
