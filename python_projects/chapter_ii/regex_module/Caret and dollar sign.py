import re

beginsWithHello = re.compile(r'^Hello')
mo1 = beginsWithHello.search('Hello world!')
mo2 = beginsWithHello.search('He said Hello')
print(mo1)
print(mo2)
print()
endsWithNumber = re.compile(r'\d$')
mo3 = endsWithNumber.search('Hi123')
mo4 = endsWithNumber.search('123Whatsup')
print(mo3)
print(mo4)
print()
wholeStringIsNum = re.compile(r'^\d+$')
mo5 = wholeStringIsNum.search('123456')
mo6 = wholeStringIsNum.search('123 45')
print(mo5)
print(mo6)