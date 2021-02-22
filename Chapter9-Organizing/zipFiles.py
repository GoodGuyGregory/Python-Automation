# illustrates the concept of zipping files
import zipfile

# open the file and establish a variable to use
exampleZip = zipfile.ZipFile('example.zip')

print('Lists the items in the zip file')
print(exampleZip.namelist())

# extracting information from Zip files
# this will create a file to hold the contents of the extracted material
exampleZip.extractall('extracted_contents')

# it is also possible to extract a single file
exampleZip.extract('spam.txt', 'single_files')

# close the stream
exampleZip.close()

#  CREATING ZIP FILES:

# must open the file in write mode to create a zip file
newZip = zipfile.ZipFile('new.zip', 'w')

newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()

# to add additional files to a compressed file
# open the file in append mode with 'a'
