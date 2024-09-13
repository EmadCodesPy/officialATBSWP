import re

phoneNumbRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #same as \d{3}-\d{3}-\d{4}
mo = phoneNumbRegex.search('My number is 415-555-1234')
print('The number found is ' + mo.group())