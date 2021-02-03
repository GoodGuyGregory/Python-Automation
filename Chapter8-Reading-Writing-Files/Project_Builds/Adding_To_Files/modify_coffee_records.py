# this program allows the user to modify the quantity
# in a record in the coffee.txt file

import os  # needed for the remove and rename functions


def main():
    # create a bool variable to use as a flag
    found = False

    # Get the search value and the ne quantitiy.
    search = input('Enter a description to search for: ')
    new_qty = int(input('Enter the new Quantity: '))

    # open the original coffee.txt file
    coffee_file = open('coffee.txt', 'r')

    # open the temporary file
    # open in write mode
    temp_file = open('temp.txt', 'w')

    # read the first record's description field
    descr = coffee_file.readline()

    # read the rest of the file
    while descr != '':
        # read the quantity field
        qty = coffee_file.readline()

        # strip the \n from the description
        descr = descr.strip('\n')

        # write either this record to the temp file,
        # of the new record if this is the one that is
        # to be modified
        if descr == search:

            # found the description and it needs to updated
            temp_file.write(descr + '\n')
            temp_file.write(str(new_qty) + '\n')

            # set the found flag to True
            found = True
        else:
            # write the original record to the temp file
            temp_file.write(descr + '\n')
            temp_file.write(str(qty) + '\n')

        # Read the next description
        descr = coffee_file.readline()

    # Close the coffee file and the temp file
    coffee_file.close()
    temp_file.close()

    # delete the original coffee.txt file
    os.remove('coffee.txt')

    # rename the tempfile
    os.rename('temp.txt', 'coffee.txt')

    # if the search value was not found in the file
    if found:
        print('The file has been updated for ', search)
    else:
        print('Sorry {} was not found' .format(search))


main()
