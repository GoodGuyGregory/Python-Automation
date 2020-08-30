#! /Users/user/.pyenv/versions/3.7.5/bin/python3
#  phoneEmailExtractor.py - searches copied clipboard text for emails and phone numbers

# REGEX 
import re
import pyperclip

# 1. retrieve the text from the user
searchDocument = pyperclip.paste()

# defined REGEX for phone numbers:

phoneRegex = re.compile(r'''(
    
'''))
