while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        #  move to next step
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only)')
    password = input()
    if password.isalnum():
        # end program
        break
    print('Passwords can only have letters and numebers')
