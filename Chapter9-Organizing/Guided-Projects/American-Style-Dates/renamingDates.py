#! python3
#  renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY

import shutil
import os
import re

#  create a regex that matches files with the American date format
datePattern = re.compile(r"""^(.*?) # all text before the date
                         ((0|1)?\d)-  # one or two digits for the month
                         ((0|1|2|3)?\d)- # one or two digits for the day
                         ((19|20)\d\d) # four digits for the year
                         (.*?)$   # all text after the date
                         """, re.VERBOSE)

# loop over the files in the working directory
for ameriFilename in os.listdir('.'):
    mo = datePattern.search(ameriFilename)

    #  skip files without a date
    if mo == None:
        continue

    #  get the different parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    #  form the euro-style date
    euroFilename = beforePart + dayPart + '-' + \
        monthPart + '-' + yearPart + afterPart

    # get the fill, absolute path
    absWorkingDir = os.path.abspath('.')
    ameriFilename = os.path.join(absWorkingDir, ameriFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # rename the files
    print('Renaming "%s" to "%s"...' % (ameriFilename, euroFilename))
    shutil.move(ameriFilename, euroFilename)  # uncomment after testing
