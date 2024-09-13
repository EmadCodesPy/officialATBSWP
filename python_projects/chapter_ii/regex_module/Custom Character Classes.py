import re

vowelRegex = re.compile(r'[aeiouAEIOU]')
mo1 = vowelRegex.findall('Robocop eats baby food. BABY FOOD')

consonantRegex = re.compile(r'[^aeiouAEIOU]')
mo2 = consonantRegex.findall('Robocop eats baby food. BABY FOOD')

print(mo1)
print()
print