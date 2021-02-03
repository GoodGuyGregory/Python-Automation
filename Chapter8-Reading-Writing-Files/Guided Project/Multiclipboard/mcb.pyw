#! /Users/user/.pyenv/versions/3.7.5/bin/python3
# mcb.pyw - saves and loades pieces of text to the clipboard
# Usage: ./mcb.pyw save <keyword> - saves clipboard to keybard
#        ./mcb.pyw <keyword> - loads keyword to clipboard
#        ./mcb.pyw list - loads all keywords to clipboard
#        ./mcb.pyw delete - deletes a keyword from the shelf


import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')

# save clipboard content:
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # list keywords and load content:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    # delete a specific word:

    elif sys.argv[1] in mcbShelf:
        #  return the contents of that keyword
        pyperclip.copy(mcbShelf[sys.argv[1]])
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if sys.argv[2] in mcbShelf:
        del mcbShelf[sys.argv[2]]
        print("removed {}" .format(str(sys.argv[2])))
    else:
        print("{} isnt saved" .format(str(sys.argv[2])))
mcbShelf.close()
