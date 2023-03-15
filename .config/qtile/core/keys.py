from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from extras import float_to_front
from utils import config

keys, mod, alt = [ ], 'mod4', 'mod1'
terminal = config['terminal'].copy()

for key in [
  # Switch between windows
  ([mod], 'Left', lazy.layout.left()),
  ([mod], 'Up', lazy.layout.right()),
  ([mod], 'Down', lazy.layout.down()),
  ([mod], 'Right', lazy.layout.up()),

  # Move windows between columns
  ([mod, 'shift'], 'h', lazy.layout.shuffle_left()),
  ([mod, 'shift'], 'l', lazy.layout.shuffle_right()),
  ([mod, 'shift'], 'j', lazy.layout.shuffle_down()),
  ([mod, 'shift'], 'k', lazy.layout.shuffle_up()),

  # Increase/decrease window size
  ([mod], 'i', lazy.layout.grow()),
  ([mod], 'm', lazy.layout.shrink()),

  # Window management
  ([mod, 'shift'], 'space', lazy.layout.flip()),
  ([mod], 'o', lazy.layout.maximize()),
  ([mod], 'n', lazy.layout.normalize()),
  ([mod], 'F4', lazy.window.kill()),
  ([ ], 'F11', lazy.window.toggle_fullscreen()),

  # Floating window management
  ([mod], 'space', lazy.window.toggle_floating()),
  ([mod], 'c', lazy.window.center()),
  ([mod], 'f', lazy.function(float_to_front)),

  # Toggle between layouts
  ([mod], 'Tab', lazy.next_layout()),

  # Qtile management
  ([mod, 'control'], 'b', lazy.hide_show_bar()),
  ([mod], 'End', lazy.spawn('poweroff')),
  ([mod, 'control'], 'r', lazy.reload_config()),
  ([mod, 'control'], 'F4', lazy.spawn('reboot')),
  ([mod, alt], 'r', lazy.restart()),

  # Kill X11 session
  ([mod, alt], 's', lazy.spawn('kill -9 -1')),

  # Terminal
  ([mod], 'Return', lazy.spawn('alacritty')),
  ([mod, 'shift'], 'Return', lazy.spawn(terminal['floating'])),

  # Application Launcher
  ([mod, 'shift'], 'r', lazy.spawn('rofi -show window')),
  ([mod], 'r', lazy.spawn('/home/avenger047/.config/rofi/launchers/type-5/launcher.sh')),
  

  ([mod, 'shift'], 'c', lazy.spawn('conky -c /home/avenger047/.config/conky/Regulus/Regulus.conf')),

  # Web Browser
  ([mod], 'b', lazy.spawn(config['browser'])),

  # Screenshot Tool
  ([ ], 'Print', lazy.spawn('gnome-screenshot -i')),

  # Backlight
  ([mod], 'XF86AudioLowerVolume', lazy.spawn('brightnessctl set 5%-')),
  ([mod], 'XF86AudioRaiseVolume', lazy.spawn('brightnessctl set +5%')),

  # Volume
  ([ ], 'XF86AudioMute', lazy.spawn('pamixer --toggle-mute')),
  ([mod], '5', lazy.spawn('pamixer --decrease 5')),
  ([mod], '6', lazy.spawn('pamixer --increase 5')),

  # Player
  ([ ], 'XF86AudioPlay', lazy.spawn('playerctl play-pause')),
  ([ ], 'XF86AudioPrev', lazy.spawn('playerctl previous')),
  ([ ], 'XF86AudioNext', lazy.spawn('playerctl next')),
]: keys.append(Key(*key)) # type: ignore
