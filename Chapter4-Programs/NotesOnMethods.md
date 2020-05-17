## List Specific Methods:

* append('element') : adds elements to the end of a list

* insert(<#>, 'item'): inserts an element into a list at a specified index

* remove('<item>'): removes an element in the list. returns `ValueError` if the item doesn't exist. if the value appears multiple times it will only remove the *first* instance of the object

* sort(): sorts the elements by alphabetical and numeric value optionally you can reverse the sort with `sort(reverse=True)` only sorts lists of homogenous types. it is also important to note that the sorting method uses *"ASCIIbetical order"* meaning that the values of capital letters will be returned before lowercase letters

to remedy this add `sort(key=str.lower)` to your method call. this makes the sort behave as if all letters are lowercase

**Copy and DeepCopy**

imported from the copy module. these methods allow you maintain the immutability of lists and dictionaries. for example. if you wanted to copy a list's contents and then edit them it will manipulate the referenced lists in this chapter. if you use `copy.copy()` it will create a difference reference pointer to the data and keep the new copied list from creating sideffects on that lists contentes

```python
import copy
spam = ['A','B','C','D']
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
# ['A', 'B', 'C', 'D']
print(cheese)
# ['A', 42, 'C', 'D']
```
