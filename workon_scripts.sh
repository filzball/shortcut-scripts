#!/bin/sh


script=$(ls $HOME/.scripts | dmenu -i -sb "#2c8405" -p "Work on which script: " -l 10)
[[ -e "$HOME/.scripts/$script" ]] && [[ -f "$HOME/.scripts/$script" ]] || exit 1
st -e nvim $HOME/.scripts/$script
