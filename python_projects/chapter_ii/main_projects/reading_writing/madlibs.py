import re

file = open('B:\ATBSWP\python_projects\chapter_ii\main_projects\\text.txt')
fileRead = file.read()
regex = re.compile(r'\w+\s*|\W')
wordList = regex.findall(fileRead)
file.close()

replacementText = {'ADJECTIVE': 'Enter an adjective',
                   'NOUN': 'Enter a noun',
                   'VERB': 'Enter a verb'}

outList = []

for word in wordList:
    if word.strip() in replacementText: 
        inp = str(input(f'{replacementText[word.strip()]}: '))
        outList.append(inp+' ')
    else:
        outList.append(word)

out = ''.join(outList)

print(out)

newFile = open('B:\ATBSWP\python_projects\chapter_ii\main_projects\\outputText.txt', 'w')
newFile.write(out)
newFile.close()