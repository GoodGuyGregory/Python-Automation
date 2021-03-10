import random


def flip():
    toss = random.randint(0, 1)  # 0 is tails, 1 is heads
    if toss == 1:
        toss = 'heads'
    else:
        toss = 'tails'

    return toss


guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    toss = flip()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guess = input()
        toss = flip()
        if toss == guess:
            print("You've guessed it")
        else:
            print('Nope. you are really bad at this game')
