#! /Users/user/.pyenv/versions/3.7.5/bin/python3
#  phoneEmailExtractor.py - searches copied clipboard text for emails and phone numbers

# REGEX 
import re
import pyperclip

# 1. retrieve the text from the user
searchDocument = pyperclip.paste()

# 2. Define REGEX needed for tasks:

# defined REGEX for phone numbers and emails:

phoneRegex = re.compile(r'''(
    (\d{3}|\(d{3}\))?  #area code and optional parenthesis
    (\s|-|\.)?         # seperator can be a (space | hyphen | . )
    \d{3}              # first three digits of the phone number
    (\s|-|\.)          # seperator of a (space | hyphen | . )
    \d{4}              # remaining 4 digits of the telephone number
    (\s*(ext|x|ext.)\s*\d{2,5})? # matches the extension 
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ #username characters
    @                 # @ symbol for email
    [a-zA-Z0-9.-]+    # domain name
    (\.[a-zA-Z]{2,4}) # dot-something (.co/.edu/.org/.com) etc
)''', re.VERBOSE)

#  Locate the emails and phone numbers from the clipboard
# convert to string 
textToSearch = str(pyperclip.paste())

# stores all found items from the text 
matches = []

# match and add groups of found numbers 
for groups in phoneRegex.findall(textToSearch):
    phoneNumber = '-'.join(groups[1],groups[3], groups[5])
    if groups[8] != '':
        phoneNumber += ' x' + groups[8]
    matches.append(phoneNumber)

for groups in emailRegex.findall(textToSearch):
    matches.append(groups[0])
    

