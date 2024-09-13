'''This is a local insecure password locker that 
I will use to copy my pswrds to my clipboard'''

PASSWORDS = {'overflow': '8Rd7VUdtEBFN3B',
             'talabat': 'Roblox360!',
             'github': 'Roblox360123456'}

import pyperclip
import sys

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1:]  #first command line arg is the account name e.g "python pw.py XX" XX is copied to account
account = ' '.join(account)

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f'The password for {account} has been copied to the clipboard')
    pass
else:
    print(f'There is no account named {account}')