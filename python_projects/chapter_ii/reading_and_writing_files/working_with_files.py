import re

helloFile = open('/users/emad/desktop/hello.txt')
helloContent = helloFile.read()
#returns content of the file as one big string
print(helloContent)

sonnetFile = open('/users/emad/desktop/sonnet29.txt')
sonnetContent = sonnetFile.readlines()
#returns each line of a file sepereated by a line break as a list
print(sonnetContent)
