import re

robocop = re.compile(r'robocop', re.I) #Case insensitive is the re.I part
mo = robocop.search('Robocop is part man, part machine, all cop.')
print(mo.group())