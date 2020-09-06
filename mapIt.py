#! /bin/env python3
# mapIt.py = Launches a map on the browser using an address from the command line or clipboard.
import pyperclip
import sys
import webbrowser


if len(sys.argv) > 1:
    # Get address from the command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()
webbrowser.open(f'https://www.google.com/maps/place/{address}')
