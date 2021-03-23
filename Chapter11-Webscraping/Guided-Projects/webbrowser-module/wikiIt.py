#! /Users/user/.pyenv/versions/3.7.5/bin/python3
# wikiIt.py - Launches a wikipedia page in the browser using an item to search from the
# command line or clipboard

import webbrowser
import sys
import pyperclip

# open a webpage with python
if len(sys.argv) > 1:
    # get address from command line:
    # gets items from the commandline array and adds a space
    searchItem = ' '.join(sys.argv[1:])
else:
    #  get address from clipboard
    searchItem = pyperclip.paste()


webbrowser.open('https://en.wikipedia.org/wiki/' + searchItem)
