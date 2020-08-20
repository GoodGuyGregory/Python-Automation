## Regex in Python

all regular expressions in python require an import of the **re** module as `import re`
create and compile regex objects in order to use regex in python with the `regexVar = re.compile(r'<REGEX>')`

the `search()` on the regex object will allow for the object to be searched for matching characters. it will return *None* if there isn't a match. if there are elements of the pattern to be found it will return a **Match** object. use the returned object's `group()` method to get the actual matching strings result

it is also important to note that the `\` can be used as an escape character for symbols and other elements such as a `(909)` in an area code group. by using `(\(\d{3}\))`

Python Symbol | Meaning
------------- | -------
`[]` | allows for the creation of custom character classes in regex
`*` | matches zero or more of the group that precedes the star can occurs any time in the text. it can catch repeats in the string in question `batRegex = re.compile(r'Bat(wo)*man')` would catch the repeated `wowow` in `mo3 = batRegex.search('The Adventures of Batwowowowoman')`
`^` | creates a negative character class. meaning all of the characters that are not inside of the character class `nonVowelRegex = re.compile(r'[^aeiouAEIOU]')` would return only consonants. it can also be used to indicate that a regex must be matched with a pattern's order  must occur at the beginning of the string `beginsWithHello = re.compile(r'^Hello')
`$` | often used in conjunction with the `^` can be used to specify specific ending values of pattern matching. `endsWithNumber = re.compile(r'\d+$')` this code ensures the regex matches patterns that will end with a digit or more
`.` | wildcard character matches everything with that specific pattern. unless that character is a newline symbol. each wildcard character matches a single character in the regex
`.*` | matches everything found within a string. this can be used for specification in filling out forms etc. `nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')`
`re.DOTALL` | used in conjuction with `.*` to allow for the newline characters to be matched `newlineRegex = re.compile('.*', re.DOTALL)`
`re.IGNORECASE / re.I` | used when compiling regex expressions when you are only concerned about matching letters and not worried about whether the letters are capital or lowercase. pass the `re.I or re.IGNORECASE` as the second argument into the `re.compile(r'<REGEX>', re.IGNORECASE)` for the regex and it will take care of the rest
`+` | matches one or more of the occurances of s specific regex in a string `batRegex = re.compile(r'Bat(wo)+man')` this will only return true if *Batwoman* or *Batwowowowman* was found. but it will not match the string for *Batman* because `(wo)+` is required at least *one* time 
`?` | matches zero or one of the groups preceeding the question mark such as `batRegex = re.compile(r'Bat(wo)?man')` this symbol can also indicate a *non-greedy* group in a search
`|`  | used for matching multiple instances of an expression such as `heroRegex = re.compile (r'Batman|Tina Fey')`  
`(phrase){3,5}` | specifies a range of number to match with the word `phrase`. this for example will match all strings with `'phrasephrasephrase'` all the way up to five instances of the word `phrase` but nothing less than 3. you can leave out the first or second to give it a min or max
`\d` | digit character any single digit fomr 0-9
`\D` | any character that is **not** a numeric digit from 0-9
`\w` | any letter or number and the underscore character commonly known as `word` characters
`\W` | Any Character that is not a letter, numeric digit, or the underscore
`\s` | any character that is a space, tab or new line character `space` characters
`\S` | any character that is not a space, tab or new line character


**Regex Object Methods**

Method | Usage
------- | ------
`search()` | used to find the first occurance of a a regular expression object
`findall()` | returns the strings of every match in the searched string. the default return type is a list of strings as long as there are no groups in the regular expression. such as in this example `phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups` if groups exist then findall will return a list of tuples

[Python Regex Tester](https://pythex.org/)