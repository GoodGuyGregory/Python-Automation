# List Maker Program for Musicians

allArtists = []

while True:
    print('Enter the name of an Artist you are listening to (or enter nothing to stop):')
    #  Breaks out of the program
    name = input()
    if name == '':
        break
    allArtists = allArtists + [name]  # list concatenation
print('The Artist name is: ')
print('==========================')
for name in allArtists:
    print(' ' + name)
