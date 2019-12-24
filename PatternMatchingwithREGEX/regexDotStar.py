import re

# Dot-Star: Everything you need to know to do basic application work...

# .* indicated everything in that group. it enters greedy mode and will always try to macth as much text as possible

# GREEDY .*:

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')

# Will take the first name:
mo.group(1)
print(mo.group(1))

# Will print everything in  the Last Name:
mo.group(2)
print(mo.group(2))

# NON-GREEDY:
nongreedyRegex = re.compile(r'<.*?>')

mo1 = nongreedyRegex.search('<to serve man> for dinner.>')
mo1.group()

# prints the shorter non-greedy
print(mo1.group())

# GREEDY:
greedyRegex = re.compile(r'<.*>')

mo2 = greedyRegex.search('<to serve man> for dinner.>')

mo2.group()

# Prints the greedy
print(mo2.group())
