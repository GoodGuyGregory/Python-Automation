import traceback


def spam():
    bacon()


def bacon():
    raise Exception('This is the error message')


# print("Raising Exceptions in methods to prevent breaks")
# print("===================================================")
# # spam()

print('Producing Log Files where errors occured')
print("===================================================")

try:
    raise Exception('This is the error message details')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('the traceback infor was written to errorInfo.txt')
