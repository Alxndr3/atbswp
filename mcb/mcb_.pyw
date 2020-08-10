#!/usr/bin/env python3

# mcb.pyw - Saves and loads pieces of text to the clipboard

# Usage: python3 mcb.pyw save <keyword> - Saves clipboard to the keyword
#        python3 mcb.pyw <keyword> - Loads keyword to the clipboard
#        python3 mcb.pyw list - Loads all keywords to the clipboard
#        python3 mcb.pyw erase - Erases database
import pyperclip
import shelve
import sys


mcb_shelf = shelve.open('mcb_')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])


mcb_shelf.close()
