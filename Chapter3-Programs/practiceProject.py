# Methods

# Solves with Recursion


def collatz(number):
    # print("Checking Numbers")
    #  if number is even collatz should print even
    # Base Case
    if number == 1:
        return number
    else:
        if number % 2 == 0:
            print(str(number) + " is even")
            # print("Continue working....")
            return collatz(number // 2)

        elif number % 2 == 1:
            print(str(number) + " is odd")
            # print("Continue working....")
            return collatz(3 * number + 1)

# Main method


def main():
    numberToCheck = int(input("Enter Number: "))
    print(collatz(numberToCheck))


main()
