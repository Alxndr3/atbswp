#!/usr/bin/env python3.7
# This version is develop by Alexandre Cardoso
# bullet_pointer_adder.py - Adds Wikipedia bullet point to the start
import pyperclip

text = pyperclip.paste()
text_new = ''
text_list = []
for i in range(len(text)):
    if text[i] != '\n':
        text_new = text_new + text[i]
    else:
        text_list.append(text_new)
        text_new = ''
for x in range(len(text_list)):
    text_new = text_new + f'* {text_list[x]} \n'

pyperclip.copy(text_new)

