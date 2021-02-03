#  this program adds coffee inventory records to
# a coffee.txt file


def main():
    # create a loop control variable:
    another = 'y'

    # open the file in append mode:
    coffee_file = open('coffee.txt', 'a')

    #  add records to the file
    while another == 'y' or another == 'Y':
        #  Get the coffee record data
        print('Enter the following coffee data:')

        descr = input('Description: ')
        qty = str(int(input('Quantity (in pounds): ')))

        # append the data to the file:
        coffee_file.write(descr + '\n')
        coffee_file.write(qty + '\n')

        # determine whether the user wants to add
        # another record to the file.
        print('Do you want to add another coffee?')

        another = input('Y = yes, anything else = no: ')

    # ALWAYS close the file:
    coffee_file.close()
    print('Data appended to coffee.txt')


#  run the program
main()
