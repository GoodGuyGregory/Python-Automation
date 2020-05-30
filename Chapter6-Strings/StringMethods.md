**String Specific Methods**

Case Changing Methods:

* `upper()`: changes the case of the string to all uppercase
* `lower()`: changes the case of the string to all lowercase

Checking Case of Strings:

* `islower()`: returns true or false if the string in question is lowercase
* `isupper()`: returns true or false if the string in question is uppercase

Checking contents of Strings:

* `isaplha()`: returns true if the string contains only letters and is not blank

* `isalnum()`: returns true if the string consists of only letters and numbers

* `isdecimal()`: returns true if the string consists of numeric characters and is not blank

* `isspace()`: returns true if the string is a space or only spaces, tabs or newlines and is not blank

* `istitle()`: returns true if the string consists only of words that begin with uppercase letters

* `startswith('<element>')`: checks the starting value of a string returns true or false

* `endswith('<element>')`: checks the ending value of a string returns true or false

Combining Multiple Strings:

* `join(<['string1','string2']>)`: concatenates multiple strings together

```python
' '.join(['My','name','is','Greg'])
```

Splitting Strings:

* `'some string'.split()`: splits strings into a list of their contents. you can also split a delimiter value for split. for example `'some string'.split('s')` will return `['', 'ome ', 'tring']`

Justifying Strings:

* `'Some String'.rjust(<size>)`: specifiy the size of the right justification and you will of moved your string that size to the right

* `'Some String'.ljust(<size>)`: specifiy the size of the left justification and you will of moved your string that size to the left

* `'Some String'.center(<size>)`: specifiy the size of the center justification and you will of moved your string that size to the center

you can also use a special character argument to hold elements in the empty space `'Some text'.rjust(20, '=')`

Stripping Off Elements of String:

* `strip()`: removes whitespaces and new lines as well as tabs from a string. this can be used with specific sides too. such as `lstrip()` and `rstrip()`. Strip can also take an argument such as `spam.strip('specific word')` to be removed from ths string

you can also remove additional text at a specific letter and partion it with the `.partition('<selection>')` method

Checking Unicode values:

* `ord('A')`: returns the ASCII value for the character in question

