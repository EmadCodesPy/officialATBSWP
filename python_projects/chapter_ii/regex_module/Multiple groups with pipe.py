import re

heroRegex = re.compile(r'Batman|Tina Frey')

mo1 = heroRegex.search('Batman and Tina Frey')
print(mo1.group())

mo2 = heroRegex.search('Tina Frey and Batman')
print(mo2.group())

print()

batRegex = re.compile(r'Bat(man|mobile|copter)')

mo3 = batRegex.search('The Batmobile is gone')
print(mo3.group())
print(mo3.group(1))