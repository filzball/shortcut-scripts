#!/usr/bin/env python

import sys
from python_dmenu import DMenu
from colors import COLORS
import subprocess

PROMPT = "Do you want to exit dwm? : "
SB = COLORS["gruvbox"]["normal"]["red"]
SF = COLORS["gruvbox"]["normal"]["bg"]
FONT = "Hack Nerd Font-14"

answer = DMenu("No Yes".split(" "), case_insensitive=True, prompt=PROMPT, font=FONT,
             sb=SB, sf=SF).run()

if answer == "Yes":
    pid = subprocess.run("pidof -s dwm".split(" "), capture_output=True).stdout.decode("utf-8").strip()
    subprocess.run(["kill", "-TERM", pid])
else:
    sys.exit(1)
