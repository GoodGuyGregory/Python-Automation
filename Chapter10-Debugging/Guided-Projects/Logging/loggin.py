# allow for logging in your code
import logging
#  specify the logging details
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
#  specify logging start
logging.debug('Start of program')

# used to easily disable log messages for the user
# logging.disable(logging.CRITICAL)

#  factorial example


def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total


print(factorial(5))
logging.debug('End of Program')
