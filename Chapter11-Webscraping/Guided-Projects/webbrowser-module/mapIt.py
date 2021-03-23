#! /Users/user/.pyenv/versions/3.7.5/bin/python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard

# imports:
import webbrowser
import sys
import pyperclip

# open a webpage with python
if len(sys.argv) > 1:
    # get address from command line:
    # gets items from the commandline array and adds a space
    address = ' '.join(sys.argv[1:])
else:
    #  get address from clipboard
    address = pyperclip.paste()

    # Get the address from the clipboard
webbrowser.open('https://www.google.com/maps/place/' + address)
