#!/usr/bin/env python
# library script for dmenu which opens pdf books

import sys
import python_dmenu as dmenu
import os
import subprocess

from colors import COLORS

# colors
SB = COLORS["gruvbox"]["normal"]["aqua"]
SF = COLORS["gruvbox"]["normal"]["bg"]

FN = "Hack Nerd Font-14"


PATH = f"{os.getenv('HOME')}/documents/books"

# # get all the books in ~/documents/books
os.chdir(PATH)
books = os.listdir(".")
books.append("EXIT")

# # make a menu
menur = dmenu.DMenu(books, case_insensitive=True, prompt="Which book do you want to read? : ",
                    font=FN, sb=SB, sf=SF, lines=10)
fname = menur.run().strip()

# # open the book in a pdf reader
if fname and fname != "EXIT":
    subprocess.run(["mupdf", fname])
else:
    sys.exit(0)
