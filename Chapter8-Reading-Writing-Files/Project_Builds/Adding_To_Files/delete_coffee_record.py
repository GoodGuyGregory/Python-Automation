# this program allows the user to delete
# a record in the coffee.txt file

import os  # needed for the remove and rename functions


def main():
    # create a bool variable to use as a flag
    found = False

    # Get the coffee to delete
    search = input('Which coffee do you want to delete? ')

    # open the original coffee.txt file
    coffee_file = open('coffee.txt', 'r')

    # open the temp tile
    temp_file = open('temp.txt', 'w')

    # read the first record's description field.
    descr = coffee_file.readline()

    # Read the rest of the file:
    while descr != '':
        # read the quantity field
        qty = coffee_file.readline()

        # strip the \n from the description
        descr = descr.strip('\n')

        # if this is not the record to delete, then
        # write it to the temp file
        if descr != search:
            temp_file.write(descr + '\n')
            temp_file.write(str(qty) + '\n')
        else:
            # Set Found equal to True and avoid writing to temp
            found = True

        # Read the next description
        descr = coffee_file.readline()

    # Close the coffee_file and temp_file
    coffee_file.close()
    temp_file.close()

    # delete the original coffee file
    os.remove('coffee.txt')

    # rename the temp file
    os.rename('temp.txt', 'coffee.txt')

    # if the search value isn't found
    if found:
        print('removed {} from the file' .format(search))
    else:
        print('{} was not found' .format(search))


main()
