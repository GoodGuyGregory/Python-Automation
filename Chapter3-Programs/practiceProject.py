# Methods
def collatz(number):

    print("you entered: " + str(number))
    #  if number is even collatz should print even
    if number % 2 == 0:
        # print(str(number) + " is even")
        return number // 2

    elif number % 2 == 1:
        print("the number " + number + "is odd")

# Main method


def main():
    print("enter a number:")
    numberToCheck = int(input())
    collatz(numberToCheck)


main()
