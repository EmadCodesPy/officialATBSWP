import os, re, pprint
#This is a regex search to find what you want in a folder

alphaFile = os.listdir('B:\ATBSWP\python_projects\\regex_search_file')

getRegex = str(input('What is your regular expression: '))
regex = re.compile(rf'{getRegex}')

dictionary = {}

for file in alphaFile:
    openFile = open(os.path.join('B:\ATBSWP\python_projects\\regex_search_file\\', file))
    readFile = openFile.read()
    regexFound = regex.findall(readFile)
    dictionary[file] = regexFound
    openFile.close()

print(pprint.pformat(dictionary))
