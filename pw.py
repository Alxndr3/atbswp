#!/usr/bin/env python3.7
# pw.py An insecure password locker program.
import sys
import pyperclip


PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

if len(sys.argv) < 2:
    print('Usage: python py.py [account] - copy account password')
    sys.exit()

# First command line argument is the account name
account = sys.argv[1]
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f'Password {PASSWORDS[account]} for {account} copied to clipboard.')
else:
    print(f'There is no account named {account}')
