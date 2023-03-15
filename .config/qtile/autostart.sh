#!/bin/sh
feh --bg-scale /home/avenger047/Pictures/wall.png

xset led 3
picom --config /home/avenger047/.config/qtile/core/picom.conf
caffeine &
killall conky
sleep 2s

killall -9 conky
conky -c $HOME/.config/conky/Regulus/Regulus.conf

killall -9 dunst
dunst &
