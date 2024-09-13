import re

batRegex = re.compile(r'Bat(wo)*man') #This is only for zero or more
mo1 = batRegex.search('The adventures of Batman')
mo2 = batRegex.search('The adventures of Batwoman')
mo3 = batRegex.search('The adventures of Batwowowowoman')
 
print(f'{mo1.group()} \n{mo2.group()} \n{mo3.group()}')

bat2Regex = re.compile(r'Bat(wo)+man') #This is only for 1 or more

bat3Regex = re.compile(r'Ha{,3}') #This is only true for up to 3 Ha, anything more is false

