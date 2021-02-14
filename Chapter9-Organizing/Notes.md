## Chapter 9 Organizing Files

**shutil Module**

**copying files**

allows for copying files and directories `shutil.copy(source, destination)` if the destination is a filename it will be used as the new name of the copied file

it is possible to copy an entire directory with the `shutil.copytree(source, destination)` 

**moving files**

allows for moving of files to a specified destination `shutil.copy(source, destination)` if there are versions of the file already in th directory it will rewrite over them. you can also rename files in the destination to avoid this error.

```python
import shutil

# if there was not a directory named someDir copy would rename somefile to 
# someDir. which isn't helpful so check for these errors
shutil.copy('somefile.txt', 'someDir')

# if there is already a somefile in the someDir rename it
# by changing th destination name
shutil.copy('somefile.txt', 'someDir/newSomeFile.txt')

```

**deleting files**

there are three ways to delete files in python

* `os.unlink(filename)` will delete the filename specified `os.rmdir(directory)` will delete the folder at the path (the folder must be empty)

* `shutil.rmtree(path)` will remove the folder and its contents 

* `send2trash.send2trash(filename)` will send the file name to the recycle bin instead of deleting files and folders