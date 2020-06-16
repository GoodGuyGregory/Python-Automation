#  FUnction for Checking if a string is a phone number
#  Without Regular Expressions


def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        # no hyphen
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    # All Pass it is a valid phone number
    return True


def isPhoneSplicer(text):
    for i in range(len(text)):
        chunk = text[i:i+12]
        if isPhoneNumber(chunk):
            print('Phone number found: ' + chunk)
    print('Done!')


def main():
    phoneNumber = input('Enter a Phone number: ')
    print("Checking if {} is a phone number ".format(phoneNumber))
    print(isPhoneNumber(phoneNumber))

    # Checking Splicer method
    message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
    print(isPhoneSplicer(message))


main()
