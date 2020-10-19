#! /Users/user/.pyenv/versions/3.7.5/bin/python3

# strongPasswordDectection: checks whether
# a copied password or entered password is strong.

import re, pyperclip



def main():
    #  TODO:
    #  build a function that uses REGEX to make sure the password string it is passed
    #  is at least 8 characters long
    #  contains both upper and lower case letters
    #  has at least one digit

    def strongPasswordChecker():

        # Password REGEXs
        #  is at least 8 characters long
        CharCountRegex = re.compile(r'.{8,}')
        #  contains both upper and lower case letters
        UpperLettersRegex = re.compile(r'[A-Z]')
        #  has at least one digit
        DigitRegex = re.compile(r'[0-9]')

         print("checking criteria...")

        # Check input from the user:
        passwordToCheck = pyperclip.paste()
        mo1 = passwordRegex.search(passwordToCheck);
        mo1.group()
        if mo1 === true:
            print("Great Password")
        else:
            print("You can make a Better Password")
            print("Make it at least Eight Characters for Starters")


main()
