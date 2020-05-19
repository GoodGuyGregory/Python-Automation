import random
numberOfStreaks = 0


def generateTrails():
    trialList = []
    for i in range(100):
        flipResult = random.randint(0, 1)
        if flipResult == 1:
            print("Got HEADS")
            trialList.append('H')
        elif flipResult == 0:
            print("Got TAILS")
            trialList.append('T')


for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    print()
    print()
    print("Running Trails")
    generateTrails()
    # Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
