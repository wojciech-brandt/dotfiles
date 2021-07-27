# IMPORTS
from typing import List  # noqa: F401

import os, subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

# BASIC SETTINGS 
mod = "mod4" 
terminal = guess_terminal() 

# KEYBIDINGS
keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Tab", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below,
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),

    # Pushing focused window to tiling / to floating
    Key([mod], "t", lazy.window.toggle_floating(), 
        desc="Put the focused window to/from floating mode"),

    # Volume and player controls 
    Key([], "XF86AudioRaiseVolume", 
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +1.5%")),
    Key([], "XF86AudioLowerVolume", 
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -1.5%")),
    Key([], "XF86AudioMute", 
        lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    Key([], "XF86AudioPrev", 
        lazy.spawn("playerctl prev")),
    Key([], "XF86AudioNext", 
        lazy.spawn("playerctl next")),
    Key([], "XF86AudioPlay", 
        lazy.spawn("playerctl play-pause")),

    # Laptop brightness keys
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 10%-")),

    # Printscreen functionality with flameshot
    Key([], "Print", lazy.spawn("flameshot gui")),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "p", lazy.spawn("dmenu_run"),
        desc="Spawn dmenu"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
        #     desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # mod1 + shift + letter of group = move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            desc="move focused window to group {}".format(i.name)),
    ])

# LAYOUTS
layouts = [
    # layout.Columns(border_focus_stack=['#ff79c6', '#ff92d0'], border_width=2),
    layout.Columns(border_focus        = '#bd93f9',
                   border_normal       = '#282a36',
                   border_focus_stack  = '#ff79c6',
                   border_normal_stack = '#8c486f',
                   border_width        = 3,
                   margin              = 6,
                   ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# WIDGETS
widget_defaults = dict(
    font='DroidSansMono Nerd Font',
    fontsize=16,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(scale=0.8),
                widget.GroupBox(
                    rounded = False,
                    active = '#f8f8f2',
                    borderwidth = 4,
                    disable_drag = True,
                    fontsize = 16,
                    this_current_screen_border = '#ff79c6',
                    other_current_screen_border = '#6272a4',
                    other_screen_border = '#44475a',
                    this_screen_border = '#bd93f9',
                ),
                widget.Sep(
                    linewidth = 0,
                    padding   = 6,
                ),
                widget.TextBox(
                    text='',
                    font = 'DroidSansMono Nerd Font',
                    foreground = '#ff79c6',
                    padding = 6,
                    fontsize = 18,
                ),
                widget.CPUGraph(
                    border_color = '#ff79c6',
                    fill_color = '#8f3d6c',
                    graph_color = '#ff79c6',
                ),
                widget.Sep(
                    linewidth = 0,
                    padding   = 6,
                ),
                widget.TextBox(
                    text='',
                    font = 'DroidSansMono Nerd Font',
                    foreground = '#50fa7b',
                    padding = 6,
                    fontsize = 20,
                ),
                widget.MemoryGraph(
                    border_color = '#50fa7b',
                    fill_color = '#146328',
                    graph_color = '#50fa7b',
                ),
                widget.Sep(
                    linewidth = 0,
                    padding   = 6,
                ),
                widget.TextBox(
                    text='ﯲ',
                    font = 'DroidSansMono Nerd Font',
                    foreground = '#8be9fd',
                    padding = 6,
                    fontsize = 20,
                ),
                widget.NetGraph(
                    border_color = '#8be9fd',
                    fill_color = '#357987',
                    graph_color = '#8be9fd',),
                #widget.WindowName(),
                widget.Spacer(length=bar.STRETCH), 
                widget.Clock(format='%d-%m-%Y %a %H:%M'),
            ],
            26,
            background='#282a36',
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(scale=0.8),
                widget.GroupBox(
                    rounded = False,
                    active = '#f8f8f2',
                    borderwidth = 4,
                    disable_drag = True,
                    fontsize = 16,
                    this_current_screen_border = '#ff79c6',
                    other_current_screen_border = '#6272a4',
                    other_screen_border = '#44475a',
                    this_screen_border = '#bd93f9',
                ),
                widget.Spacer(length=bar.STRETCH), 
                widget.Clock(format='%d-%m-%Y %a %H:%M'),
            ],
            26,
            background='#282a36',
        ),
    )
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    ],
    border_focus        = '#8be9fd',
    border_normal       = '#282a36',
    border_width        = 3,
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# AUTOSTART
@hook.subscribe.startup_once
def start_one():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
