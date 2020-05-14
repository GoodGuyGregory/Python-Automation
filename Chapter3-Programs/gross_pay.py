
def main():
    # try catch example to catch invalid
    try:
        # get the number of hours worked
        hours = int(input("How many hours did you work? "))

        # get the hourly pay rate:
        pay_rate = float(input("Enter your hourly pay rate: "))

        # calculate rate
        gross_pay = hours * pay_rate

        # Display the gross pay
        print('Gross pay: $', format(gross_pay, ',.2f'), sep='')
    except ValueError:
        print('Error: Hours worked and hourly pay rate must')
        print('be valid numbers.')


main()
