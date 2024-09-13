import re

#positive lookhead checks the whole stirng to see if something is present or not

regex = re.compile(r'(?=.*\d){3,}') #checks ahead for any digits but returns nothing

password = 'HaHaHa2'

if regex.search(password) != None:
    print(password)
else:
    print('No digit present')