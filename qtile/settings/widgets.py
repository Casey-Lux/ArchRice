from libqtile import widget
import subprocess
from settings.theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(fg='text', bg='dark'):
    return {
        'foreground': colors[fg][0] if isinstance(colors[fg], list) else colors[fg],
        'background': colors[bg][0] if isinstance(colors[bg], list) else colors[bg],
    }

# Draws a space
def separator():
    return widget.Sep(**base(), linewidth=0, padding=1)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text=" 󱎕", 
        fontsize=42,
        padding=-2
    )


def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='UbuntuMono Nerd Font',
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'][0],
            inactive=colors['inactive'][0],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),
    ]


primary_widgets = [
    *workspaces(),

    separator(),

    powerline('color4', 'dark'),

    widget.TextBox(**base(bg='color4'), text=' ArchLinux'),

    powerline('color3', 'color4'),

    icon(bg='color3', text=''),
    
    widget.GenPollText(
        func=lambda: subprocess.check_output(
           "ip -4 addr show ens33 | grep -oE 'inet [0-9.]+' | awk '{print $2}'",
           shell=True
        ).decode().strip(),
        #func=lambda: "TEST",
        update_interval=15,
        **base(bg='color3')
    ),

    powerline('color2', 'color3'),

    #widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),

    widget.CurrentLayout(**base(bg='color2'), padding=5),

    powerline('color1', 'color2'),

    icon(bg="color1", fontsize=17, text='󰃭 '),

    widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color1'),

    #widget.Battery(background=colors['dark'], padding=5, format='{char} {percent:2.0%}'),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold italic',
    'fontsize': 15,
    'padding': 3,
}
extension_defaults = widget_defaults.copy()
