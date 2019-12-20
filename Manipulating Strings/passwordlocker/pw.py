#! python3
# pw.py - An inseure password locker program.

# The dictionary wil be the data structure that organizes your account and password data.
# simply call your account from the commandline to get the password for that specific account

import sys
PASSWORDS = {'email': 'EMAILPASSWORD',
             'blog': 'BLOGPASSWORD',
             'luggage': '12345'
             }

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name
