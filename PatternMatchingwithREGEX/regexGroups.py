import re

phoneNumREgex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo = phoneNumREgex.search('My number is 425-555-4242.')
print('mo.group(1) displays the first group in the regex')
print(mo.group(1))

print('mo.group(2) does the same')
print(mo.group(2))

print('mo.group(0) prints everything ')
print(mo.group(0))

print('everything can also be printed with mo.groups()')
print(mo.groups())

# You can even assign groups...
areaCode, mainNumber = mo.groups()

print('areacode, and mainNumber')
print(areaCode)
print(mainNumber)
