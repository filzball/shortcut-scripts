#!/usr/bin/env python

# Dmenu script for mounting drives

import sys
import subprocess
import python_dmenu as dmenu
import os
from colors import COLORS

# Color definition
SB = COLORS["gruvbox"]["normal"]["aqua"]
SF = COLORS["gruvbox"]["normal"]["bg"]

# font definition
FN = "Hack Nerd Font-14"

# define a few possible mountpoints
MOUNTPOINTS = [f"{os.getenv('HOME')}/mounts/usb_drive",
               f"{os.getenv('HOME')}/mounts",
                "/mnt"]


# get all mountable partitions
def get_mountables():
    mountables = {}
    lsblk = subprocess.run(["lsblk", "-n", "-o", "NAME,PATH,HOTPLUG,TYPE"], capture_output=True).stdout.decode("utf-8").split("\n")
    for line in lsblk[:-1]:
        name, path, hotplug, typ = line.split()
        if int(hotplug) and typ == "part":
            mountables.update({name[2:]: path})
    return mountables

# mount the drive
def mount(drive, mountpoint):
    command = ["sudo", "mount", drive, mountpoint]
    i = subprocess.run(command)
    return i


if __name__ == "__main__":
    mountables = get_mountables()
    data = {"Mount which drive? :": mountables,
            "Mount where?: ": MOUNTPOINTS}

    menus = dmenu.DMenus(data, case_insensitive=True, lines=10, sb=SB, sf=SF, font=FN)
    answers = []
    for menu in menus:
        answers.append(menu.run())
    if all(answers):
        mount(mountables[answers[0]], answers[1])
    else:
        sys.exit(0)

