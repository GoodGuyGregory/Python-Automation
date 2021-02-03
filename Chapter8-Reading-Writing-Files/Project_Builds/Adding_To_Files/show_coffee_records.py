# This program displays the records in the table
# coffee.txt file


def main():
    # open the coffee.txt file
    coffee_file = open('coffee.txt', 'r')

    # read the first record's description field
    descr = coffee_file.readline()

    # read the rest of the file
    while descr != '':
        #  read the quantity field
        qty = coffee_file.readline()

        # strip the \n from the descriptions
        descr = descr.strip('\n')

        # display the record
        print('Description: ', descr)
        print('Quantity: ', qty)

        # read the next description
        descr = coffee_file.readline()

    # close the file
    coffee_file.close()


# call the function
main()
