import re

atRegex = re.compile(r'.at') #only copies on character hence the lat in Flat
mo = atRegex.findall('Cat, Mat, Flat')
print(mo)
print()

nameRegex = re.compile(r'First name: (.*) Last name: (.*)')
mo1 = nameRegex.search('First name: Emad Last name: Alqadasi')
print(mo1.group(1) + '\n' + mo1.group(2))
print()

nonGreedyRegex = re.compile(r'<.*?>')
mo2 = nonGreedyRegex.search('<To serve man> for dinner.>')
print(mo2.group())
greedyRegex = re.compile(r'<.*>')
mo3 = greedyRegex.search('<To serve man> for dinner.>')
print(mo3.group())
print()

noNewLineRegex = re.compile(r'.*')
mo4 = noNewLineRegex.search('Hi \nMy name is \nEmad')
print(mo4.group())
print()

newLineRegex = re.compile(r'.*', re.DOTALL)
mo5 = newLineRegex.search('Hi \nMy name is \nEmad')
print(mo5.group())