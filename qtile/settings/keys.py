# Qtile keybindings

from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile import extension


mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    ([mod], "s", lazy.layout.down()),
    ([mod], "w", lazy.layout.up()),
    ([mod], "a", lazy.layout.left()),
    ([mod], "d", lazy.layout.right()),
    ([mod], "space", lazy.layout.next()),

    # Change window sizes (MonadTall)
    ([mod, "shift"], "l", lazy.layout.grow()),
    ([mod, "shift"], "h", lazy.layout.shrink()),

    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    ([mod], "q", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "p", lazy.spawncmd()),

    # ArcoLinux Logout
    #([mod], "x", lazy.spawn("arcolinux-logout")),

    # ------------ App Configs ------------

    # Menu
    ([mod], "m", lazy.run_extension(extension.DmenuRun(
        dmenu_prompt=">",
        dmenu_font="fira code medium-10",
        background="#15181a",
        foreground="#1979e5",
        selected_background="#1979e5",
        selected_foreground="#fff",
        #dmenu_height=24,  # Only supported by some dmenu forks
    ))),

    # Window Nav
    #([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Browser
    #([mod], "b", lazy.spawn("chromium")),
    #([mod, "control"], "b", lazy.spawn("vivaldi-stable")),
    ([mod], "b", lazy.spawn("firefox")),

    # File Explorer
    ([mod], "e", lazy.spawn("thunar")),
    # ([mod], "e", lazy.spawn("pcmanfm")),

    # Terminal
    ([mod], "Return", lazy.spawn("alacritty")),
    ([mod, "shift"], "Return", lazy.spawn("kitty")),

    # Redshift
    ([mod], "r", lazy.spawn("redshift -O 2400")),
    ([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Screenshot
    ([mod], "z", lazy.spawn("scrot")),

    #Wallpaper
    ([mod], "x", lazy.spawn("~/wallpapers/wallpaper.py")),

    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +3%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 3%-")),
]]
