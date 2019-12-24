import re

#  Simple Program to demonstrate the Specific Repetirions Curly Brackets in Python Regex
haRegex = re.compile(r'(Ha){3}')

mo1 = haRegex.search('HaHaHa')
mo1.group()

# will display the contents of the mo1.group()

print(mo1.group())

# Implementing the findall() Method of REGEX Searches:

# Notice the difference in these methods:
dobRegex = re.compile(r'\d\d-\d\d-\d\d')
dob1 = dobRegex.search('Your Date of Birth is: 12-07-93')

dob1.group()

print(dob1.group())

print(dobRegex.findall('DOB: 07-18-00 MINE: 04-20-69'))
