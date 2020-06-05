#! /Users/user/.pyenv/versions/3.7.5/bin/python3
#  bulletPointAdder.py - Adds Wikipedia Bullet points to the start
#  of each line of text on the clipboard

import pyperclip

# returns all items from the clipboard as one big line of text
text = pyperclip.paste()

# Sepeare Lines and add stars
lines = text.split('\n')
for i in range(len(lines)):  # loop through indexes in the "lines" list
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)
