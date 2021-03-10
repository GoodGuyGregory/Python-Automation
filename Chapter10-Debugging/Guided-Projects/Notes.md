## Raising Exceptions

```python
raise Exception('This is an Example Exception Message')

#  using a Try Catch
try:
    if correct != 0:
        print('something if correct')
    else
        raise Exception('#@!$! something went wrong here')
#  print your error 
except Exception as err:
    print('an exception occured' + str(err))
```

## Assertions

assertions are used to check your code's logic and are mainly used for testing. 

they are composed of
* a `assert` keyword
* condition
* comma
* string to display when the condition is `False`

```python
# example:
podBayDoorStatus = 'open'
# assert statement to check work: string to preint when the condition is False
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open"'
```

reassigning of podBayDoorStatus will cause an error if the assertion is checked later in the code. 
assertions must make a program crash if they aren't correct. Assertions are for program errors not user errors


## Logging instead of Printing

used instead of print statements and needs to be configured after importing the `logging` module

```python 
# standard import 
# allow for logging in your code
import logging
#  specify the logging details
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
```