# this program allows the user to search
#  the coffee.txt file for records matching
#  a description


def main():
    # create a bool variable to use as a flag
    found = False

    # get the search value
    search = input('Enter a description to search for: ')

    # open the file
    coffee_file = open('coffee.txt', 'r')

    # read the first record's description field
    descr = coffee_file.readline()

    # read the rest of the file
    while descr != '':
        # read the quantity field
        qty = coffee_file.readline()

        # strip the '\n' from the description
        descr = descr.strip('\n')

        # determine if it is the searched element
        if descr.lower() == search.lower():
            # display the record
            print('Description: ', descr)
            print('Quantity: ', qty)
            print()

            # set the found flag to true
            found = True

        # read the next description
        descr = coffee_file.readline()

    # close the file
    coffee_file.close()

    # if the search value was not found in the file tell the user
    if not found:
        print('That item was not found in the file.')


main()
