#  writing log messages to a file

import logging
#  configure the logging module to write to a file
logging.basicConfig(filename='myLogs.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s = %(message)s')


def logWriter():
    error = input('enter an ERROR you might see in programming ')
    logging.debug(str(error) + ' ERRORs might happen when developing python')


logWriter()
