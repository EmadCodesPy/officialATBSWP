import re

someRegexValue = re.compile(r'foo', re.VERBOSE | re.DOTALL | re.I)
#This is the only way you can use multiple flags with the regex module