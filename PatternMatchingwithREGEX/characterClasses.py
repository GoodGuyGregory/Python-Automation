import re
# This is a Crazy program that will utilize all of the Character REGEX EXPRESSIONS:

xmasRegex = re.compile(r'\d+\s\w+')

print(xmasRegex.findall(
    '12 drummers, 11 pipers, 10 lord, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves,1 patridge'))

# You can even create your own Character Classes:

vowelRegex = re.compile(r'[aeiousAEIOU]')

print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD!'))

consonantRegex = re.compile(r'[^aeiousAEIOUS]')

print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD!'))
