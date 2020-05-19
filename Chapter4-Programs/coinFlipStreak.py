import random
numberOfStreaks = 0


def main():
    for experimentNumber in range(100):
        # Code that creates a list of 100 'heads' or 'tails' values.
        print()
        print("Running Trail " + str(experimentNumber))
        trialList = []
        print("=================================")

        for i in range(100):
            print("Flipping Coin....")
            flipResult = random.randint(0, 1)
            if flipResult == 1:
                print("Got HEADS")
                trialList.append('H')
            elif flipResult == 0:
                print("Got TAILS")
                trialList.append('T')

        #  slice list into 6 elements of the sublist and compare with
        for i in range(len(trialList)):
            headStreak = 0
            segmentList = str(trialList[i:i+6])
            print(segmentList)
            if segmentList == str(['H', 'H', 'H', 'H', 'H', 'H']):
                headStreak += 1
                print(headStreak)
        for i in range(len(trialList)):
            tailStreak = 0
            segmentList = trialList[i:6]
            if segmentList == str(['T', 'T', 'T', 'T', 'T', 'T']):
                tailStreak += 1

            numberOfStreaks = headStreak + tailStreak
            # Code that checks if there is a streak of 6 heads or tails in a row.

    print('Chance of streak: %s%%' % (numberOfStreaks / 100))


main()
