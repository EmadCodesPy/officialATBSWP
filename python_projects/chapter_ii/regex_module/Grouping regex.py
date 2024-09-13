import re

phoneNumbRegex = re.compile(r'(\(\d{3}\))-(\d{3}-\d{4})') 
mo = phoneNumbRegex.search('My number is (415)-555-1234')
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
print(mo.groups())

areaCode, mainNumber = mo.groups()

print()

print(areaCode)
print(mainNumber)