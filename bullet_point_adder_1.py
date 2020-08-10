#!/usr/bin/env python3.7
# bullet_pointer_adder.py - Adds Wikipedia bullet point to the start
# of each line of text on the clipboard.
import pyperclip


text = pyperclip.paste()
# Separate lines and add stars.
lines = text.split('\n')
# Loop through all indexes in the "lines" list
for i in range(len(lines)):
    # Add star to each string in "lines" list
    lines[i] = f'* {lines[i]}'

text = '\n'.join(lines)
pyperclip.copy(text)







