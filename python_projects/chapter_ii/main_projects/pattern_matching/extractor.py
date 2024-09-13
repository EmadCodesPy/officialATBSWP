import re, pyperclip

text = str(pyperclip.paste())

emailRegex = re.compile(r'''(
                        ((\S+)@(\S+))(\.\w{3})
                        )''', re.VERBOSE)

phoneNumRegex = re.compile(r'''(
                           (\d{3}|\(\d{3}\))?
                           (\s|-|\.)?
                           \d{3}
                           (\s|-|\.)
                           \d{4}
                           )''', re.VERBOSE)

phoneGroup = phoneNumRegex.findall(text)
emailGroup = emailRegex.findall(text)

total = []
for item in phoneGroup:
    total.append(item[0])
for item in emailGroup:
    total.append(item[0])

if len(total) > 0:
    pyperclip.copy('\n'.join(total))
    print('Copied to clipboard: ')
    print('\n'.join(total))
else:
    print('Nothing was found')

