import re

# Module to allow for the implementation of Regex expressions in Python

# First Create a regex object with your demands:
# Here we are allowing a re object to compile a list object with a regular string inside
# \d represents digits 0-9
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# mo is declared and given the result of the search method on the regex object:
# search retrns a match object
mo = phoneNumRegex.search('My number is 415-555-4242.')
# if the search returns a match object it will be accessable in the group object and appear as a string
# upon output
print('Phone number found: ' + mo.group())

# This next Call will determine is a string does or doesn't have an area code based on the
# Question mark regex additions
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My Number is 415-555-4242')
mo1.group()
# Prints the findings from the regex:
print(mo1.group())

# lets see if it can locate numbers without the area code now....
mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())
