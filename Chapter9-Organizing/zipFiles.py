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
