# this Program will Validate input
while True:
    print('Enter your age:')
    age = input()
    # uses the isdecimal method
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    # confirms if is all num
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')
