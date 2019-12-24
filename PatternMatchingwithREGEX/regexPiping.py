import re

# Regex Piping is used when you are looking to match multiple expressions

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel!')
mo.group()
# if Bat|* is found it will return a group object and allow us to reveal the contents
#   of that object
print(mo.group())

# prints the regex subgroup
print(mo.group(1))

# it is also possible to match with a question mark on your regex object.
batQuestionRegex = re.compile(r'Bat(wo)?man')
mo1 = batQuestionRegex.search('The Adventures of Batman')

# Prints what is found:
mo1.group()
print(mo1.group())

mo2 = batQuestionRegex.search('The Adventures of Batwoman!')
# Prints results from regex with Batwoman
mo2.group()

print(mo2.group())

# REGEX EXPRESSIONS USING MATCHES WITH ZERO OR MORE USE '*'

batStarRegex = re.compile(r'Bat(wo)*man')

# TESTING:
mo3 = batStarRegex.search('The Adventures of Batman')

# Prints what is found:
mo3.group()
print(mo1.group())

mo4 = batStarRegex.search('The Adventures of Batwoman!')
# Prints results from regex with Batwoman
mo4.group()

print(mo4.group())

mo5 = batStarRegex.search('The Adventures of Batwowowowowowoman!')

mo5.group()

print(mo5.group())
