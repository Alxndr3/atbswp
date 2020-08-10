#!/usr/bin/env python3

# mcb.pyw - Saves and loads pieces of text to the clipboard

# Usage: python3 mcb.pyw save <keyword> - Saves clipboard to the keyword
#        python3 mcb.pyw <keyword> - Loads keyword to the clipboard
#        python3 mcb.pyw list - Loads all keywords to the clipboard
#        python3 mcb.pyw erase - Erases database
#        python3 mcb.pyw delete <keyword> - Erases database
import pyperclip
import shelve
import sys


def usage():
    print('''
    Usage: python3 mcb.pyw save <keyword> - Saves clipboard to the keyword.
           python3 mcb.pyw <keyword> - Loads keyword to the clipboard. 
           python3 mcb.pyw list - Loads all keywords to the clipboard.
           python3 mcb.pyw erase - Erases database
           python3 mcb.pyw delete <keyword> - Erases database
    ''')


# TODO: Save clipboard content
def save_clipboard(key_word):
    mcb_shelf_db = shelve.open('mcb')
    mcb_shelf_db[key_word] = pyperclip.paste()
    mcb_shelf_db.close()


# TODO: List key words and load content
def list_keyword():
    mcb_shelf_db = shelve.open('mcb')
    pyperclip.copy(str(list(mcb_shelf_db.keys())))
    mcb_shelf_db.close()


# TODO: Load content to clipboard
def load_content(key_word):
    mcb_shelf_db = shelve.open('mcb')
    content = mcb_shelf_db[key_word]
    pyperclip.copy(content)
    mcb_shelf_db.close()


# TODO: Erase DB
def erase_db():
    mcb_shelf = shelve.open('mcb')
    mcb_shelf.clear()
    mcb_shelf.close()


# TODO: Delete item from DB
def delete_item(key_word):
    mcb_shelf = shelve.open('mcb')
    del mcb_shelf[key_word]
    mcb_shelf.close()


if len(sys.argv) < 2:
    usage()
    sys.exit()

argument = sys.argv

if len(sys.argv) == 2:
    if sys.argv[1] == 'list':
        list_keyword()
    elif sys.argv[1] == 'erase':
        erase_db()
    elif sys.argv[1] in shelve.open('mcb.db'):
        load_content(sys.argv[1])

if len(sys.argv) == 3:
    if sys.argv[1] == 'save':
        save_clipboard(argument[2])
    elif sys.argv[1] == 'delete':
        delete_item(sys.argv[2])
