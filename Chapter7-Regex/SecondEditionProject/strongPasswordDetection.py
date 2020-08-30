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
    
    
    passwordRegex = re.compile()
    
    
    def strongPasswordChecker():
         print("checking criteria")
    
    # Check input from the user:
    if len(pyperclip.paste() == 0):
         passwordToCheck = input('please type your password: ')
         strongPasswordChecker(passwordToCheck)
    else:
        passwordToCheck = str(pyperclip.paste())
        strongPasswordChecker(passwordToCheck)
   
        
main()
