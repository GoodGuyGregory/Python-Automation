import random
numberOfStreaks = 0


def main():
    headStreak = 0
    tailStreak = 0
    for experimentNumber in range(10000):
        # Code that creates a list of 100 'heads' or 'tails' values.
        print()
        print("Running Trail " + str(experimentNumber))
        trialList = []
        print("=================================")

        for i in range(100):
            # print("Flipping Coin....")
            flipResult = random.randint(0, 1)
            if flipResult == 1:
                # print("Got HEADS")
                trialList.append('H')
            elif flipResult == 0:
                # print("Got TAILS")
                trialList.append('T')

        #  slice list into 6 elements of the sublist and compare with
        for i in range(len(trialList)):
            segmentList = str(trialList[i:i+6])
            # print(segmentList)
            if segmentList == str(['H', 'H', 'H', 'H', 'H', 'H']):
                headStreak += 1
            elif segmentList == str(['T', 'T', 'T', 'T', 'T', 'T']):
                # print(tailStreak)
                tailStreak += 1
    print("Overall Head Streaks: " + str(headStreak))
    print("Overall Tail Streaks: " + str(tailStreak))
    numberOfStreaks = headStreak + tailStreak
    # Code that checks if there is a streak of 6 heads or tails in a row.

    print('Chance of streak: %s%%' % (numberOfStreaks / 10000))


main()
