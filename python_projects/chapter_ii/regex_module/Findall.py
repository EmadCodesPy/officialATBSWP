import re

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.findall('Cell: 415-555-1234, Work: 212-555-0000')
print(mo)

groupedPhoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo2 = groupedPhoneNumRegex.findall('Cell: 415-555-1234, Work: 212-555-0000')
print(mo2)