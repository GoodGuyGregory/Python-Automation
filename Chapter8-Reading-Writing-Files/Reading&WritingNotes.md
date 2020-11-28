**Reading and Writing to Files Notes**

using the correct paths based on the clients OS is simple using the **os** module 

```python
import os
# combines the client's OS configuration
os.path.join('Usr','bin','spam')
```
this is common for creating file names as strings etc.

**Getting Current Working Directory**

it is possible to retun the current working directory from the user. using the `os.getcwd()` you can also change the working dir with `os.chdir(<path>)`

**Create Folders/Directories**

use the `os.makedirs('user/delicious/walnut/waffles')` to make a couple folders with the names used as an argument 
