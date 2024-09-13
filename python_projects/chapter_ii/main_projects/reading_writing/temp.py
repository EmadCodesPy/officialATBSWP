import re
file = open('B:\ATBSWP\python_projects\chapter_ii\main_projects\\text.txt')
fileRead = file.read()

regex = re.compile(r'\w+\s*|\W')

output = regex.findall(fileRead)
final = []
for word in output:
    x = word.strip()
    final.append(x)
    
print(final)