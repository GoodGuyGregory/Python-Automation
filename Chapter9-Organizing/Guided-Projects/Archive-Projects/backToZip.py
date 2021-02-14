#! python3
#  backToZip.py - copies an entire folder and its contents into
#  a ZIP file whose filename increments.

import zipfile
import os


def backupToZip(folder):
    #  back up the entire contents of "folder" into a ZIP file.

    folder = os.path.abspath(folder)  # ensures the folder path is absolute

    # determine code name for the file
    number = 1
    while True:
        #  establishes name for the file archive:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    #  create the Zip file
    print('creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    #  walk the whole folder tree and compress the files in each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % foldername)
        # add the current folder to the ZIP.
        backupZip.write(foldername)
        # add all of the files inside of the folders
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue  # dont back up the backup Zip files
            # join adds the paths of the folder and files together in the zip
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')


# archives the curremt directory
backupToZip('delicious')
