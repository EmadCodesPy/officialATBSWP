import re

'''
Create something that takes the text and removes whitespace from the ends
if there is a strip arguments then remove the stripped text from the main text
'''


def strip(txt, strip=' '):
    if strip == ' ':
        regex = re.compile(r'(^\s*)|(\s*$)')
    else:
        regex = re.compile(f'{strip}')

    mo = regex.sub(f'', f'{txt}')
    print(mo)

strip('Hi my haname is apple ha ha', 'ha')


