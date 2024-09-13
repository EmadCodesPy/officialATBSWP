import re, sys

password = sys.argv[1]

regex = re.compile(r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}')


def strengthCheck(password):
    if regex.search(password) != None:
        print('Your password is strong')
    else:
        print('Your password is too weak')


strengthCheck(password)

