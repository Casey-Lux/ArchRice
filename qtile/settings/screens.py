# Multimonitor support

from libqtile.config import Screen
from libqtile import bar
from settings.widgets import primary_widgets

def status_bar(widgets):
    return bar.Bar(widgets, 28, margin=[4, 6, 4, 6], opacity=0.95)

screens = [
    Screen(top=status_bar(primary_widgets))
]
