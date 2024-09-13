import re

namesRegex = re.compile(r'Agent \w+')
mo = namesRegex.sub(r'CENSORED', r'Agent Emad gave the document to  Agent Allen')
print(mo)
print()
agentNamesRegex = re.compile(r'Agent (\w)(\w)\w*')
mo1 = agentNamesRegex.sub(r'\1-*0',r'Agent Emad gave the document to  Agent Allen') #the \# is for the group in the regex and the following is the replacement text
print(mo1)